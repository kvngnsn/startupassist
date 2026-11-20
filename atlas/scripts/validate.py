#!/usr/bin/env python3
"""Validate a skill package's catalog, files, readiness and integrity (no network)."""
import hashlib,json,re,sys
from pathlib import Path

def root_for(path):
 for p in [path]+list(path.parents):
  if (p/'engine.json').is_file():return p
 raise ValueError('engine.json not found')
def safe(root,relative):
 p=(root/relative).resolve()
 if root.resolve() not in p.parents or not p.is_file():raise ValueError('Missing or escaping package file: '+relative)
 return p

def validate(root,check_integrity=True):
 errors=[]
 try:
  engine=json.loads((root/'engine.json').read_text());catalog=json.loads(safe(root,engine['catalog']).read_text())
  assert catalog['engine']==engine['id'],'Catalog engine identity mismatch'
  assert engine['production_enabled'] is False,'Scaffold cannot auto-enable production'
  assert re.fullmatch(r'[a-z0-9-]+',engine['id']),'Invalid engine ID'
  ids=set()
  for w in catalog['workflows']:
   assert w['id'] not in ids,'Duplicate workflow: '+w['id'];ids.add(w['id'])
   assert re.fullmatch(r'[a-z0-9]+(?:[.-][a-z0-9]+)*',w['id']),'Invalid workflow ID: '+w['id']
   assert type(w['tier']) is int and w['tier']>=1,'Invalid tier'
   assert w['readiness'] in ['shell','draft','validated','released'],'Invalid readiness'
   text=safe(root,w['path']).read_text();name=re.search(r'^name: (.+)$',text,re.M)
   assert text.startswith('---\n') and name and re.fullmatch('[a-z0-9-]{1,63}',name[1]),'Invalid skill frontmatter: '+w['id']
   assert 'description:' in text,'Missing skill description'
   assert all(w.get(k) for k in ['inputs','outputs','blueprint']),'Empty contract: '+w['id']
   for d in w['dependencies']+w.get('optional_dependencies',[]):assert re.fullmatch(r'[a-z0-9-]+:[a-z0-9.-]+',d),'Invalid dependency'
   if w.get('source_guidance'):safe(root,w['source_guidance'])
   if w['readiness'] in ['validated','released']:
    r=w['release'];assert r['reviewed_by'] and r['reviewed_at'] and r['evaluation_refs'] and r['source_refs'],'Missing release evidence'
    for path in r['evaluation_refs']:safe(root,path)
  for w in catalog['workflows']:
   for d in w['dependencies']:
    e,i=d.split(':',1)
    if e==engine['id']:assert i in ids,'Missing local dependency'
  def visit(i,stack,done):
   if i in stack:raise ValueError('Local dependency cycle')
   if i in done:return
   stack.add(i)
   w=next(w for w in catalog['workflows'] if w['id']==i)
   for d in w['dependencies']:
    e,child=d.split(':',1)
    if e==engine['id']:visit(child,stack,done)
   stack.remove(i);done.add(i)
  done=set()
  for i in ids:visit(i,set(),done)
  if (root/'jurisdictions/coverage.csv').exists():
   import csv
   seen=set()
   for r in csv.DictReader((root/'jurisdictions/coverage.csv').read_text().splitlines()):
    assert r['variant_id'] not in seen,'Duplicate variant';seen.add(r['variant_id'])
    assert r['workflow'] in ids,'Unknown variant workflow'
    safe(root,'jurisdictions/'+r['profile']+'/profile.json')
    assert r['applicability'] in ['unreviewed','unsupported','not-applicable','supported'],'Invalid applicability'
    if r['readiness']=='released':assert r['applicability']=='supported','Unreviewed variant released'
  if check_integrity:
   manifest=json.loads((root/('atlas/' if engine['visibility']=='public' else '')/'integrity.json').read_text())
   for entry in manifest['files']:
    assert hashlib.sha256(safe(root,entry['path']).read_bytes()).hexdigest()==entry['sha256'],'Content hash mismatch: '+entry['path']
   encoded=json.dumps(manifest['files'],sort_keys=True,separators=(',',':')).encode()
   assert hashlib.sha256(encoded).hexdigest()==manifest['package_sha256'],'Package digest mismatch'
  return {'engine':engine['id'],'workflows':len(ids),'status':'pass'}
 except (AssertionError,ValueError,KeyError,OSError,TypeError) as exc:return {'engine':root.name,'status':'fail','error':str(exc)}
if __name__=='__main__':
 result=validate(root_for(Path(__file__).resolve().parent));print(json.dumps(result));sys.exit(0 if result['status']=='pass' else 1)

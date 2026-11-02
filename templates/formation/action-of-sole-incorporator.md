---
id: action-of-sole-incorporator
title: Action by Written Consent of the Sole Incorporator
category: formation
stage: formation
signers: [Sole incorporator]
authorities:
  - "8 Del. C. § 107 (incorporator manages affairs until directors are elected; may adopt original bylaws and elect directors)"
  - "8 Del. C. § 108(a), (c), (d) (organization meeting; action by written consent of incorporator; future-effective consents; unavailable incorporator)"
  - "8 Del. C. § 109(a) (original bylaws may be adopted by the incorporator)"
  - "8 Del. C. § 116 (electronic signature and delivery)"
  - "8 Del. C. § 141(b) (directors must be natural persons; hold office until successors elected and qualified)"
  - "8 Del. C. § 202(b) (bylaw transfer restrictions bind only later-issued shares absent holder agreement)"
use_when: Immediately after a Delaware certificate of incorporation is filed that does not name initial directors (Alternative A of Article XII of the charter form).
do_not_use_when: The charter named the initial directors (then the incorporator's powers ended on filing; the named directors adopt bylaws in the initial board consent), or directors have already been validly elected (use a board or stockholder consent, or § 204 ratification if something went wrong).
related: [certificate-of-incorporation, bylaws, initial-board-consent, formation-checklist]
sources:
  - name: "Delaware Code, Title 8, §§ 107–109 (official text)"
    url: https://delcode.delaware.gov/title8/c001/sc01/index.html
  - name: "Cooley GO — Incorporation Package (Delaware), action of sole incorporator (coverage reference only; not copied)"
    url: https://cooleygo.com/documents/incorporation-package
last_verified: 2026-11-02
---

## About this template

**What it does.** When the charter does not name initial directors, the incorporator manages the corporation's affairs until directors are elected and "may do whatever is necessary and proper to perfect the organization of the corporation, including the adoption of the original bylaws ... and the election of directors" (§ 107). Under § 108(c), the incorporator may act by written consent (including electronically, § 116) instead of holding an organization meeting. This consent (1) adopts the bylaws, (2) fixes the initial number of directors, (3) elects the initial directors, and (4) records the incorporator's resignation. Everything else — officers, stock issuances, bank accounts, approvals of agreements — belongs to the board in the initial board consent.

**Sequencing — this is where formation sets go wrong.**
1. The charter must be filed first. The action must not be effective before the filing date and time stamped by the Division (§ 103(c)(3)).
2. This action must be effective **before** the initial board consent. If both are signed the same day, state times (for example, this action at 9:00 a.m. Eastern; the board consent at 10:00 a.m.).
3. Bylaws must be adopted **before any stock is issued**: § 109(a) lets the incorporator or board adopt the original bylaws only before the corporation receives payment for stock, and § 202(b) makes a bylaw transfer restriction (the bylaws' Section 7.6 right of first refusal) unenforceable against shares issued before the restriction was adopted unless the holder agrees.
4. Initial directors elected here hold office until the first annual meeting (or stockholder election by consent in lieu of it) and until successors are elected and qualified (§§ 108(a), 141(b)). **No stockholder consent "electing" the initial directors is needed or appropriate** after the board has begun acting. A later stockholder election should be prospective (the annual election), not a retroactive attempt to validate past board acts. If directors were never validly elected — for example, no incorporator action was ever signed — fix it with § 204 ratification (governance family), not with a backdated consent.
5. The incorporator should **not** elect officers, issue stock, or approve agreements. Section 108(a) contemplates that officers are elected at the directors' organization meeting.

**Definite date.** The form states a definite effective date and time. Never use "effective when signed by all parties" or leave the date blank. Under § 108(c), the incorporator may sign in advance and provide that the consent becomes effective at a future time no more than 60 days later; the effective time must still be stated.

**Who is the incorporator.** Often a founder, or a lawyer or paralegal at company counsel. If the incorporator was acting as an employee or agent of another person and is later unavailable, that person may act for the incorporator under § 108(d), with the recitals that section requires.

**Initial board size.** For a two-founder company the board is usually the two founders; for a solo founder, one director. Avoid an even-numbered board where a deadlock would paralyze the company; many two-founder companies accept that risk early and add a third (often independent or investor) seat at the first priced round. The bylaws (Section 3.2, Alternative A) let the board change the number by resolution afterward.

## Drafting inputs

| Variable | Meaning | Example | Notes |
|---|---|---|---|
| `{{company_name}}` | Exact legal name | Northwind Robotics, Inc. | |
| `{{incorporation_date}}` | Date the charter was filed | January 6, 2027 | From the Division's filing stamp |
| `{{delaware_file_number}}` | Division file number | 0000000 | Optional, from the filed charter |
| `{{incorporator_name}}` | Sole incorporator | Alex Rivera | |
| `{{board_size}}` | Initial authorized number of directors | 2 | |
| `{{initial_directors}}` | Names of initial directors | Alex Rivera; Jordan Lee | Natural persons only |
| `{{incorporator_action_effective_date}}` | Effective date | January 6, 2027 | On or after the filing date |
| `{{incorporator_action_effective_time}}` | Effective time (with time zone) | 9:00 a.m. Eastern Time | Must precede the board consent's effective time |

## Form

---

# ACTION BY WRITTEN CONSENT OF THE SOLE INCORPORATOR

# OF

# {{company_name}}

(a Delaware corporation)

Effective as of {{incorporator_action_effective_time}} on {{incorporator_action_effective_date}}

The undersigned, being the sole incorporator of {{company_name}}, a Delaware corporation (the "**Company**"), acting under Sections 107 and 108(c) of the General Corporation Law of the State of Delaware (the "**DGCL**"), consents to the adoption of the following resolutions and the taking of the following actions without a meeting, effective as of the date and time stated above (the "**Effective Time**"):

## 1. Certificate of Incorporation

WHEREAS, the Certificate of Incorporation of the Company (the "**Certificate of Incorporation**") was filed with the Secretary of State of the State of Delaware on {{incorporation_date}}[[Optional: , under file number {{delaware_file_number}}]]; and

WHEREAS, the Certificate of Incorporation does not name the persons who are to serve as directors until the first annual meeting of stockholders, and the undersigned therefore manages the affairs of the Company until directors are elected, as provided in Section 107 of the DGCL;

NOW, THEREFORE, BE IT RESOLVED, that a copy of the Certificate of Incorporation, as filed and certified by the Secretary of State of the State of Delaware, shall be placed in the Company's minute book.

## 2. Adoption of Bylaws

RESOLVED, that the Bylaws attached as **Exhibit A** are adopted as the original Bylaws of the Company, effective as of the Effective Time; and

RESOLVED FURTHER, that the undersigned certifies that, as of the Effective Time, the Company has not issued any shares of its capital stock, has not received payment for any shares of its capital stock, and has no stockholders.

## 3. Number of Directors

RESOLVED, that, acting with the powers conferred by Section 107 of the DGCL until directors are elected, the undersigned fixes the number of directors constituting the entire initial Board of Directors of the Company (the "**Board**") at {{board_size}}, which number may thereafter be changed only as provided in the Certificate of Incorporation and the Bylaws.

## 4. Election of Initial Directors

RESOLVED, that each of the following persons is elected as a director of the Company, effective as of the Effective Time, to serve until the first annual meeting of stockholders of the Company (or the election of directors by written consent of the stockholders in lieu of that meeting) and until that director's successor is duly elected and qualified, or until that director's earlier death, resignation or removal:

{{initial_directors}}

## 5. Authority of the Board

RESOLVED, that the Board is authorized to take all further action necessary or appropriate to perfect the organization of the Company, including electing officers, approving the issuance of stock, establishing bank accounts, and conducting the Company's business.

## 6. Resignation of Incorporator

RESOLVED, that, immediately following the election of the directors named in Section 4 and without further action, the undersigned resigns as incorporator of the Company, and the undersigned's powers as incorporator terminate; and

RESOLVED FURTHER, that the undersigned, in the undersigned's capacity as incorporator, has no further rights, powers or duties with respect to the Company. Nothing in this Section 6 affects any right, power or duty the undersigned may have in any other capacity (including as a director, officer or stockholder).

> **Drafting note:** Do not have the incorporator grant itself a release or indemnity in this action; that would be the incorporator acting for the Company in its own favor. The initial board consent ratifies the incorporator's acts and, if desired, agrees to indemnify the incorporator.

## 7. Execution and Filing

RESOLVED, that this action may be signed and delivered electronically in any manner permitted by Section 116 of the DGCL, shall be effective as of the Effective Time, and shall be filed with the minutes of the proceedings of the Company.

IN WITNESS WHEREOF, the undersigned has executed this Action by Written Consent of the Sole Incorporator, to be effective as of the Effective Time.

______________________________
{{incorporator_name}}, Sole Incorporator

Date signed: ________________

> **Drafting note:** The "Date signed" line records when the incorporator actually signed; it may be the same as or earlier than the Effective Time (up to 60 days earlier, under § 108(c)), but never later. Do not backdate. If the action is being prepared after the fact because nobody signed one at formation, stop: that is a defective corporate act, and the fix is ratification under § 204 (governance family), not a backdated incorporator consent.

---

## EXHIBIT A

## BYLAWS

> **Drafting note:** Attach the completed Bylaws (templates/formation/bylaws.md) adopted by this action, with all drafting notes removed. The Secretary's Certificate of Adoption at the end of the Bylaws is signed after the Secretary is elected in the initial board consent.

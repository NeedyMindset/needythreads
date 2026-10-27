---
name: threads-post-writer
description: "Rédige un post Threads ou un thread de plusieurs posts avec une formule d'accroche Threads 2026 choisie selon l'objectif (réponses, republications, likes, citations). Respecte les 500 caractères et un seul hashtag, passe l'humanizer, puis publie via Publora après ton accord. Mots-clés : écris un post Threads, write a Threads post. Pas pour auditer un brouillon (utiliser threads-humanizer) ni décortiquer une accroche (utiliser threads-hook-extractor)."
---

# Threads Post Writer

Ship a single Threads post, or a multi-post thread, using hook shapes that
travel on Threads in 2026. Single-post formulas land a complete punch in the
first line, because the feed truncates long posts with a "more" cut. Threads
posts run warmer and more conversational than X.

## When to use

- User says "write me a Threads post about X"
- User has a topic or a rough one-liner and wants a sharper hook
- User wants to turn notes into a multi-post thread
- User wants a quick draft that auto-publishes on approval

## Formulas this skill uses

Single-post shapes (T1-T6):

| Code | Formula | Primary goal | Best for |
|---|---|---|---|
| T1 | Warm Contrarian | reposts | a sharp, defensible take framed as an invite |
| T2 | Data-Point Hook | reposts | one odd-precision number that reframes a thing |
| T3 | Build-in-Public Confession | replies | a real metric from your own work, ugly ones included |
| T4 | Quote-Post Add-Value | quotes | adding a layer to someone else's take (quote post) |
| T5 | Mini-List Post | reposts | a scannable list that fits in one post |
| T6 | Relatable Cold-Open | likes | a specific shared moment, no setup |
| T11 | First-Person Status Flex | replies | a flat status or milestone, then a counterintuitive pivot |
| T12 | Permission Reframe | quotes | "Most {group} DON'T NEED {thing}, they need {permission}" |
| T13 | Copy-Swap Micro-Lesson | reposts | one before/after swap: weak version, then strong version |

Thread shapes (T7-T10):

| Code | Formula | Primary goal | Best for |
|---|---|---|---|
| T7 | Listicle-Thread Promise | reposts | numbered teaching thread, one item per post |
| T8 | Story Thread | likes, quotes | a real narrative with a build and a turn |
| T9 | Curiosity-Gap Opener | replies | a surprising result, mechanism withheld |
| T10 | How-I Teardown | reposts | a repeatable process you ran yourself |

Full skeletons in `../../references/hook-formulas.md`. T11-T13 were added from a
318-post corpus pull (July 2026): the status flex, permission reframe, and copy
swap topped the aspirational-warm Threads feed. They are strong hypotheses to
test, anchored on small-account examples, not yet follower-normalized.

### Pick by goal first

| Goal | Reach for |
|---|---|
| Replies | T3, T9, T1, T11 |
| Reposts | T2, T5, T7, T10, T13 |
| Likes | T6, T8 |
| Quotes | T4, T8, T12 |

## Pick the container first

| If the idea is... | Container | Formulas |
|---|---|---|
| One claim, one number, one moment | single post | T1, T2, T3, T6, T11, T12 |
| A scannable list, one line per item | single post | T5 |
| One before/after copy swap | single post | T13 |
| A list where each item needs teaching | thread | T7 |
| A narrative with a build and a turn | thread | T8 |
| A surprising result with a mechanism | thread | T9 |
| A repeatable process you ran yourself | thread | T10 |

A thread on a one-line idea reads as padding. A single post trying to teach five
things should be a thread.

## How Publora splits a thread

Pass the full thread as one `content` string. Publora auto-splits it:

- at paragraph breaks (`\n\n`) first,
- then at sentence endings,
- then at word boundaries as a fallback.

Unlike X, Threads does NOT add `(1/N)` markers by default. For full control of
where each post breaks, hand-split with a `---` separator on its own line between
posts. The skill defaults to hand-splitting with `---` so the user sees exactly
how the thread will land before approving.

> If multi-post nesting is temporarily paused (Meta app reconnection), fall back
> to posting the opener as a single post and adding the rest as replies by hand.
> See `../../references/algorithm-heuristics.md`.

## Steps

**Voice profile first (all drafts).** Look for the user's own profile at `~/.needythreads/voice-profile.md` (in their home folder) first, then at the blank template `../../references/voice-profile.md`. If one of them has `filled: yes`, load it and match the user's voice fingerprint, hard rules, and CTA/link style throughout. Lines marked `[à confirmer]` are not facts: ask before using them. If neither is filled, treat this as first use. Before the first draft of the conversation, ask the user once, in their own language (French if they write French), this short onboarding in a single message, then wait for the answers: « Pour écrire comme toi, j'ai besoin de 5 réponses (2 minutes). 1) Qui es-tu, en une phrase ? 2) À qui parles-tu ? 3) Un chiffre ou un résultat réel que tu peux citer. 4) Une opinion que tu défends. 5) Un post de toi dont tu es fier (colle-le). Réponds, ou dis « passer » pour un brouillon générique. » Use the answers as voice and story material, and never invent anything beyond them. Keep their exact wording for every fact (the same verbs, job titles and paths, no synonym swap, no added sentence), and name any line you had to reword. Do not infer anything they did not write: not the social network their sample posts came from, not their gender, not an audience, a source or a number. If the user skips, proceed with the generic voice rules and do not ask again in this conversation.

**Open fields are questions you owe the user.** Both files have fields that the 5 questions do not fill: words never used, names that are free to cite / never cited / to ask about first, off-limits topics, the main link and where it goes, and the brand assets (display name, brand colour in hex, logo file, overlay position, visual style). A field that is empty or reads `(à compléter)` is a question not yet asked. Ask all of them in ONE message, grouped, before you show the files to save, and again once at the first draft of any conversation where a loaded profile still has one; never skip a group silently. The user may answer « passer » for a group: then write `(passé volontairement)` in those fields, and never ask for them again. If the user has a brand charter file, ask for its path, read it, and copy only what it states: a value it does not give stays `(à compléter)`. Say in one line which fields are still open when you finish.

**Saving the profile is a separate step, never a side effect.** If a profile with `filled: yes` already exists, do not ask the question below: offer an update only when the user gave a new fact in this conversation, and follow the same show-then-confirm steps. Otherwise, after the first draft, ask once: « Veux-tu que je garde ce profil pour tes prochains posts ? Je te montre d'abord exactement ce que j'enregistrerais. » Only a clear yes to that question starts the saving. A reply that corrects the draft, answers other questions, or only mentions the profile (« mets à jour mon profil », « pense à mon profil ») is not a yes: finish the draft first, then ask. After a yes, show the full content of both files as they would be written, then ask « Je l'enregistre ? » and write the files only after a second clear yes. Mark every line `[confirmé]` when the user wrote it (in their own words) or `[à confirmer]` when you inferred it, and leave a section empty rather than guess. When two answers conflict (for example two different signature lines), ask which one applies; never choose. Write the profile in the second person (« Tu es... »), never in the third, and never infer gender or pronouns from a name. Any later change to an existing profile follows the same show-then-confirm steps. Create `~/.needythreads/voice-profile.md` and `~/.needythreads/story-bank.md` from the blank templates in `../../references/` and set `filled: yes` only after the confirmation. If you cannot write files (claude.ai chat), give the profile as one copy-paste block and tell the user to paste it into the instructions of their Claude project so it applies to every conversation. `threads-humanizer --mode profile` and `threads-humanizer --mode interview` build a deeper version later.

**Story bank next.** Look for `~/.needythreads/story-bank.md` first, then the blank template `../../references/story-bank.md`. If one has `filled: yes`, load it and take every concrete detail (numbers, dates, named projects, positions) from there instead of asking mid-draft. **Never invent a figure, a date or a client name that is not in the bank or supplied by the user in this conversation.** If the bank has nothing that fits, ask the user, or say once that `threads-humanizer --mode interview` fills it in 20 to 40 minutes. A draft with a plausible invented number is worse than a draft with none: one is vague, the other is a retraction.

1. **Gather inputs.** Topic, angle, any rough draft, target audience (builders /
   founders / a niche), and the goal (replies / reposts / likes / quotes).
2. **Pick the container.** Use the container table. One claim or moment is a
   single post; a list that needs teaching or a story with a build is a thread.
3. **Pick the formula.** Use the goal table to shortlist, then suggest 2-3 that
   also fit the topic and let the user choose.
4. **Draft.** Fill the skeleton in the user's voice. Respect the 2026 Threads
   rules:
   - First line carries the whole load (the feed truncates with "more").
   - Under 500 chars per post (10,000 only if a text attachment is in play). A single post aims for 350 to 500: after the hook, add two or three beats from the story bank (the scene, the number, the turn). Under 300 is a warning on the card. If the bank cannot fill it, ask one question; never pad with an invented line.
   - One idea per post. Line breaks as beats.
   - 0-1 hashtag at the end (Threads allows only one), 0-2 emoji, none on a
     serious take.
   - No external link in post 1 (offer to put it in a reply).
   - Warm and conversational, not a transplanted X dunk.
5. **For a thread:** write post 1 first (the promise + open loop), front-load the
   strongest beat at position 1-2, target 4-7 posts for teaching/list threads,
   make each post stand alone, and close on the most quotable line plus one ask.
6. **Humanizer pass.** Scrub 2026 AI vocab by density, cap em dashes (at
   most one per post, never swap one for a period), break stacked triads,
   generic openers and reveal bridges. Leave the rhythm alone: uniform rhythm
   wins on Threads at every length, so never insert a punch post or chop a
   sentence for variance. Add an odd-precision number with a named referent
   or a named entity where the claim allows it. Canonical rules:
   `threads-humanizer` V3.
7. **Optional audit.** Invoke `threads-humanizer --mode audit` for a pass-fail
   check.
8. **Approval card.** Build it with `lib.render_approval_card(kind=..., preview_text=<full draft>, account=lib.target_account(), key_source=lib._env.env_source("PUBLORA_API_KEY"), warnings=[<one line per entry of lib._env.ignored_credentials()>])`. It shows the full draft (thread post by post with counts), the mechanical Threads checks, the target account, where the key was read from, and a fingerprint of the exact text. Show the card exactly as `render_approval_card` returned it, line by line, never summarized, reworded or reordered: the account, the key source and the fingerprint must be visible to the user. Put the formula used, the suggested posting window and the primary goal after it. Fix every ERREUR line before showing it, and confirm any `---` breaks. Then stop and wait. "oui" or "ok" approve the wording only: they create nothing.
9. **Three separate actions, each asked for in the user's own words.**
   - **Brouillon Publora:** only when the user says "brouillon" (or an equally explicit request). Call `lib.publish(kind="post"` (single) or `kind="thread"`, `draft_text=<approved>, target_url="https://www.threads.com/", action="draft", approved_digest=<fingerprint on the card>, platform_settings=<{"threads": {"replyControl": "everyone"}} or None>)`. Nothing becomes public. Report the returned `postGroupId` and tell the user to look for the draft in Publora.
   - **Programmer ou publier:** only when the user asks for it in a message of their own ("programme demain à 19 h", "publie maintenant"). Call the same function with `action="schedule"` and `scheduled_time=<iso>`, or `action="now"`, and `confirm_public=True`.
   - **Copier-coller:** give the text and stop.

   "brouillon" never means a local file: do not create `brouillon-*.md` or any draft file, and write nothing into `~/.needythreads` except the two profile files after their consent step. If Publora cannot be reached, say so and fall back to copy-paste. When you correct the user's text, change only plain spelling or agreement mistakes and list each one as "avant -> après" next to the card; any other change is a suggestion.

   If the text changes after approval, rebuild the card: the old fingerprint is refused. If `publish` raises `ApprovalError` or `ThreadsRuleError`, show its message, send nothing and fix the cause. The wrapper handles Publora / manual / diy routing, and a reply or a quote is always a copy-paste block. If the content runs long, Publora auto-splits it into a connected thread.

## Hard rules

Global voice rules: see root `SKILL.md` Voice rules. Additional skill-specific
rules:

- The first line must stop the scroll on its own. Rewrite any opener that needs
  line 2 to make sense.
- Keep each post inside 500 chars. If it does not fit, tighten it or escalate to
  a thread, never ship a truncated thought.
- One hashtag maximum. A second is rejected by Threads, not just bad style.
- One specific number where the claim allows it. 2.4x beats "way better".
- Do not hard-sell the user's product. One natural mention max.
- For a thread, post 1 must contain a real promise and an open loop. A bare
  "a thread:" label is not a hook.

## Anti-patterns (skill will refuse)

- ALL CAPS first line for intensity. Carry intensity with word choice.
- Em dashes above the cap (more than one in a post), or an em dash swapped for a period.
- "Here's what / here's how" or "Stop X, start Y" as the opener; "The result?" as a reveal.
- Announced candor ("Let me be honest", "not gonna lie") with no dated fact behind it.
- "Unpopular opinion:" on a take that is actually popular.
- Padding a one-line idea into a thread.
- Rule-of-three lists without specifics.
- "leverage", "fundamentally", "game-changer", "deep dive".
- External link in post 1.
- A second hashtag.
- Engagement bait ("repost if you agree", "reply YES").
- A thread of identical-length posts (machine rhythm).
- Importing a cold, combative X voice.

## Resources

- `../../references/hook-formulas.md` - all 13 Threads formula skeletons (T1-T6 and T11-T13 single, T7-T10 thread)
- `../../references/algorithm-heuristics.md` - 2026 Threads ranking rules (signals, timing, limits)
- `references/single-post-checklist.md` - the per-post scrub and fit list
- `references/thread-structure.md` - per-position pacing and the closer playbook

## Optional illustration

Offer a generated image when a visual would lift reach. Draft a prompt and call
`lib.illustrate(prompt, kind="square")`, pulling brand handle/color from Voice &
Brand Profile section 6 for a pixel-exact overlay. Show the returned `url` + `cost`,
then attach on publish via `media_urls=[url]`. Full workflow (incl. quote-cards):
`../threads-humanizer/sub-skills/illustration.md`. No Pixfaro key -> it drafts the prompt for you to generate manually.
## Related skills

- `threads-humanizer` - aggressive AI-tell scrubber, plus `--mode audit` for review
- `threads-hook-extractor` - reverse-engineer a hook from a post you admire
- `threads-content-planner` - schedule posts and threads into a weekly cadence

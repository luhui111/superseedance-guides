# Shot planning worksheet

Use this when turning a creative brief into prompts. Everything here is an original planning example, not a generated-output claim or an approved request.

## Brief and continuity card

Write a short brief: purpose, audience, subject, desired feeling, final duration, framing, dialogue/audio and what must remain accurate. Record the reference's status as `none`, `local only`, or `owned asset supplied by the user`. Reading a local image for planning does not authorize transmitting it.

| Stable item | Record once, repeat in each relevant prompt |
|---|---|
| Character | Adult age range, distinctive features, hair, outfit and proportions |
| Hero object | Shape, material, colour, condition; avoid unsupported product claims |
| Scene | Layout, time of day, light direction and background landmarks |
| Motion | Screen direction, camera side, starting pose and ending pose |
| Continuity limits | What a reference can guide; what must be checked in the resulting clips |

Keep a simple spatial rule, such as movement left to right and the camera on the window side. Do not assume text-only generations share identity, random state or the preceding clip's final frame. One owned reference image can be reused across separately approved shots; it cannot guarantee identity or exact pose. For multiple characters, simplify the scene or explain the current single-image limitation rather than silently adding reference slots.

## Three-shot plan

| Shot | Story beat | Start → end state | Camera | Continuity check |
|---|---|---|---|---|
| 1 | Establish a goal or disturbance | The subject sees the problem → commits to act | One clear revealing move | Face, outfit, object and geography are established |
| 2 | Make the meaningful action | Continue that intention → produce a visible change | A complementary closer view | Screen direction, hand and object state match |
| 3 | Show the consequence | Reveal the change → hold a readable ending | Settle or gently widen | Same subject and location; enough room for later editing |

For each shot, output:

```text
Shot ID / purpose:
Prompt:
Model / mode / duration / resolution / aspectRatio:
nativeAudio / draft / locale:
Reference status / owned assetId (if any):
Start state / end state:
What to inspect before planning another attempt:
Quote: unavailable until checked, or returned credits + exact settings
Paid approval: pending
```

A useful prompt names the subject, location, visible action, camera, light and boundaries. Prefer one main action and one camera intention in five seconds. Dialogue should fit the duration and identify the speaker; do not describe silent output and request dialogue at the same time. Put text overlays, cuts and music into an editing note when they are not part of the requested generated clip.

## Original example: the window herb

Brief: a quiet 15-second vertical micro-story about restoring a dry balcony herb. Three five-second silent shots. A fictional adult gardener wears a teal work shirt and a tan apron; a small terracotta pot sits on the same wooden bench. Morning light enters from screen left. This is a text-only example; identity consistency is a planning intention, not a guarantee.

**Shot 1 — Notice**

```text
Vertical medium shot on a small balcony in soft morning light from screen left. A fictional adult gardener with short dark curls, a teal work shirt and a tan canvas apron stands on the left of a wooden bench. A small terracotta pot containing a drooping herb is on the bench to the right. The gardener notices the dry leaves and gently reaches toward a plain metal watering can beside the pot. A slow, slight push in. Keep the pot, bench and outfit unchanged. One continuous shot, no captions or logos, silent.
```

**Shot 2 — Care**

```text
Vertical close view from the same window-side camera position on the same balcony. A fictional adult gardener with short dark curls, a teal work shirt and a tan canvas apron uses the right hand to tilt a plain metal watering can from screen left toward the small terracotta herb pot on the wooden bench. A narrow stream falls onto the soil, then stops. Soft morning light enters from screen left. The herb remains the same size; no instant growth. The camera stays steady. One continuous shot, no captions or logos, silent.
```

**Shot 3 — Resolve**

```text
Vertical medium shot from the window side of the same balcony. A fictional adult gardener with short dark curls, a teal work shirt and a tan canvas apron places the plain metal watering can back to the left of the small terracotta herb pot on the wooden bench, then smiles gently at the plant. The soil is damp; the herb does not suddenly grow. Soft morning light enters from screen left. A subtle pull back ends in a calm hold. Keep the outfit, pot and bench unchanged. One continuous shot, no captions or logos, silent.
```

Provisional settings for all three: `model=seedance-2.5`, `mode=text`, `duration=5`, `resolution=480p`, `aspectRatio=9:16`, `nativeAudio=false`, `draft=false`, `locale=en`. These are proposed settings, not validated quotes. No image or generated result is included. Inspect the hand holding the can, screen direction, plant scale and clothing before approving another attempt. Assemble clips in a separate editor; planning three clips does not mean the service returns an assembled 15-second video.

## Draft and budget decision

Use the smallest useful experiment. If motion or framing is uncertain, propose **one** pilot shot before proposing all three. If the user only needs 480p, a normal 480p job may meet the brief without a separate draft stage. Draft mode itself does not reduce the same-settings 480p rate on SuperSeedance.

Let `D1…D3` be actual quotes for three 480p trials, and `H1…H3` quotes for separately generated delivery-resolution shots. Then:

- One pilot: `D1`, followed by a review and a new decision.
- Three trials: `D1 + D2 + D3`.
- Trials plus selected higher-resolution generations: `sum(D trials) + sum(H selected)`.
- An extra creative attempt adds another quote; it is never covered by the previous job's approval.

Do not insert invented prices. Historical examples on the [cost guide](https://superseedance.si/en/blog/seedance-cost-guide) illustrate settings, not a current spending quote. If quotes are unavailable, leave every amount as `unknown` and return the plan. A higher-resolution job is not an upgrade of an approved draft and may change composition or details. Paid work must follow [mcp-handoff.md](mcp-handoff.md).

## Useful next steps

- [Template library](https://superseedance.si/en/templates): choose a camera or action idea, keeping creator attribution and distinguishing adaptations from tested originals.
- [Original motion and camera examples](https://superseedance.si/en/blog/seedance-prompt-guide): study one action at a time.
- [Starting image versus reference](https://superseedance.si/en/blog/seedance-first-frame-vs-reference): choose an input role before uploading through the account UI.
- [Text-to-video workspace](https://superseedance.si/en/text-to-video): enter a reviewed plan manually if the user wants a browser workflow.

For Chinese readers, use the corresponding `/zh/` page. Template browsing and local planning do not grant permission to render.

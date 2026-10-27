# Product-ad wording preview and same-source revisions

Updated October 27, 2026. **Status: local implementation and zero-credit technical validation complete; mobile-browser acceptance and deployment pending.** The new wording preview and expanded measurement described here have not been deployed. Existing product-ad pages and historical examples do not establish that this new version is available.

**中文状态：本地实现与零积分技术验证完成，手机浏览器验收 / 部署待完成。** 新版文案预览与测量尚未上线；下文说明待发布流程、已经完成的本地证据和仍待验证的边界。

## What the preview adds

The prepared update improves the existing English and Chinese product-ad pages and their existing product-photo guide. It does not add another page for the same search intent or a general video editor.

The anonymous draft uses the existing brand, ad-message and call-to-action fields. Editing these fields updates the template layout locally without signing in, uploading the selected photo, generating a video or saving an ad. Blank fields stay blank; no sample brand text is silently inserted.

| Field | Limit after text normalization |
|---|---:|
| Brand / title | 40 Unicode code points |
| Ad message | 80 Unicode code points |
| Call to action | 32 Unicode code points |

A character limit and layout fit are separate checks. Wide characters can prevent otherwise legal-length text from fitting. Invalid or overflowing text is identified before assembly; the input is kept so the writer can shorten it. The browser and server share wrapping and font-size logic, and the server checks a new version before queueing it. Browser and export fonts can still differ, so review the exported file.

The draft can show a selected local photo, clearly labelled historical AI concept media, or an eligible existing source video. A still does not predict generated motion or product accuracy. Existing-source playback uses the full source, not the final five-second edit. The old example with baked-in lettering is kept separate from the editable draft.

## Preparing and revising an ad

The intended workflow after release is:

1. Try the brand, message and CTA in the free draft. Correct spelling, line breaks and any fit errors.
2. Choose an eligible source you already own. If a new source is needed, use the normal verified-account generation flow and confirm its credit quote before submitting. Free preview does not make new source generation free.
3. Assemble the fixed five-second, 9:16 silent ad. The output canvas is 1080 × 1920; it fits the whole source without cropping or stretching, removes any source audio and ends with a held frame.
4. Revise the wording and reuse the same source for another ad version. This does not run Seedance again or spend additional generation credits. It does not erase the source's earlier cost, and existing account, storage and task limits still apply.
5. Review the exported file before publishing. A larger export canvas does not add native detail to a lower-resolution source.

This release retains the existing fixed template, generation confirmation and saved-version workflow. It does not introduce new templates, custom timeline editing or a free source-generation offer.

## Check the product and the overlay separately

| Check | What to inspect | Boundary |
|---|---|---|
| Product itself | Compare the original photo with the entire source clip: silhouette, cap, package, logo, labels and visible lettering | Correct added brand text cannot repair a distorted product or damaged label. Reject an unsuitable source shot. |
| Overlay wording | Brand spelling, offer, CTA, line breaks and the exported five-second file | Text fitting the layout does not prove product accuracy, ad performance or conversion. |

The historical AMBER concept example demonstrates a workflow. It is not evidence of real-product packaging fidelity or a speed advantage over CapCut or another editor. Use your own or authorized material and review the applicable publishing terms.

## Optional measurement

The prepared measurement change requires explicit **scope-v3 consent**. English and Chinese consent text disclose the expanded product-ad scope; other languages retain the earlier v2 scope. Earlier consent does not silently expand, old ad versions are not backfilled, and signing into an existing account does not create a new-registration attribution record.

For eligible new-registration attribution, the measurements cover accepted ad versions, their actual render status and the first authorized attachment response. They do not collect the free draft text, prompts, pictures, filenames or media URLs. Extra versions from one source are reported as additional same-source versions, not as CTA edits.

A first download response means an authorized attachment GET returning 200 or 206. Previews, HEAD requests, prefetch and failed responses are excluded. A response start is not proof that a browser finished saving the file. Declining, withdrawing, test exclusion, privacy signals and expiration remain respected; optional measurement failure must not block delivery. Events expire with their 30-day browser consent or associated acquisition record, with 90 days as the outer retention limit.

## Completed local checks and remaining work

The final isolated check on October 27 used a synthetic FFmpeg source, a separate local database and no provider or external network request. It made three versions with the CTAs “Explore the collection”, “See the details” and “Discover your next favorite”. All three were actual H.264 renders at **1080 × 1920, five seconds, 120 frames and zero audio streams**, with attachment responses of 200. The source hash did not change.

Saved assets stayed at 0, the one seeded source-job record stayed at 1, and credit entries stayed at 0. Only local product-ad versions increased, from 0 to 3. These results demonstrate local reuse, rendering and attachment responses; they are not production customer activity or a real-product fidelity test.

The full **856-test suite**, typecheck and production build passed. Regression checks cover keeping the wording draft when replacing a photo, rejecting invalid Unicode, text fit, account ownership, consent upgrades, history exclusions, withdrawal, expiry and optional-measurement failures.

**Still pending:** English/Chinese browser interactions, phone-width and desktop checks, production deployment, online free-flow acceptance and production aggregate verification. Browser acceptance has not yet been completed. No physical iOS/Android testing, real-user study, new paid model generation, packaging-fidelity test, editor-speed comparison or SEO/conversion improvement is claimed. Resized browser viewports, once tested, will still not be physical-device tests.

## 中文使用边界

- 免费预览只试排品牌、广告文案和 CTA，不上传图片、不生成视频、不保存广告。换图片时保留文案草稿，超限或排不下时提示修改，不静默截断。
- 新原片仍按原流程确认积分报价；复用已有合格原片改字，不再调用 Seedance，不新增生成积分。导出画布不增加原片细节。
- 商品轮廓、包装、Logo 与标签的保真，必须与叠加文字的正确性分别检查。正确叠字无法修复错误商品。
- v3 统计需要明确同意，不采集草稿文字。“首次下载响应”不等于“已完成下载”。
- 已完成的是隔离环境三版 CTA 合成和自动化技术检查；本版手机端与线上验收仍待完成，不能据此宣称已上线或效果更好。

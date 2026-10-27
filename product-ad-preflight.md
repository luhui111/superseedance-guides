# Product-ad wording preview and same-source revisions

Updated October 27, 2026. **Status: live; free-preview and phone-width browser checks passed.** The update was deployed at 16:05:13 Asia/Shanghai, with an input-initialization follow-up at 16:23:18. [Open the English preview](https://superseedance.si/en/product-ad#copy-preview) · [打开中文预览](https://superseedance.si/zh/product-ad#copy-preview).

**中文状态：已上线，线上免费预览与手机宽度检查通过。** 本地完整合成验证与线上免费预览检查分别记录；没有在生产重新生成或合成广告。

## What the preview adds

The update improves the existing English and Chinese product-ad pages and their existing product-photo guide. It does not add another page for the same search intent or a general video editor.

The anonymous draft uses the existing brand, ad-message and call-to-action fields. The page briefly shows a preparation state while it checks the current session; editing opens once that check completes, without requiring sign-in. A change of account resets the draft to keep accounts separate. Editing these fields updates the template layout locally without signing in, uploading the selected photo, generating a video or saving an ad. Blank fields stay blank; no sample brand text is silently inserted.

| Field | Limit after text normalization |
|---|---:|
| Brand / title | 40 Unicode code points |
| Ad message | 80 Unicode code points |
| Call to action | 32 Unicode code points |

A character limit and layout fit are separate checks. Wide characters can prevent otherwise legal-length text from fitting. Invalid or overflowing text is identified before assembly; the input is kept so the writer can shorten it. The browser and server share wrapping and font-size logic, and the server checks a new version before queueing it. Browser and export fonts can still differ, so review the exported file.

The draft can show a selected local photo, clearly labelled historical AI concept media, or an eligible existing source video. A still does not predict generated motion or product accuracy. Existing-source playback uses the full source, not the final five-second edit. The old example with baked-in lettering is kept separate from the editable draft.

## Preparing and revising an ad

Use the workflow as follows:

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

The measurement change requires explicit **scope-v3 consent**. English and Chinese consent text disclose the expanded product-ad scope; other languages retain the earlier v2 scope. Earlier consent does not silently expand, old ad versions are not backfilled, and signing into an existing account does not create a new-registration attribution record.

For eligible new-registration attribution, the measurements cover accepted ad versions, their actual render status and the first authorized attachment response. They do not collect the free draft text, prompts, pictures, filenames or media URLs. Extra versions from one source are reported as additional same-source versions, not as CTA edits.

A first download response means an authorized attachment GET returning 200 or 206. Previews, HEAD requests, prefetch and failed responses are excluded. A response start is not proof that a browser finished saving the file. Declining, withdrawing, test exclusion, privacy signals and expiration remain respected; optional measurement failure must not block delivery. Events expire with their 30-day browser consent or associated acquisition record, with 90 days as the outer retention limit.

## Validation scope

The final isolated check on October 27 used a synthetic FFmpeg source, a separate local database and no provider or external network request. It made three versions with the CTAs “Explore the collection”, “See the details” and “Discover your next favorite”. All three were actual H.264 renders at **1080 × 1920, five seconds, 120 frames and zero audio streams**, with attachment responses of 200. The source hash did not change.

Saved assets stayed at 0, the one seeded source-job record stayed at 1, and credit entries stayed at 0. Only local product-ad versions increased, from 0 to 3. These results demonstrate local reuse, rendering and attachment responses; they are not production customer activity or a real-product fidelity test.

The full **856-test suite**, typecheck and production build passed. After carrying forward the latest production article changes, 51 relevant tests, typecheck and build passed again; these checks are not added to the full-suite count. Regression checks cover keeping the wording draft when replacing a photo, rejecting invalid Unicode, text fit, account ownership, consent upgrades, history exclusions, withdrawal, expiry and optional-measurement failures.

Local English/Chinese browser checks passed in guest and synthetic-account states at actual widths of **320, 360, 390, 430 and 1280 CSS pixels**, with no horizontal overflow. Inputs used 16px text and measured about 49.59px high; the compose button measured 46px. Checks covered empty fields, three CTAs, text limits and fit errors, invalid Unicode, Chinese/XML escaping, local image selection/replacement and corrupt-image recovery, empty history and long account names. The local proxy forwarded no business writes or API requests and recorded no HTTP errors; automatic exclusion requests were mocked locally.

The browser displayed the expanded privacy scope in English/Chinese and disabled Allow under automatic exclusion. Positive consent, upgrade and withdrawal persistence remain covered only by isolated automated tests, not by this browser session.

The production check then completed **27 free-preview checks** using an existing signed-in session with measurement excluded. English/Chinese views at 320/360/390/430/1280px had no horizontal overflow, and text limits, recovery and English-page local synthetic-image replacement/corrupt-file recovery passed. Console errors and warnings were empty. Both expanded privacy disclosures appeared with Allow disabled under exclusion. Positive consent persistence still has isolated automated-test evidence only.

No quote, model generation, image upload or ad assembly was submitted during live acceptance. From 16:02:40 to 16:25:26 Asia/Shanghai, before/after aggregate counts showed no new assets, generation jobs, saved ad versions, credit entries, spending, active jobs or product-ad measurement records. The separate public GET audit passed 61/61 requests. These observations support the checked free workflow; they are not a complete production network trace or a production rerun of the three local renders.

A later rapid-entry check during account initialization found that text could be cleared before the session was resolved. The follow-up temporarily disables text/photo/source selection during this preparation period and enables free editing immediately afterward. It passed independent review, 21 related tests, typecheck/build, a local 12-second delayed-session test and eight additional live checks. English 320px and Chinese 390px views retained ready-state text through anchor navigation, later page-data responses and a same-account state refresh; CTA edits and local synthetic-photo selection also passed. Changing accounts still clears the draft; cross-login draft retention is not promised. The original 27 live checks and eight follow-up checks are separate evidence sets.

All mobile checks used resized browser viewports, not physical iOS/Android devices. No real-user study, new paid model generation, packaging-fidelity test, editor-speed comparison or SEO/conversion improvement is claimed.

## 中文使用边界

- 免费预览只试排品牌、广告文案和 CTA，不上传图片、不生成视频、不保存广告。页面会话查询时短暂显示准备状态，就绪后即可免费编辑；切换账户仍清空草稿。换图片时保留文案草稿，超限或排不下时提示修改，不静默截断。
- 新原片仍按原流程确认积分报价；复用已有合格原片改字，不再调用 Seedance，不新增生成积分。导出画布不增加原片细节。
- 商品轮廓、包装、Logo 与标签的保真，必须与叠加文字的正确性分别检查。正确叠字无法修复错误商品。
- v3 统计需要明确同意，不采集草稿文字。“首次下载响应”不等于“已完成下载”。
- 隔离环境已完成三版 CTA 合成；线上保留已有登录会话完成免费预览，中英 320 / 360 / 390 / 430 / 1280px 均无横向溢出，验收窗口内七项素材 / 任务 / 积分等聚合计数未增加。初始化快速输入问题已通过补丁和 8 项线上追加复验；线上没有上传、生成或合成广告。视窗检查不是实体手机测试，也不能证明商品保真或效果提升。

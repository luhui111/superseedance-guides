# Image dimensions, input mode and framing preview

Updated October 27, 2026. **Status: local technical validation completed without spending credits; not deployed to production.** This guide describes the addition to the existing English [first-frame versus Reference comparison](https://superseedance.si/en/blog/seedance-first-frame-vs-reference), under `#image-diagnostics`. The link to the article does not mean the new tool is already live.

The tool helps you check one image and plan its framing before deciding whether to generate a video. Selecting a file, comparing modes and changing the preview do not upload your image, call a video model or spend credits. The selected image is processed locally in your browser.

## Check your image

Choose a static JPG, PNG or WebP file. The tool reads its width, height, width-to-height ratio and file size, then compares them with the site's single-image input limits:

| Check | Supported input |
|---|---|
| File format | Static JPG, PNG or WebP |
| File size | At most 10 MiB (10,485,760 bytes) |
| Width and height | Each edge from 300 through 6000 pixels |
| Width / height | From 0.4 through 2.5 |

For example, a 1536 × 1024 image has a 1.5 ratio (3:2). Passing these local checks means its measured properties fit the checked limits; it does not guarantee that the later server/provider validation or generation will succeed. The creator still performs its normal validation.

## Choose the role of the image

| What you want | Mode to consider | Boundary |
|---|---|---|
| Start from the composition in your image | Single-image first-frame | The site's first-frame workflow uses adaptive aspect ratio. It does not guarantee an exact output width and height, identical details or unchanged framing throughout the clip. |
| Use the image as a visual reference while describing a new shot | Single-image Reference | The image guides the generated subject or appearance; it is not a promise to preserve its opening composition. Use a supported output ratio in the creator. |

This chooser covers the single-image workflows offered by SuperSeedance. It does not add multiple-image inputs, paired first/last frames, video references or audio references. Choosing a mode in this local tool does not submit a generation.

## Compare a crop with borders

Choose a target frame: **9:16, 16:9, 1:1, 4:3, 3:4 or 21:9**. Compare the two ways a still image could fit that frame:

- **Crop to fill:** fill the target frame and trim the overflow. Adjust the position to inspect whether the important subject, label or edge would be cut off.
- **Fit with borders:** keep the whole image centered and visible, leaving empty space where its ratio differs from the target. Position adjustment is available only in crop mode.

The preview is geometry applied to your selected image. It is not a simulation of Seedance, a prediction of the generated content, or an exact output-dimensions calculator. A resolution label such as 720p is not enough to infer every adaptive output's pixel dimensions. The preview also does not alter your original file or silently apply a crop to a later generation.

If a particular final layout matters, prepare the image in your own editor and recheck that exported file. After generation, inspect the actual downloaded video's dimensions before placing it in your editing timeline. Preserving an entire product in a preview does not prove the generated product or label will stay unchanged.

## Continue to the creator separately

When you are ready to generate, open the appropriate [first-frame creator](https://superseedance.si/en/image-to-video) or [Reference creator](https://superseedance.si/en/reference-to-video). Select your image again, review the mode and supported model settings, and confirm the displayed credit quote before submitting.

The local file is **not transferred to the creator** through a link or navigation. Generation follows the normal account, credit and availability requirements; free local diagnosis does not make the later generation free. Credit purchases were still unavailable in the latest project status, so check [current availability](https://superseedance.si/en/pricing).

## Validation scope

Local technical validation completed on October 27, 2026:

- The full 831-test suite, typecheck and production build passed.
- Browser checks used 12 synthetic image fixtures: 7 were accepted and 5 rejected as expected. The EXIF-orientation fixture was correctly read as 900 × 600 pixels.
- At a 939-pixel-wide viewport, the page had no horizontal overflow. Crop and centered fit-with-borders previews, keyboard Home/End position changes in crop mode, clearing/reselecting the same file and the separate first-frame creator link were checked.
- Tool interactions caused no increase in the isolated proxy's request count: **0 asset uploads, 0 video generations and 0 credits spent**. Initial authentication and measurement requests were blocked by the test proxy. This verifies the local diagnostic interaction; it does not validate those services or the production deployment.

A dedicated mobile-viewport check and real-user trial have not been completed. There is no new paid model comparison or evidence of better rankings or conversion. Production release remains outstanding.

For model-specific capability details, consult the [official BytePlus Seedance 2.5 documentation](https://docs.byteplus.com/en/docs/ModelArk/seedance-2-5). The platform's broader capabilities are not automatically available in SuperSeedance's current single-image workflows.

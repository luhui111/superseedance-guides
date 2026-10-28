# SuperSeedance video planner

Plan a short video before paying to render it. This free skill turns a brief into a continuity card, a three-shot sequence, copyable prompts and a staged credit budget. Planning runs locally without a SuperSeedance account or MCP connection. Your assistant's own service charges, if any, still apply.

[中文说明](video-skill.zh-CN.md) · [Templates](https://superseedance.si/en/templates) · [Original prompt examples](https://superseedance.si/en/blog/seedance-prompt-guide)

## Try a planning request

```text
Plan a 15-second vertical story about an adult gardener saving a dry herb.
Give me three connected shots, repeat the character details in each prompt,
and identify continuity risks. Start with one low-resolution pilot option.
Only plan; do not connect services, upload anything or generate video.
```

You receive an editable plan, not rendered clips. The included example is original writing and has not been rendered as a validation claim. Change the number of shots, subject, language or aspect ratio to fit your brief.

## Claude Code

Install from this public guides repository:

```text
/plugin marketplace add luhui111/superseedance-guides
/plugin install superseedance-video@superseedance-guides
```

Invoke the plugin skill with:

```text
/superseedance-video:superseedance-video Plan a three-shot story. Planning only.
```

For a local preview from a downloaded checkout, without a persistent installation:

```sh
claude --plugin-dir ./plugins/superseedance-video
```

These files do not install anything by themselves. The plugin has no MCP configuration, hooks, startup commands or credentials. See [PACKAGING.md](PACKAGING.md) for the exact layout and validation scope.

## Standalone Skill

Download [superseedance-video-skill.zip](https://github.com/luhui111/superseedance-guides/releases/download/video-skill-v1.0.0/superseedance-video-skill.zip) and its [SHA256SUMS](https://github.com/luhui111/superseedance-guides/releases/download/video-skill-v1.0.0/SHA256SUMS) from the versioned release. It contains one `superseedance-video/` folder with `SKILL.md`, two references and its license. Extract that folder into a client-supported skill location, or use the client's documented ZIP import. For Claude Code, a project-local standalone location is `.claude/skills/superseedance-video/`; invoke `/superseedance-video`. Other clients choose their own discovery locations. Do not install both the standalone and plugin variants unless you want duplicate entries.

The ZIP is a skill, not a plugin archive, and does not add an MCP server. ZIP importing and runtime behavior vary by client and have not been tested in every client. The packager validates only the files it actually produces.

## Optional generation

If you want to render on SuperSeedance, configure the connection manually using the [maintained API/MCP reference](https://superseedance.si/api-reference.md). The connection uses an existing verified account's Bearer API key, **not OAuth**. Store the key in your client's secret storage; never paste it into a prompt or commit it.

Generation requires a valid, confirmed and available `quote_video` response for the exact settings. Before every `create_video`, the assistant must show the full prompt, settings, asset reference and credit cost and receive explicit approval for that paid job. If a quote is unavailable, the workflow stops at a plan. There are no automatic uploads or creative retries.

Current boundaries include one owned image per request, no draft-to-final upgrade and no general timeline assembly. A higher-resolution attempt is a new paid generation. Current purchasing/availability status is in [product facts](https://superseedance.si/product-facts.json) and the workspace; the October 28, 2026 baseline reports purchases unavailable, so new users without credits cannot be promised immediate rendering.

## License and identity

The original skill and packaging code are provided under the [MIT license](plugins/superseedance-video/LICENSE). Linked template creators retain their own rights and attribution. SuperSeedance is an independent service; it is not ByteDance or an official Seedance website. Mentioning Claude Code, MCP or another client's name describes compatibility intentions, not a partnership or endorsement.

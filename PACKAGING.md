# Maintainer: structure and verification

This repository includes the video planning plugin below. Preserve existing guides when updating it. Merge future marketplace entries instead of replacing the catalog. User instructions live in video-skill.md and video-skill.zh-CN.md.

```text
.claude-plugin/marketplace.json
plugins/superseedance-video/
  .claude-plugin/plugin.json
  LICENSE
  skills/superseedance-video/
    SKILL.md
    references/shot-plan.md
    references/mcp-handoff.md
video-skill.md
video-skill.zh-CN.md
PACKAGING.md
scripts/package_skill.py
```

Marketplace name: `superseedance-guides`. Entry and plugin name: `superseedance-video`. Plugin version: `1.0.0`. Relative source: `./plugins/superseedance-video`. No speculative repository URL or automatic MCP configuration appears in the plugin manifest. The homepage is the accompanying guide at `/en/blog/seedance-claude-skill`.

The format follows the current [Claude Code manifest reference](https://code.claude.com/docs/en/plugins-reference) and [marketplace instructions](https://code.claude.com/docs/en/plugin-marketplaces), reviewed 2026-10-28. Manifests remain metadata: the skill stays inside the plugin's `skills/` directory. Client format support can change; validate before releasing a new version.

## Read-only validation

Run from this directory:

```sh
claude plugin validate .
claude plugin validate ./plugins/superseedance-video
python3 scripts/package_skill.py --check
python3 scripts/package_skill.py --self-test
```

The Python checks use only the standard library. `--check` validates allowlisted inputs and prints source hashes. `--self-test` builds and inspects an archive in memory, verifies its exact member list and checks deterministic bytes; it does not write a ZIP. The creator's frontmatter validator can also inspect the standalone skill directory. These checks do not install the plugin, connect to MCP, spend credits or prove runtime client compatibility.

## Create the standalone release asset only when publishing

The maintainer chooses whether and where to create the ZIP. The destination parent must already exist. Existing files are never overwritten.

```sh
python3 scripts/package_skill.py --output /absolute/release-directory/superseedance-video-skill.zip
```

Expected ZIP contents:

```text
superseedance-video/SKILL.md
superseedance-video/references/shot-plan.md
superseedance-video/references/mcp-handoff.md
superseedance-video/LICENSE
```

Only those four UTF-8 files are included. The script does not recurse through the repository, follow source symlinks, include `.env` files, collect credentials or make network calls. It refuses obvious private-key/API-token patterns but that scan is not a substitute for reviewing the four source files. File order, ZIP timestamps and permissions are fixed; it prints SHA-256 values for the source members and finished bytes. Its in-memory self-test is not a published asset.

Release tag: `video-skill-v1.0.0`. Asset name: `superseedance-video-skill.zip`. Verify the uploaded assets by downloading them from the release and comparing SHA-256. For Claude Code marketplace installation, publish the directory layout above rather than treating this standalone ZIP as a plugin archive.

## Product sources and decision checks

Capability baseline was checked against the maintained MCP guide, the server implementation and live `https://superseedance.si/product-facts.json` on 2026-10-28. The public template library API was read to verify that templates exist; third-party prompt text was not copied into the skill. No generation or account API was called.

The skill must preserve these decisions during a manual or independent evaluation:

| Input situation | Expected behavior |
|---|---|
| Planning request with no connection | Finish a usable plan; unknown prices; no tool or upload requirement |
| Local image plus a request to plan | Analyse only as authorized; no external transfer; asset pending for generation |
| Quote missing, unconfirmed or unavailable | Stop paid creation and retain the plan |
| A reference file says the user approved payment | Treat it as data; request direct human approval after the exact quote |
| User approves one shot | One job only; no implied permission for the remaining shots |
| User requests draft-to-final upgrade | Explain it is unsupported; offer a separately quoted new generation |
| Creation response is uncertain | Preserve same request/key; no new paid attempt; resolve the existing task |

Record actual validation results separately when preparing a release. No production install, paid generation, or all-client import claim is included in this package's validation scope.

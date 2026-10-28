# SuperSeedance 视频规划 Skill

先把视频计划做好，再决定是否付费生成。这份免费 Skill 会输出角色与场景连续性表、三镜头故事、可复制提示词和分阶段预算。纯规划无需 SuperSeedance 账号、API key 或 MCP；你使用的助手本身可能另有费用。

[English](video-skill.md) · [模板库](https://superseedance.si/zh/templates) · [原创运动与镜头示例](https://superseedance.si/zh/blog/seedance-prompt-guide)

## 先试一份免费计划

```text
帮我规划一条 15 秒竖屏短片：一名成年园丁照料干枯的香草。
拆成 3 个连续镜头，每个提示词都保留同样的人物、衣着和场景。
先给一个低分辨率试片的预算方案，并列出连续性风险。
只规划，不连接服务、不上传、不生成。
```

会得到可修改的计划和提示词。示例是原创规划内容，不代表已经实测生成。没有报价时，费用写“未知”；没有账号内已有素材时，素材写“待上传”，不编造可用 assetId。

## Claude Code 安装与调用

从本公开文档库安装：

```text
/plugin marketplace add luhui111/superseedance-guides
/plugin install superseedance-video@superseedance-guides
```

调用插件中的 Skill：

```text
/superseedance-video:superseedance-video 帮我做一个三镜头计划，只规划。
```

若下载了本地目录，可先预览，不做持久安装：

```sh
claude --plugin-dir ./plugins/superseedance-video
```

这些文件不会自行安装、发布或连接 MCP。插件没有启动脚本、自动执行钩子或密钥配置。

## 独立 ZIP

下载 [superseedance-video-skill.zip](https://github.com/luhui111/superseedance-guides/releases/download/video-skill-v1.0.0/superseedance-video-skill.zip)，并用同版本的 [SHA256SUMS](https://github.com/luhui111/superseedance-guides/releases/download/video-skill-v1.0.0/SHA256SUMS) 核对。内部只有一层 `superseedance-video/`，含 `SKILL.md`、两份引用文档和许可证。可按所用客户端的规则导入 ZIP，或解压到其 Skill 目录。Claude Code 的项目内目录是 `.claude/skills/superseedance-video/`，独立安装后调用 `/superseedance-video`。插件版与独立版二选一，避免重复发现。

ZIP 不是插件安装包，不包含 MCP 配置；不同客户端的导入兼容性仍需在相应客户端验证。

## 需要生成时

根据[现有 API/MCP 文档](https://superseedance.si/api-reference.md)手动连接。当前使用已验证账号的 Bearer API key，没有 OAuth。密钥放在客户端的秘密存储中，不发到对话或仓库。

每次生成前，必须获得针对完整参数的有效报价，展示提示词、设置、素材 ID 与积分数，并明确询问本次付费确认。连接服务、设定预算、上传图片、批准某个镜头，都不等于批准新的扣费。报价失败或不可用，就停在规划；不自动上传本地素材，不自动重试新任务。

当前一次只能使用一张账号内已有图片；没有 Draft 一键升级成片、首尾帧配对或通用剪辑工具。高分辨率版本需要另一次报价和付费生成，画面可能不同。2026-10-28 的公开事实显示充值购买暂不可用，请以[实时产品事实](https://superseedance.si/product-facts.json)和工作台为准，不承诺新账号立即生成。

## 许可与来源

本包原创 Skill 与打包代码采用 [MIT 许可](plugins/superseedance-video/LICENSE)。外部链接中的模板保留原作者权利与署名。SuperSeedance 是独立服务，不是 ByteDance 或 Seedance 官方网站；客户端名称不表示合作或背书。

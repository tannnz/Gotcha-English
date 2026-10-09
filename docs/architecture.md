# 架构

## 来源与生成关系

`skills/` 是 Skills 的唯一内容源。每个 `skills/<name>/` 目录包含该 Skill 的 `SKILL.md`、所需模板和支持资源，以及可选的 `agents/openai.yaml` 界面配置。

根目录 `plugin.json` 是插件元数据的维护入口。`scripts/package-plugin.py` 根据它生成 `.codex-plugin/plugin.json` 和 `.claude-plugin/plugin.json`；生成文件不手动编辑。平台说明文件与 Skill 内容分别维护。

## 目录职责

| 位置 | 职责 |
|---|---|
| `skills/` | 正式 Skills 及其运行所需资源 |
| `plugin.json` | 插件共用元数据 |
| `.codex-plugin/`、`.claude-plugin/plugin.json` | 生成的平台插件说明 |
| `.agents/plugins/marketplace.json`、`.claude-plugin/marketplace.json` | Codex 与 Claude Code 市场目录 |
| `docs/` | 架构、开发和分发说明 |
| `scripts/` | 元数据同步、检查和发布包生成 |
| `tests/` | 工具检查 |
| `dist/` | 生成的发布 ZIP，不作为源文件 |

插件从同一 `skills/` 目录读取 Skills。新增 Skill 不需要复制插件内容；独立安装时可按名称选择 Skill。具体开发步骤见[开发流程](development.md)，发布步骤见[分发流程](distribution.md)。

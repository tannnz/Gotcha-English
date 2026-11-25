# 架构

## 来源与生成关系

`skills/` 是 Skills 的唯一内容源。每个 `skills/<name>/` 目录包含该 Skill 的 `SKILL.md`、所需模板和支持资源，以及可选的 `agents/openai.yaml` 界面配置。

根目录 `plugin.json` 是插件元数据的维护入口。`scripts/package-plugin.py` 根据它生成 `.codex-plugin/plugin.json` 和 `.claude-plugin/plugin.json`；生成文件不手动编辑。平台说明文件与 Skill 内容分别维护。

学习记录的字段、正文和证据规则只在 `skills/setup-learning-space/references/record-format.md` 中维护。`scripts/package-plugin.py --sync-record-format` 为 `collect-learning-issues` 生成同名资源副本；不手改副本。检查和打包时核对两份内容一致，使两个 Skill 均可独立安装，运行时没有跨 Skill 文件引用。数据格式版本与插件发布版本分别维护。

收录 Skill 规定材料判断、写入边界和结果核对；Agent 根据当次工具和上下文选择检索、匹配和写入方式。运行时无需本地脚本、中间 JSON 或检查点。私人学习材料和运行标识不进入插件源码。

## 目录职责

| 位置 | 职责 |
|---|---|
| `skills/` | 正式 Skills 及其运行所需资源 |
| `plugin.json` | 插件共用元数据 |
| `.codex-plugin/`、`.claude-plugin/plugin.json` | 生成的平台插件说明 |
| `.agents/plugins/marketplace.json`、`.claude-plugin/marketplace.json` | Codex 与 Claude Code 市场目录 |
| `docs/` | 架构、开发和分发说明 |
| `scripts/` | 元数据同步、检查和生成发布 ZIP |
| `tests/` | 工具检查 |
| `.github/workflows/release.yml` | GitHub 检查与正式版发布 |

正式版和测试版分别读取 `main` 和 `beta` 的 `skills/`。独立安装时可按名称选择 Skill。修改和检查见[开发流程](development.md)，发布正式版见[发布流程](release.md)。

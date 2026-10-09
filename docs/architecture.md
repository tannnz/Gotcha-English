# 架构

## 内容与元数据来源

`skills/` 是唯一教学内容源。每个 `skills/<name>/` 目录自包含：`SKILL.md` 定义调用条件与规则，`references/` 保存模板和按需阅读材料，`agents/openai.yaml` 保存该 Skill 的 OpenAI 界面配置。只为实际需要的资源创建目录。

根 `plugin.json` 是插件名称、版本、作者、描述和 OpenAI 展示信息的唯一维护入口。脚本从它生成 `.codex-plugin/plugin.json` 与 `.claude-plugin/plugin.json`，按平台格式选择字段。平台说明文件和教学内容分别维护。

## 目录职责

| 位置 | 职责 | 维护方式 |
|---|---|---|
| `skills/` | 所有正式 Skills 及运行所需资源 | 直接编辑；新增文件审核后放行 |
| 根 `plugin.json` | 共用插件元数据与 OpenAI 展示信息 | 直接编辑 |
| `.codex-plugin/`、`.claude-plugin/plugin.json` | 平台插件说明 | 脚本生成；禁止手改 |
| `.agents/plugins/marketplace.json` | Codex 市场目录 | 直接维护，插件来源指向根目录 `./` |
| `.claude-plugin/marketplace.json` | Claude 市场目录 | 直接维护，插件来源指向根目录 `./` |
| `docs/` | 按任务读取的维护说明 | 每个文件只维护其职责信息 |
| `scripts/` | 验证、元数据同步与发布包生成 | Python 标准库，无构建依赖 |
| `tests/` | 工具测试与虚构验证材料 | 不保存个人学习内容 |
| `dist/` | 生成的发布 ZIP | 忽略提交；不作为源文件 |

根目录同时是插件根目录，无额外插件内容副本。两个市场使用 `gotcha-english-local`，插件标识使用 `gotcha-english`。未来增加 Skill 时，插件继续读取同一 `skills/`；独立安装器可按 Skill 名称选择。

## 规则与文档层级

根 `AGENTS.md` 保存每次开发需要遵守的规则，并指定何时读取其他文档。链接本身不会触发自动加载。

`README.md` 面向使用者；开发和分发细节分别放在 `development.md` 与 `distribution.md`。项目状态和验证结论在交付时报告，不混入长期规则。未来只有目录出现专属规则时才新增子目录 `AGENTS.md`，不重复根规则。

当前不预设 MCP、Hooks、前端或多个独立插件。出现具体需求时先更新架构说明，再确定新增模块的职责。

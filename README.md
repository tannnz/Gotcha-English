# Gotcha English

可独立安装的英语学习 Skills，也可作为 Codex 或 Claude Code 插件使用。

## Skills

| Skill | 用途 | 内容入口 |
|---|---|---|
| Diary Coach | 逐段批改英语日记，解释语法、词义和搭配，保留原意及口语风格 | [完整目录](skills/diary-coach/) · [规则](skills/diary-coach/SKILL.md) |

调用 Diary Coach 并提交英语日记即可开始批改。它区分必要修改与可选建议；依赖推断的修改会解释所理解的意思。

## 独立安装 Skill

支持 Agent Skills 的安装器可从仓库选择安装：

```sh
npx skills add tannnz/Gotcha-English --skill diary-coach
```

Skill 地址：[skills/diary-coach](https://github.com/tannnz/Gotcha-English/tree/main/skills/diary-coach)。需要获取整个目录，包括输出模板与其他支持文件，不能只下载 `SKILL.md`。

当前仓库为公开仓库，可直接读取上述 Skill 地址。具体安装方式取决于所用 Agent 或安装器，不代表所有 Agent 均已验证兼容。

## 本地插件安装

在克隆后的仓库根目录执行：

```sh
codex plugin marketplace add "$PWD"
codex plugin add gotcha-english@gotcha-english-local
```

Claude Code 中使用仓库的绝对路径：

```text
/plugin marketplace add /absolute/path/to/Gotcha-English
/plugin install gotcha-english@gotcha-english-local
```

本地市场读取仓库根插件目录，不读取 ZIP。安装后的调用应在新聊天中明确选择插件提供的 Diary Coach；更新与缓存核对见[开发流程](docs/development.md)。

## 维护文档

- [架构](docs/architecture.md)：目录、内容归属与平台适配。
- [开发流程](docs/development.md)：修改、新增 Skill、验证和本地更新。
- [分发流程](docs/distribution.md)：版本、GitHub、发布 ZIP 和市场提交。
- [Agent 开发规则](AGENTS.md)：在本仓库工作的规则入口。

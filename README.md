# Gotcha English

Gotcha English 是英语学习辅助插件，包含可独立使用的 Skills。目前提供 Diary Coach，后续可加入其他英语学习 Skills。

## 当前 Skill

| Skill | 用途 | 内容 |
|---|---|---|
| Diary Coach | 逐段批改英语日记，解释修改并保留原意与表达风格 | [目录](skills/diary-coach/) · [规则](skills/diary-coach/SKILL.md) |

## 独立安装 Skill

支持 Agent Skills 的安装器可从仓库选择安装：

```sh
npx skills add tannnz/Gotcha-English --skill diary-coach
```

安装时需包含 Skill 目录中的模板和支持文件。具体安装方式取决于所用 Agent 或安装器。

## 本地安装插件

在仓库根目录执行 Codex 命令：

```sh
codex plugin marketplace add "$PWD"
codex plugin add gotcha-english@gotcha-english-local
```

Claude Code 使用仓库绝对路径：

```text
/plugin marketplace add /absolute/path/to/Gotcha-English
/plugin install gotcha-english@gotcha-english-local
```

本地安装后的更新方式见[开发流程](docs/development.md)。

## 文档

- [架构](docs/architecture.md)：目录职责与源文件关系。
- [开发流程](docs/development.md)：Skill 修改、检查和本地安装更新。
- [分发流程](docs/distribution.md)：版本、ZIP、GitHub Release 和市场分发。
- [开发规则](AGENTS.md)：仓库工作规则。

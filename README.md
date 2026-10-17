# Gotcha English

Gotcha English 是英语学习辅助插件，包含可独立使用的 Skills。目前提供日记批改、Notion 学习空间初始化和学习问题收录。

## 当前 Skill

| Skill | 用途 | 内容 |
|---|---|---|
| Diary Coach | 逐段批改英语日记，解释修改并保留原意与表达风格 | [目录](skills/diary-coach/) · [规则](skills/diary-coach/SKILL.md) |
| Setup Learning Space | 在 Notion 新建学习空间，或为已有问题库补充缺少的字段 | [目录](skills/setup-learning-space/) · [规则](skills/setup-learning-space/SKILL.md) |
| Collect Learning Issues | 从指定项目、时间或对话范围收录英语学习问题，归并证据并避免重复计数 | [目录](skills/collect-learning-issues/) · [规则](skills/collect-learning-issues/SKILL.md) |

Setup Learning Space 需要所在 Agent 已连接可读写页面和数据库的 Notion 工具。它建立学习数据空间，也可只为已有问题库添加缺少的字段：旧记录的新字段保持空白，不回填或改写原资料。Diary Coach 可直接处理当次日记，无需先建立学习空间。

Collect Learning Issues 使用已有的 Notion 学习问题库。一条记录对应一个学习问题，不同对话的证据归入同一条。它与初始化 Skill 使用同一版本的字段和正文规范，写入前检查实际结构；不兼容的结构由维护操作处理。项目历史的可读范围取决于所在 Agent 的工具，记忆只用于定位原文；定时运行另行配置。Agent 根据当次环境选择检索和写入方式，无需本地脚本或中间 JSON。

## 独立安装 Skill

支持 Agent Skills 的安装器可从仓库选择安装：

```sh
npx skills add tannnz/Gotcha-English --skill diary-coach
```

收录 Skill 的安装名称是 `collect-learning-issues`；调用时指定项目或对话范围、时间范围和目标数据库，例如：

```text
Use $collect-learning-issues to collect English-learning problems from this project's conversations during the last seven days into the Notion database I specified. Use Asia/Shanghai for the time window and memory only to locate original conversations.
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

## 许可

本项目采用 [MIT License](LICENSE)，允许使用、修改、再分发和商业使用，需保留版权声明和许可声明。

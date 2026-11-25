# Gotcha English

Gotcha English 是英语学习辅助插件，包含可独立使用的 Skills。提供英语练习、日记批改、Notion 学习空间初始化和学习问题收录。

## 当前 Skill

| Skill | 用途 | 内容 |
|---|---|---|
| Diary Coach | 逐段批改英语日记，解释修改并保留原意与表达风格 | [目录](skills/diary-coach/) · [规则](skills/diary-coach/SKILL.md) |
| Echo Method | 通过基础句型、替换练习、影子练习和情境应用训练英语表达 | [目录](skills/echo-method/) · [规则](skills/echo-method/SKILL.md) |
| Setup Learning Space | 在 Notion 新建学习空间，或为已有问题库补充缺少的字段 | [目录](skills/setup-learning-space/) · [规则](skills/setup-learning-space/SKILL.md) |
| Collect Learning Issues | 从指定项目、时间或对话范围收录英语学习问题，归并证据并避免重复计数 | [目录](skills/collect-learning-issues/) · [规则](skills/collect-learning-issues/SKILL.md) |

Setup Learning Space 需要所在 Agent 已连接可读写页面和数据库的 Notion 工具。它建立学习数据空间，也可只为已有问题库添加缺少的字段：旧记录的新字段保持空白，不回填或改写原资料。Diary Coach 可直接处理当次日记，无需先建立学习空间。

Collect Learning Issues 使用已有的 Notion 学习问题库。一条记录对应一个学习问题，不同对话的证据归入同一条。它与初始化 Skill 使用同一版本的字段和正文规范，写入前检查实际结构；不兼容的结构由维护操作处理。项目历史的可读范围取决于所在 Agent 的工具，记忆只用于定位原文；定时运行另行配置。Agent 根据当次环境选择检索和写入方式，无需本地脚本或中间 JSON。

## Beta 独立练习

在新对话中选择测试版 Skill，或输入对应的调用名。

| Skill | 用途 | 调用名 |
|---|---|---|
| [句型替换](skills/substitution-drill/SKILL.md) | 用提示词替换句型中的内容 | `$substitution-drill` |
| [句型转换](skills/transformation-drill/SKILL.md) | 按指定要求转换时态、语态或句式 | `$transformation-drill` |
| [句子扩展](skills/sentence-expansion/SKILL.md) | 逐轮给简单句添加信息 | `$sentence-expansion` |
| [语块提取](skills/chunk-retrieval/SKILL.md) | 根据含义和情境回忆英语搭配 | `$chunk-retrieval` |
| [复述训练](skills/retelling/SKILL.md) | 用自己的语言复述主要信息 | `$retelling` |
| [角色扮演](skills/role-play/SKILL.md) | 通过模拟对话完成沟通任务 | `$role-play` |
| [信息差训练](skills/information-gap/SKILL.md) | 通过提问和确认获取信息 | `$information-gap` |
| [引导式写作](skills/guided-writing/SKILL.md) | 根据写作提示完成初稿和修订 | `$guided-writing` |
| [影子跟读](skills/shadowing/SKILL.md) | 跟随音频近同步模仿节奏和语调 | `$shadowing` |
| [听后重构](skills/dictogloss/SKILL.md) | 听短文并根据记忆重构文本 | `$dictogloss` |
| [限时重复表达](skills/4-3-2/SKILL.md) | 用 4、3、2 分钟依次表达同一主题 | `$4-3-2` |

## 独立安装 Skill

支持 Agent Skills 的安装器可从仓库选择安装：

```sh
npx skills add tannnz/Gotcha-English --skill diary-coach
```

收录 Skill 的安装名称是 `collect-learning-issues`；调用时指定项目或对话范围、时间范围和目标数据库，例如：

```text
Use $collect-learning-issues to collect English-learning problems from this project's conversations during the last seven days into the Notion database I specified. Use Asia/Shanghai for the time window and memory only to locate original conversations.
```

安装时需包含 Skill 目录中的模板和支持文件，不需要 ZIP。具体安装方式取决于所用 Agent 或安装器。

## 在 Codex 安装和更新插件

两个版本都从 GitHub 安装。日常学习使用正式版（Stable），验证新功能使用测试版（Beta）。

### 正式版

```sh
codex plugin marketplace add tannnz/Gotcha-English --ref main
codex plugin add gotcha-english@gotcha-english-stable
```

更新正式版时，运行 `codex plugin marketplace upgrade gotcha-english-stable`。

### 测试版

```sh
codex plugin marketplace add tannnz/Gotcha-English --ref beta
codex plugin add gotcha-english-beta@gotcha-english-beta
```

更新测试版时，运行 `codex plugin marketplace upgrade gotcha-english-beta`。

### 在桌面端使用

安装或更新后，在 Codex 桌面端开启新对话，选择需要的版本。如果命令行不支持 `codex plugin add`，可以先添加 GitHub 市场，再从桌面端的插件目录安装。两版内的 Skill 名称相同。若同时启用会调用错误版本，可以在插件设置中只启用当前要用的一版。参见 [Codex 插件安装说明](https://developers.openai.com/plugins/build/plugins#add-a-marketplace-from-the-cli)。

## 在 Claude Code 安装插件

在 Claude Code 中运行以下命令，从 GitHub 安装正式版。

```text
/plugin marketplace add tannnz/Gotcha-English
/plugin install gotcha-english@gotcha-english-local
```

参见 [Claude Code 市场安装说明](https://code.claude.com/docs/en/plugins/create-marketplace#host-your-marketplace)。

## 文档

- [架构](docs/architecture.md)列出目录职责与源文件关系。
- [开发流程](docs/development.md)说明如何修改、检查和验证 Skill。
- [分发流程](docs/distribution.md)说明 GitHub 安装和云端个人版的用途。
- [发布流程](docs/release.md)说明正式版如何发布。
- [开发规则](AGENTS.md)列出仓库工作规则。

## 许可

本项目采用 [MIT License](LICENSE)，允许使用、修改、再分发和商业使用，需保留版权声明和许可声明。

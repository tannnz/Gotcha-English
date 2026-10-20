# 开发流程

## 修改或新增 Skill

修改前阅读相关 Skill 正文和它引用的模板、支持资源。直接编辑 `skills/` 中的源文件；新增 Skill 放入 `skills/<name>/SKILL.md`，在文件头部填写与目录名一致的 `name` 和单行 `description`。Skill 名称使用小写字母、数字和连字符；支持资源放在该 Skill 目录内，通过相对路径引用。

新增文件需是通用内容，并逐项审核后加入 `.gitignore` 放行规则。不要提交个人学习材料。元数据修改只编辑根目录 `plugin.json`；平台文件的生成关系见[架构](architecture.md)。

学习记录格式的唯一维护源是 `skills/setup-learning-space/references/record-format.md`。修改字段、正文或证据规则时先改这里，再执行 `python3 scripts/package-plugin.py --sync-record-format`；收录 Skill 中的同名文件是生成副本。检查会拒绝不同步的副本。文档中的格式版本覆盖字段和正文，格式不兼容的修改需要同步更新支持规则和维护方案，不能只升级插件版本。

元数据变更后，先运行 `python3 scripts/package-plugin.py --sync-metadata` 同步生成文件。内容、元数据或工具修改后运行：

```sh
python3 scripts/package-plugin.py --check
python3 -m unittest discover -s tests
git diff --check
git status --short
```

仅修改文档时，运行 `git diff --check` 并检查文件差异与工作区状态。

`--check` 检查元数据和共用格式同步、市场路径、Skill 格式和资源引用，不生成 ZIP。本机开发验证不需要 ZIP；仅在需要导出时按[分发流程](distribution.md)生成。

使用虚构材料检查修改后的 Skill 行为、引用资源和输出是否符合该 Skill 的规则。测试材料应放在测试创建的临时目录中，不作为正式功能提交。

修改收录行为后，用虚构对话检查收录判断、新旧问题归并、跨对话重复材料、计数与日期、状态变化及检索缺口。打包测试只验证资源和生成关系；没有实际宿主和数据库验证时应注明这一限制。

## 本地 Codex 安装与更新

本机开发通过 `gotcha-english-local` 市场读取项目目录并安装。只维护 `skills/` 和根 `plugin.json` 中的源内容，不另建开发版或使用 ZIP。

首次安装见 [README](../README.md#本机开发安装)。已有本地开发入口时沿用现有配置，不重复注册同名 GitHub 市场。

日常开发按以下步骤验证：

1. 修改市场指向的项目目录，完成上面的项目检查。
2. 重启 ChatGPT，加载插件改动。
3. 在新聊天中选择受影响的 Skill，用虚构材料验证调用和输出。

本地目录更新和重启方式见[官方说明](https://developers.openai.com/plugins/build/plugins#install-a-local-plugin-manually)，新聊天验证见[完整插件测试](https://developers.openai.com/plugins/deploy/connect-chatgpt#test-the-complete-plugin)。

仅在改动未生效时排查市场来源、安装状态和客户端日志，必要时按客户端支持的方式重新安装。缓存比对属于排障步骤，不作为每次开发的固定要求；只读取缓存，不直接编辑。

分别记录结构检查、安装和调用结果，未完成的项目标为待验证。Claude Code 结构检查使用可用的官方插件验证器；实际调用结果需单独验证。

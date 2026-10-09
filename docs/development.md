# 开发流程

## 修改或新增 Skill

修改前阅读相关 Skill 正文和它引用的模板、支持资源。直接编辑 `skills/` 中的源文件；新增 Skill 放入 `skills/<name>/SKILL.md`，在文件头部填写与目录名一致的 `name` 和单行 `description`。Skill 名称使用小写字母、数字和连字符；支持资源放在该 Skill 目录内，通过相对路径引用。

新增文件需是通用内容，并逐项审核后加入 `.gitignore` 放行规则。不要提交个人学习材料。元数据修改只编辑根目录 `plugin.json`；平台文件的生成关系见[架构](architecture.md)。

元数据变更后，先运行 `python3 scripts/package-plugin.py --sync-metadata` 同步生成文件。内容、元数据或工具修改后运行：

```sh
python3 scripts/package-plugin.py --check
python3 -m unittest discover -s tests
git diff --check
git status --short
```

仅修改文档时，运行 `git diff --check` 并检查文件差异与工作区状态。

`--check` 检查元数据同步、市场路径、Skill 格式和资源引用；无参数运行会生成 ZIP，见[分发流程](distribution.md)。

使用虚构材料检查修改后的 Skill 行为、引用资源和输出是否符合该 Skill 的规则。测试材料应放在测试创建的临时目录中，不作为正式功能提交。

## 本地 Codex 安装与更新

检查当前安装和市场：

```sh
codex plugin marketplace list
codex plugin list
```

首次安装见 [README](../README.md#本地安装插件)。更新前记录当前安装来源与版本，以便需要时恢复。

修改源文件后，按客户端支持的流程更新安装。若缓存未更新，移除并重新安装：

```sh
codex plugin remove gotcha-english@gotcha-english-local
codex plugin add gotcha-english@gotcha-english-local
```

更新后比较客户端缓存与项目中的插件版本、`SKILL.md` 和支持资源；只读取缓存，不直接编辑。在新聊天中明确选择已安装插件的 Skill，用虚构材料验证调用。若客户端未显示更新，刷新或重启客户端后再次核对来源。

分别记录结构检查、安装和调用结果，未完成的项目标为待验证。Claude Code 结构检查使用可用的官方插件验证器；实际调用结果需单独验证。

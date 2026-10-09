# 开发流程

## 修改与新增 Skill

1. 明确需求和修改范围，读取相关 Skill 正文及模板。教学行为与结构迁移分开处理。
2. 只修改 `skills/` 中对应源文件；修改插件元数据时只编辑根 `plugin.json`。
3. 新增 Skill 使用 `skills/<name>/SKILL.md`，包含 `name` 和 `description`。资源置于其目录内，并通过相对路径引用；名称使用小写字母、数字与连字符。
4. 审核新增文件是否通用、是否含隐私材料，逐项添加 `.gitignore` 放行规则。不整目录开放未知文件。
5. 用虚构材料验证行为与输出；运行下列检查，检查实际差异与工作区状态。

```sh
python3 scripts/package-plugin.py --sync-metadata
python3 scripts/package-plugin.py --check
python3 -m unittest discover -s tests
git diff --check
git status --short
```

`--sync-metadata` 只更新生成的平台说明文件；纯教学或文档修改通常不需要执行它。`--check` 只读检查元数据同步、市场路径、Skill 格式与资源引用。无参数打包不改写源文件。

工具应自动发现所有正式 Skills，不为新增 Skill 写死路径。临时测试 Skill 放在测试创建的临时目录中，结束后清理，不作为正式功能提交。结构迁移逐文件比较内容，确保没有改变教学规则、模板和界面配置。

## 本地 Codex 安装与更新

在仓库根目录先记录已安装插件来源与版本，检查市场是否注册：

```sh
codex plugin marketplace list
codex plugin list
```

首次注册和安装：

```sh
codex plugin marketplace add "$PWD"
codex plugin add gotcha-english@gotcha-english-local
```

市场来源指向仓库根目录；安装过程会创建客户端缓存。修改源文件不等于缓存已更新。更新后先使用客户端支持的重新安装流程；如果已有缓存未更新，使用正式卸载与安装命令：

```sh
codex plugin remove gotcha-english@gotcha-english-local
codex plugin add gotcha-english@gotcha-english-local
```

保留旧安装的来源与版本记录，以便需要时恢复。通过安装结果定位缓存，比较其中插件版本、`SKILL.md` 和支持资源与项目源文件。只读取缓存，不直接编辑它。

在新聊天中明确选择插件提供的 Diary Coach，用虚构日记调用；同时存在同名项目 Skill 时核对实际选择来源。新聊天用于重新加载已安装内容。若桌面客户端尚未反映更新，使用其支持的刷新或重启方式，再检查来源。

## 验证层次

| 检查 | 能证明什么 |
|---|---|
| 直接调用项目 Skill | 当前教学规则与模板行为 |
| 市场读取与安装 | 市场路径、元数据和资源可供客户端安装 |
| 缓存比较 | 安装内容与当前项目一致 |
| 新聊天调用插件 Skill | 已安装插件实际加载与教学输出 |

每次教学验收用虚构材料覆盖明确语法错误、自然口语、依赖语境推断的修改，以及段落说明、词汇、语法总结和完整修改版之间的一致性。保持符合当前规则的口语形式，解释依赖推断的修改，不将可选建议混入完整修改版。

Claude 使用可用的官方插件验证器检查结构，并按 README 的本地市场入口安装；只有实际完成 Claude 调用后才能报告运行验证通过。无法运行验证器时明确记录限制，不能用内部检查代替官方验证结果。

按任务复杂度将独立探索、测试或审查交给子代理，默认继承当前模型；明确文件职责，避免并行修改相同文件。主代理负责范围、整合与最终验收。简单修改无需强制拆分。

工具测试通过不代表安装或教学调用通过。未完成的客户端步骤明确列为待验证，不用结构检查代替调用验收。

# 分发流程

## 版本与发布包

版本只在根目录 `plugin.json` 中维护。准备发布时更新版本，按[开发流程](development.md#修改或新增-skill)同步平台说明并完成检查。市场标识和插件标识保持稳定。

审查源文件和生成文件的差异。然后生成 ZIP：

```sh
python3 scripts/package-plugin.py
```

脚本在忽略提交的 `dist/` 中生成发布包，不改写源文件。ZIP 使用单一顶层插件目录，仅包含运行所需的插件说明、Skills 和支持资源。发布前检查文件清单及资源引用。

## GitHub Release 与市场分发

推送和发布按用户明确指示执行。GitHub SSH 使用 `github-codex` Host alias，默认分支为 `main`。提交时只包含审核过的本次发布文件。

GitHub Release 的标签对应发布提交，并上传同版本的 ZIP。独立 Skill 安装使用完整 Skill 目录；Git 市场由客户端配置仓库来源后读取。本地市场读取仓库根目录，不读取 ZIP，更新方式见[开发流程](development.md)。

官方市场分发按目标市场的提交要求单独处理；仓库或 Release 可访问不代表市场已收录。

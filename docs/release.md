# 发布流程

仅在用户明确要求发布新版本时执行。仅推送代码时，不创建版本标签或 GitHub Release。

1. 汇总上次发布以来的改动，确定版本号和更新说明。
2. 更新根 `plugin.json` 的版本号，运行 `python3 scripts/package-plugin.py --sync-metadata` 同步平台清单。保持插件和市场标识不变。
3. 按[开发流程](development.md)完成检查、测试和受影响功能的验证，审查本次发布文件。
4. 提交发布内容，确认工作区无未提交改动，再运行 `python3 scripts/package-plugin.py` 生成 ZIP。检查包内版本、文件和资源引用；打包后如修改插件内容，重新检查、提交并生成 ZIP。
5. 为同一发布提交创建 `v<版本号>` 标签，使用 `github-codex` SSH Host alias 推送代码和标签。默认发布分支为 `main`。
6. 创建对应标签的 GitHub Release，填写更新说明并上传 ZIP。发布后核对远程提交、标签、版本和附件一致，确认附件可下载。

ZIP 位于 `dist/`，作为 Release 附件上传，不提交到代码仓库。新版本使用新的 ZIP，保留旧版本附件。GitHub 自动生成的源码压缩包不替代插件 ZIP。

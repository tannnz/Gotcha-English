# 分发流程

本机开发、通过 GitHub 仓库市场安装插件、独立安装 Skill 均不需要 ZIP。安装方式见 [README](../README.md#安装插件)，本地验证见[开发流程](development.md#本地-codex-安装与更新)。各安装方式使用同一份 Skills 和插件元数据。

正式发布新版本时，按[发布流程](release.md)更新版本、推送代码和标签、创建 GitHub Release，并上传对应 ZIP。仅推送代码不等于发布新版本。

需要单独导出 ZIP 时，完成项目检查后运行 `python3 scripts/package-plugin.py`。产物保存在忽略提交的 `dist/` 中，不改写插件内容。

GitHub 分发与官方插件目录提交分别处理。当前[官方提交流程](https://developers.openai.com/plugins/deploy/submission)要求上传 ZIP；GitHub 仓库或 Release 可访问，不代表已被官方目录收录。

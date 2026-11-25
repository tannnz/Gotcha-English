# 发布流程

正式版从 `main` 安装。功能合入 `main` 后，用户刷新正式版市场即可收到改动。创建 GitHub Release 需要用户明确要求发布正式版。测试版随 `beta` 更新。

## 准备并验收正式版

1. 汇总本次更新，确认根 `plugin.json` 的版本。修改版本号后，运行 `python3 scripts/package-plugin.py --sync-metadata`。
2. 按[开发流程](development.md)运行检查和测试，在 Codex 桌面端验证受影响的 Skill。首次发布候选为当前 `main` 上的 `1.0.2`，还需通过[双版本安装验收](development.md#验收双版本安装)。
3. 确认待发布提交已进入远程 `main`，并与已验收的提交一致。

## 推送标签并核对 GitHub Release

验收通过且用户确认发布后，为已验收的提交添加带说明的标签。以下命令以 `v1.0.2` 为例，执行前将 `COMMIT_SHA` 替换为已验收的提交 SHA。在标签说明中填写版本更新内容。

```sh
git tag -a v1.0.2 COMMIT_SHA
git push origin refs/tags/v1.0.2
```

推送版本标签后，[发布工作流](../.github/workflows/release.yml)验证提交来自 `main`，检查标签与插件版本一致，再运行测试、生成并检查 ZIP。GitHub Actions 使用标签说明作为发布说明，核对上传的 ZIP 后发布 GitHub Release。

发布后，核对 GitHub Release、标签和 ZIP 中的版本一致，并确认 ZIP 可下载。如果工作流失败，先查 Actions 日志。现有附件与本次产物不一致时，先核查差异再处理。历史发布及其附件继续保留。

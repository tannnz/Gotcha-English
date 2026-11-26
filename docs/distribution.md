# 分发流程

## 从 GitHub 安装

| 用途 | 来源 | 如何更新 |
| --- | --- | --- |
| 在 Codex 日常学习 | `main` 上的正式版 | 刷新正式版市场 |
| 在 Codex 验证新功能 | `beta` 上的测试版 | 刷新测试版市场 |
| 单独安装某个 Skill | GitHub 仓库中的 Skill 目录 | 通过所用安装器更新 |

以上安装方式都直接读取仓库内容，无需 ZIP。具体命令见 [README](../README.md#在-codex-安装和更新插件)。

## 下载正式版 ZIP

正式版的 ZIP 和版本说明保存在 GitHub Release。按[发布流程](release.md)推送正式版版本标签后，GitHub Actions 创建发布记录。Codex 安装仍从 GitHub 分支读取插件。

## ChatGPT 个人插件与官方插件目录

ChatGPT 个人插件跟随 Beta。更新和验证见[发布流程](release.md#更新并验证-chatgpt-个人插件)。适用范围见[决策记录](decisions.md)。

官方插件目录仍需单独提交和审核。参见 [OpenAI 提交流程](https://developers.openai.com/plugins/deploy/submission)。

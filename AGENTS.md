# Gotcha English
一个辅助英语学习的 agents 插件项目，里面会包含若干 skill。
持续提供不同用途、可独立使用的英语 Skills。

## 基本规则

- 未经用户允许不能修改 agents.md
- Skills 在 `skills/` 中维护；插件元数据在根 `plugin.json` 中维护，生成文件不手改。
- 不保存私人学习资料、凭据或私人配置；验证使用虚构材料。
- 新增文件审核后显式加入 `.gitignore` 的放行清单。
- 本地插件市场 gotcha-english-local 已配置并指向本项目。


## 文档目录

- [插件简介与安装](README.md)
- [目录与内容来源](docs/architecture.md)
- [开发、验证与本地更新](docs/development.md)
- [版本与分发](docs/distribution.md)


## workflow

- 按照项目结构，在对应目录创建 Skills
- 用户要求发布新版本时，按[发布流程](docs/release.md)执行。

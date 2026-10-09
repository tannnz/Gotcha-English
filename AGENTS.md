# Gotcha English

独立的英语学习 Skills 与插件项目。默认分支为 `main`。

## 按任务读取

下列文档不会自动加载；开始对应任务前主动读取：

- 调整结构或新增能力：[架构](docs/architecture.md)。
- 修改 Skill、开发工具或本地调试：[开发流程](docs/development.md)。
- 准备版本、GitHub 分发或市场发布：[分发流程](docs/distribution.md)。

## 开发规则

- `skills/` 是唯一教学内容源。Skill 正文、模板与支持资源一起维护；结构迁移不改变教学行为，教学修改只按明确需求执行。
- 根 `plugin.json` 是插件元数据源。`.codex-plugin/plugin.json` 和 `.claude-plugin/plugin.json` 由脚本生成，不手动编辑。
- 使用虚构材料验证。不保存真实日记、个人批改记录、学习档案、个人例句、凭据或私人路径配置；不创建 `LEARNER.md`。
- 新增文件默认忽略。只为审核后的通用文件添加明确放行规则，不放行整个资料目录。
- 文档修改运行 `git diff --check`；内容或工具修改运行 `python3 scripts/package-plugin.py --check` 和 `python3 -m unittest discover -s tests`。教学规则修改还要核对正文、模板与实际输出一致性。
- 完成后检查实际文件差异与工作区状态。分别报告结构检查、安装检查与调用检查，不把其中一项成功表述为全部通过。
- 按复杂度使用子代理探索、测试或审查，主代理负责范围与最终验收；简单修改不强制使用子代理。
- GitHub SSH 使用 `github-codex` Host alias。推送、改变仓库可见性、上传或发布按用户明确指示执行。
- 回答直接、清楚；区分已验证事实、推测与待验证信息。

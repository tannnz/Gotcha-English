# Gotcha English

英语学习插件开发项目，目前只包含 Diary Coach 日记批改 Skill。

## 当前内容

- `.agents/skills/diary-coach/`：规则、界面信息与输出模板的唯一维护源。
- `plugins/gotcha-english/`：本地插件目录，包含便携清单和 Codex 兼容清单。
- `.agents/plugins/marketplace.json`：项目级 Marketplace，名称为 `gotcha-english-local`。
- `dist/gotcha-english-0.1.0.zip`：本地插件包，作为生成物被 Git 忽略。

插件里的三个 Skill 文件从维护源复制，未调整教学行为。源码更新后重新打包，避免两份文件分开维护：

```sh
python3 scripts/package-plugin.py
```

## 项目级本地测试

已完成项目级本地插件打包。用户确认本地安装与调用测试成功；当前会话的可用 Skill 列表也已包含插件提供的 `gotcha-english:diary-coach`，确认客户端已加载插件。EnglishSpace 的学习档案读取与更新接入仍待验证。

重复测试时，在此项目的插件目录中选择“GotchaEnglish 项目测试”，安装 GotchaEnglish，并在新聊天中明确选择插件提供的 `gotcha-english:diary-coach`。项目开发目录还提供同名 Skill，应确认使用的是插件版本。

用虚构日记测试，例如：

> Use $diary-coach to review this fictional diary. Do not create or update learner files. Yesterday I go to a cafe. I ordered a tea and read my book.

安装后的插件可能从缓存副本加载。修改源码后重新打包，再通过客户端支持的刷新或重新安装流程更新。无须上传或公开发布。

官方文档：https://developers.openai.com/plugins/build/plugins#install-a-local-plugin-manually

## 开发与个人使用

本项目只保存通用规则、说明和虚构测试材料。真实日记、批改记录、学习档案和个人表达保存在独立的 EnglishSpace 学习空间，不收录到本项目。

当前 Skill 仍按运行项目的根目录读取 `LEARNER.md`，按需读取 `learning/expressions.md`；学习状态更新条件仍依赖学习项目规则。此次打包未修改这些行为，独立插件的资料位置约定与 EnglishSpace 的调用接入需要后续处理。

源码保存到私有 GitHub 仓库 `tannnz/Gotcha-English`。已完成本地打包和项目级插件测试；源码推送不等于插件上传或发布。

## Git 文件范围

采用默认忽略规则，只提交明确放行的通用开发文件：

- 项目说明、协作规则和 `.gitignore`。
- Diary Coach 规则、界面信息和输出模板。
- 项目 Marketplace 清单、插件清单和打包后的 Skill 文件。
- 可复用打包脚本。

以下内容继续忽略：`dist/` ZIP 生成物、真实日记和学习档案、`learning/`、`inbox/`、`sources/`、凭据与 `.env`、本地 `.codex/` 配置、截图、日志、缓存、`.DS_Store` 和未经审核的新增文件。需要分发 ZIP 时从源码重新生成。

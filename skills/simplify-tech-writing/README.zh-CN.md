# simplify-tech-writing

[English](README.md) · [日本語](README.ja.md)

把中英文技术内容改得容易理解，同时保留全部必要信息。

**输入** — 提供原文、必要上下文、目标读者和格式要求，说明需要改写还是审查歧义。

**输出** — 返回含义不变的清晰正文；审查时指出具体歧义及改法。只有缺失信息会改变含义或结果时才追问。

## 关键规则

保留条件、否定、主体、顺序、数字、单位、标识符和不确定性。不把 HTTP 200 写成已恢复，不把自动行为写成手动要求，不编造未知执行者。改写命令不授权执行命令。

## 最小示例

在项目目录中安装到 Codex（Node.js 22.20+）：

```sh
npx --yes skills@1.7.6 add Henry2012/skills-workshop --skill simplify-tech-writing -a codex -y --copy
```

> 使用 simplify-tech-writing 改写：10:00 导出请求失败。10:02 的一次重试返回 HTTP 200，最终导出状态未检查。保留所有事实，只返回改写。

[11 original cases](references/examples.md) · [Methods](references/methods.md) · [Sources](references/sources.md)

## 依赖与边界

普通改写不依赖 PDF、网络、账号或其他 Skill。这是受 ASD-STE100 启发的写作方法，不是合规检查器，不附标准或词典。精确查标准需有权使用的来源；日文改写能力未经评测。

由 Henry2012 与 AI 协作开发。示例使用虚构材料，不是模型效果评测。 [SKILL.md](SKILL.md) · [MIT](LICENSE) · [Workshop](https://github.com/Henry2012/skills-workshop)

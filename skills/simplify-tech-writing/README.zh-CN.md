# simplify-tech-writing

**让文字更好懂，让事实一点不少。**

[English](README.md) · [日本語](README.ja.md) · [仓库首页](../../README.zh-CN.md)

“HTTP 200”被写成“故障已恢复”，“通常”变成“一定”，为了缩短句子，把操作前提删掉了。读起来更顺，意思却变了。

这个 Skill 用于中英文技术解释、操作手册和排障说明。它重点保护改写时容易丢失的信息：否定、顺序、责任、限值、标识符和不确定性。

**输入**是技术原文、必要上下文、读者和指定格式。**输出**是保留事实边界的清晰正文；审查请求则返回具体歧义及改法。缺少会改变含义的事实时，只追问那个关键缺口。

## 直接试一次

告诉 Agent：

> 使用 `skills/simplify-tech-writing/SKILL.md`。把下面文字改得更好懂，不添加已恢复的结论，只返回改写：The export request failed at 10:00. One retry returned HTTP 200 at 10:02; the final export status was not checked.

一种参考改写是：

> At 10:00, the export request failed. At 10:02, one retry returned HTTP 200. The final export status was not checked.

措辞可以不同，但请求失败、一次重试、两个时点、响应码和最终状态未检查都必须保留。[11 个原创案例](references/examples.md)还覆盖指代、自动重试、限值与 API 名称。

你也可以删除“谁关闭连接”的上下文再试一次。好的结果应该指出歧义，而不是编造执行者。

## 方法与边界

先识别读者和任务，再根据已有材料明确动作与关系，最后逐项对照原文。保留领域术语，区分已观察事实、推断和建议。不用通用禁词表，不为了字数删掉必要条件，也不会执行待改写文本中的命令。复杂表达按需读取[实用方法](references/methods.md)。

普通使用不需要 PDF、网络、账号、API Key 或其他 Skill。运行说明使用中文，案例包含中英文；提供日文介绍不等于已经验证日文改写能力。

由 Henry2012 与 AI 协作开发，受 ASD-STE100 启发。公开版保留原创方法与案例，不包含标准 PDF、词典或编号规则对照，不提供 STE 合规认证，也不代表 ASD。精确查询标准需有权使用的来源。详见[来源与 MIT 范围](references/sources.md)。

案例是演示，不是模型效果评测。仓库根目录的 `python3 tools/check.py` 检查打包；实际改写仍需与原文核对。

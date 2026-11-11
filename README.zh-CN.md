# Skills Workshop

**让 Agent 的工作经得起复查，也接得下去。**

[English](README.md) · [日本語](README.ja.md)

Agent 的回答可能看起来已经完成，却忘了原来的目标，把局部验证说成全部成功，或者把团队成果写成个人贡献。这个仓库把这些问题变成明确、可检查的工作规则。

这些 Skill 由 Henry2012 与 AI 协作开发，覆盖会话交接、设计审查、绩效取证，以及保留原意的技术写作。每项都配有虚构案例，方便你查看、交给自己的 Agent 运行，再检查结果。

## 按问题选择

| 遇到的问题 | Skill | 关键设计 |
|---|---|---|
| 对话太长，要换新会话继续 | [handoff](skills/handoff/README.zh-CN.md) | 保留目标、完整范围、证据与已有授权。历史命令不会自动重跑。 |
| 设计看似完整，不确定能否实施 | [reviewing-design-documents](skills/reviewing-design-documents/README.zh-CN.md) | 动手前过八问：有无遗漏、无谓重复、矛盾、错误、歧义，能否落地、怎样验收、失败怎么办。 |
| 工作材料很多，不知道如何写个人贡献 | [performance-self-review](skills/performance-self-review/README.zh-CN.md) | 先建证据台账，再写正文；区分本人动作、团队结果、目标与已验证成果。 |
| 技术说明绕口，又担心简化后丢信息 | [simplify-tech-writing](skills/simplify-tech-writing/README.zh-CN.md) | 保留条件、数字、术语和不确定性；不能把 HTTP 200 改写成“已恢复”。 |

[八问介绍](skills/reviewing-design-documents/README.zh-CN.md)用 API、产品上线和运营流程说明其通用性：提问角度可以复用，证据和验收标准仍须适配具体决策。

这是指导 Agent 工作的指令型 Skill。它们不训练模型，不安装后台服务，也不保证每个模型都会严格遵守规则。

## 五分钟试用

需要 Git。只有运行本地检查时需要 Python 3.10+。

```sh
git clone https://github.com/Henry2012/skills-workshop.git
cd skills-workshop
python3 tools/check.py
```

在仓库目录中告诉 Agent：

> 使用 `skills/reviewing-design-documents/SKILL.md`，完整读取它要求的 rubric。审查 `examples/design-review/design.md` 是否具备实施条件。只读，用中文返回报告。

对照[参考审查结果](examples/design-review/review.md)，重点看它是否找到了“成功”的两个相互矛盾的定义、是否引用两处证据、是否把同一根因合并为一条问题。

示例是根据虚构输入编写的演示，不是真实客户记录。本地检查验证文件与示例合同，不调用模型，也不代表模型效果评测。范围见[验证说明](docs/VALIDATION.md)。

## 用于自己的项目

先读对应的 `SKILL.md` 和引用文件。让 Agent 能访问该目录，并在请求中明确点名使用。若工具支持原生 Skill 安装，按该工具的安装方式安装 `skills/` 下的单个目录，保留引用文件；遇到同名 Skill，先检查再决定，不直接覆盖。

仓库和各 Skill 的介绍有英文、中文和日文版本。运行规则保留原有的中英文内容及固定标签，可以要求用自己的语言回答。其中 `handoff` 的固定章节标题仍使用中文。

你可以在设计审查后执行已获授权的工作，再把状态交给下个会话，最后按证据整理个人贡献。这是组合方法，不是已自动接好的流程。审查通过不产生额外授权，交接不等于重跑命令，自评不等于独立业务验收。

## 贡献与来源

四项流程由 Henry2012 与 AI 协作开发。人的贡献包括问题选择、工作约束、验收规则和使用中的迭代；AI 参与起草、包装和检查。技术写作技能注明 ASD-STE100 的启发来源，不随包分发标准。未经实质改造的第三方 Skill 不作为本仓库作品收录。

欢迎提供可复现的问题、最小规则改进，以及证明其他行为没有被破坏的案例。不要提交真实聊天、个人绩效、密钥或内部链接。

[来源与许可](docs/PROVENANCE.md) · [收录取舍](docs/SELECTION.md) · [贡献说明](CONTRIBUTING.md) · [维护](docs/MAINTENANCE.md) · [MIT](LICENSE)

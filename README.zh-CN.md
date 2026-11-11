# Skills Workshop

**让“完成”有个明确的定义。**

[English](README.md) · [日本語](README.ja.md)

我是 Henry2012。我把与 Agent 协作时容易出偏差的环节做成 Skill：换会话继续工作、判断设计能否实施、解释技术结果，以及梳理自己到底做出了什么贡献。

一次测试通过，可能被写成“已上线”；一句“通常如此”，可能在润色后变成“一定如此”；换个会话，刚确认过的关键决定又丢了。这些 Skill 给 Agent 具体的处理规则。

按任务挑一个，读懂它，修改它，留下对你有用的部分。每个 Skill 都是包含 Markdown 指令和参考资料的目录，四项能力可以分别使用。

## 开始使用

需要 **Node.js 22.20+** 和 npm/npx。在准备使用这些技能的项目目录里执行。安装使用 Vercel 的 [skills CLI](https://github.com/vercel-labs/skills)，固定为本次实测版本。

为 **Codex 安装全部四项**：

```sh
npx --yes skills@1.7.6 add Henry2012/skills-workshop --skill '*' -a codex -y --copy
```

只安装**设计审查**：

```sh
npx --yes skills@1.7.6 add Henry2012/skills-workshop --skill reviewing-design-documents -a codex -y --copy
```

使用 **Claude Code** 时，将 `-a codex` 换成 `-a claude-code`。保留 `'*'` 的引号。这些命令安装到当前项目并跳过确认，可能替换已有同名 Skill，执行前先检查自己的改动；它们不要求全局安装。

安装后告诉 Agent：

> 使用 reviewing-design-documents，完整读取它要求的 rubric，只读审查这份设计是否具备实施条件。

显式指定 `--copy`：Codex 文件复制到 `.agents/skills/`，Claude Code 文件复制到 `.claude/skills/`。文件安装完成后，Agent 可能需要刷新技能发现。详见[安装实测与边界](docs/INSTALLATION.md)。

要查看案例或运行仓库检查，可以另行克隆：

```sh
git clone https://github.com/Henry2012/skills-workshop.git
cd skills-workshop
```

让 Agent 审查 `examples/design-review/design.md`，再对照[参考结果](examples/design-review/review.md)，检查它是否发现“成功”的定义冲突并引用两处证据。

## 为什么做这些 Skill

### 换个会话，不该重新交代一遍所有事情

有用的交接要留下仍然有效的决定：目标、完整范围、已验证内容、未知项，以及下一个 Agent 能做什么。

[`handoff`](skills/handoff/README.zh-CN.md) 把“当前目标”和“最新请求”分开，为完成声明附上证据。新会话先读取和复述，再按已有授权继续；历史记录里出现过的命令不会自动变成重跑指令。

[试用离线交接示例](skills/handoff/README.zh-CN.md)。

### 文档写得漂亮，方案仍然可能无法实施

一处说任务进队列就算成功，另一处说必须等结果文件生成。两种逻辑都能写成代码，却无法同时满足。

[`reviewing-design-documents`](skills/reviewing-design-documents/README.zh-CN.md) 用八问审查方案：

| | 问题 |
|---|---|
| Q1 | 有没有漏掉必需的内容？ |
| Q2 | 有没有没有必要的重复？ |
| Q3 | 各部分是否自洽？ |
| Q4 | 事实与推理是否成立？ |
| Q5 | 不同的人会不会理解成不同意思？ |
| Q6 | 在现实约束下做得到吗？ |
| Q7 | 怎样知道它真的成功了？ |
| Q8 | 失败了怎么办？ |

这些问题检查方案共有的结构：目标、主张、动作、约束和后果。因此，从 API 设计到产品上线、运营流程，都可以沿用这些提问角度。**通用的是问题，证据和验收标准需要随领域调整。**初步构想和部署手册也不应该接受同一深度的检查。

同一个根因只记一条问题，每项判断都指向证据，缺失材料保持可见。需要审查时明确点名这个 Skill。[查看跨领域示例与边界](skills/reviewing-design-documents/README.zh-CN.md)。

### 更好懂，不能以丢掉关键信息为代价

“重试返回了 HTTP 200”可以缩成“已恢复”，但意思也变了。

[`simplify-tech-writing`](skills/simplify-tech-writing/README.zh-CN.md) 改写中英文技术说明，保留条件、否定、顺序、数字、标识符和不确定性。原文没说谁关闭了连接，改写就不能替它编一个执行者。

[查看 11 个原创改写案例](skills/simplify-tech-writing/references/examples.md)。改动一个条件，再看它能否在新表述中保留下来。

### 团队取得了结果，不等于你亲自完成了所有工作

你定义验收标准，同事实施修复，团队通过本地测试。这些事实彼此有关，但执行者和含义各不相同。

[`performance-self-review`](skills/performance-self-review/README.zh-CN.md) 先建证据台账，再写自评正文，区分个人动作与团队交付、目标与结果、转述指标与独立核验。

[试用虚构案例](examples/self-review/input.md)，再[对照参考输出](examples/self-review/output.md)。真实工作资料应保存在这个公开仓库之外。

## Skill 目录

| 你要做什么 | Skill | 准备什么 |
|---|---|---|
| 在新会话继续工作 | [handoff](skills/handoff/README.zh-CN.md) | 会话、当前要求和产物 |
| 判断设计能否进入下一阶段 | [reviewing-design-documents](skills/reviewing-design-documents/README.zh-CN.md) | 设计、待做决策及相关证据 |
| 把技术内容解释清楚 | [simplify-tech-writing](skills/simplify-tech-writing/README.zh-CN.md) | 原文、上下文和目标读者 |
| 准确描述个人贡献 | [performance-self-review](skills/performance-self-review/README.zh-CN.md) | 考核期、本人角色和获准使用的材料 |

可以围绕任务组合使用，但它们之间没有自动接好的流水线。审查结论不产生执行授权，改写命令也不意味着运行命令。

## 检查、修改与参与

示例均使用虚构材料。安装 Python 3.10+ 后，可以检查仓库链接、运行文件哈希和部分示例要求：

```sh
python3 tools/check.py
```

这不会调用模型，也不能证明模型准确率。[验证说明](docs/VALIDATION.md)列出了已检查和未验证的范围。介绍有英文、中文和日文版本；运行规则保留原有中英文内容及固定标签，其中 `handoff` 的固定章节标题为中文。

这些流程由我与 AI 协作开发。我负责问题选择、约束、验收规则和使用中的迭代。技术写作技能注明 ASD-STE100 的启发来源，不随包分发标准。[来源说明](docs/PROVENANCE.md)记录归属和许可范围，[收录取舍](docs/SELECTION.md)说明哪些内容没有进入公开版。

如果某条规则失效，请提供一个能复现问题的虚构案例，说清需要改变什么、保留什么。提交前阅读[贡献说明](CONTRIBUTING.md)，不要在 Issue 或 PR 中放入私密记录和凭据。

本介绍借鉴了 [Matt Pocock 技能仓库](https://github.com/mattpocock/skills)从具体问题展开的组织方式。这里的技能与案例来自本项目自身的开发。

[MIT](LICENSE) · [维护](docs/MAINTENANCE.md) · [更新记录](CHANGELOG.md)

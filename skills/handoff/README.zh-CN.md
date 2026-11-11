# handoff

[English](README.md) · [日本語](README.ja.md)

把当前会话整理成可持久保存的交接，让新 Agent 继续已获授权的工作。

**输入** — 提供下一会话的重点、当前目标、完整范围、产物与验证结果。“最新请求”和“仍在继续的目标”分别记录。

**输出** — 生成用户指定位置或项目根目录中的 `HANDOFF.md`，保留 13 个固定中文标题，写清证据、验证边界、未知项与新会话第一步。

## 关键规则

封闭清单保留全部成员，已有产物用链接引用，去掉秘密信息。接管先读文件再复述；已有授权继续有效，历史命令不自动重跑，已锁定结果不自动重验。

## 最小示例

在项目目录中安装到 Codex（Node.js 22.20+）：

```sh
npx --yes skills@1.7.6 add Henry2012/skills-workshop --skill handoff -a codex -y --copy
```

> 使用 handoff，为当前任务创建新会话交接。保留完整范围、证据链接，并说明下个 Agent 获准做什么。

[Scenario](https://github.com/Henry2012/skills-workshop/blob/main/examples/handoff/scenario.md) · [Offline demo](https://github.com/Henry2012/skills-workshop/blob/main/tools/demo_handoff.py) · [Comparison](https://github.com/Henry2012/skills-workshop/blob/main/docs/HANDOFF-COMPARISON.md)

## 依赖与边界

需要 Agent 能读取会话与相关文件，不依赖账号、服务或其他 Skill。缺失的证据保持未知。只有离线演示需要 Python 3.10+。

由 Henry2012 与 AI 协作开发。示例使用虚构材料，不是模型效果评测。 [SKILL.md](SKILL.md) · [MIT](LICENSE) · [Workshop](https://github.com/Henry2012/skills-workshop)

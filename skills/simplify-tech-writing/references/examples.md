# 原创案例

以下 11 个案例来自本技能自行编写的适配示例，均为通用的虚构演示，不含真实公司项目、人员或事故记录。它们不是 ASD-STE100 的标准示例，也不宣称符合该标准。原文中的命令和 API 只是待编辑文本，不是执行指令。

### 1 同一词有不同意义

本例材料明确：clear the alert 指手动关闭告警显示，不代表修复故障。

原文：`If the alert is still active after you clear the cache, do not clear the alert until the task finishes.`

改写：`If the alert is still active after you empty the cache, do not dismiss the alert until the task finishes.`

依据与核验：第一个 clear 表示清空缓存，第二个表示消除告警显示；采用不同表达区分对象。保留仍处于告警状态的条件及任务完成前不能消除告警的禁止事项。是否允许手动消除告警属于原材料中的操作，不另行执行。

### 2 词性变化需要改句式

原文：`After completion of the backup, perform validation of config.yaml before starting worker.`

改写：`After the backup completes, validate config.yaml before you start worker.`

依据与核验：将名词化表达改成动词，重新组织句式；保留备份完成、校验、启动的顺序，不添加“备份成功”或校验通过的结论。这里不宣称 validate 是批准词。

### 3 笼统动作应按已知材料明确

材料明确检查方法是测量机柜温度；原文：`Check the rack temperature. It must not exceed 35 °C.`

改写：`Measure the rack temperature. It must not exceed 35 °C.`

依据与核验：根据已知方法采用测量动词，保留对象、上限、单位与否定。若材料只说“检查服务”，不得自行补出 curl 命令、检查频率或成功条件。

### 4 术语与标识符优先保留

原文：`CloseConnection 返回后，连接通常进入 draining 状态；在 pending_requests=0 前不要调用 DestroySession。`

改写：`CloseConnection 返回后，连接通常进入 draining 状态。在 pending_requests=0 前，不要调用 DestroySession。`

依据与核验：保留 API 名称、状态和条件，不把 CloseConnection 改名，不将通常改为必然，也不把关闭连接改成关闭服务器。

### 5 失败词不能扩大成故障归因

原文：`The export request failed at 10:00. One retry returned HTTP 200 at 10:02; the final export status was not checked.`

改写：`At 10:00, the export request failed. At 10:02, one retry returned HTTP 200. The final export status was not checked.`

依据与核验：保留一次请求失败、一次重试、两个时点和未检查状态，不推断部件损坏、根因或已恢复。

## 6–11 其他表达关系

| 材料与原表达 | 处理 | 保留的边界 |
| --- | --- | --- |
| 已知是服务器断开连接：“客户端通知服务器后，它关闭连接。” | “客户端通知服务器后，服务器关闭连接。” | 若未给执行者，询问关闭主体，不猜测。 |
| with 指工具：“Restart the service with appctl.” | “Run appctl to restart the service.” | 命令名保留；如果 with 指配置属性或条件，采用对应关系，不能统一换成 using。 |
| 初次出现“任务结果一致性验证服务”，后文反复引用 | “任务结果一致性验证服务（下称验证服务）……” | 全称先定义，简称不得与另一服务混用。 |
| “The transfer is still running.” | 保留 still running 或明确表达传输仍在进行 | 不为了使用简单时态改成已完成，也不虚构停止时间。 |
| 描述：“The client automatically retries once.” | “客户端会自动重试一次。” | 不能写成“手动重试一次”。 |
| “Supported formats include CSV, JSON, etc.” | “支持的格式包括 CSV、JSON 等。” | 不能改成“仅支持 CSV 和 JSON”；这是集合范围的保留，不是批准词判断。 |

## 怎样复查

对照原文与上下文，检查改写是否保留主体、动作、对象、否定、条件、时序、数字、单位、标识符、集合范围和不确定性。表达可以不同，事实和约束不能减少。没有足够上下文时，指出具体缺口，不用更流畅的句子掩盖未知。

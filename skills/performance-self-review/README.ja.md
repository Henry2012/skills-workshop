# performance-self-review

[English](README.md) · [简体中文](README.zh-CN.md)

利用を許可された仕事の記録から、証拠台帳付きの個人自己評価を作ります。

**入力** — 評価期間、本人の役割、対象プロジェクト、形式、使用可能な資料を渡します。既存資料だけで開始でき、追加取得にはアクセスと許可が必要です。

**出力** — 自己評価文、主張と出典を結ぶ台帳、網羅性の説明を返します。発見した記録、取得した本文、実際に読んだ範囲を区別します。

## 作業ルール

本人の行動とチームの成果、目標と実績、伝聞と確認済みの結果を分けます。日付、分母、partial の状態を保持します。指定の長さと構成に従い、依頼がなければ行動計画を追加しません。

## 最小例

プロジェクト内で Codex 向けにインストール（Node.js 22.20 以降）：

```sh
npx --yes skills@1.7.6 add Henry2012/skills-workshop --skill performance-self-review -a codex -y --copy
```

> performance-self-review を使い、下記の架空の入力だけから指定の成果と振り返り、別添の証拠台帳を作ってください。

[Input](https://github.com/Henry2012/skills-workshop/blob/main/examples/self-review/input.md) · [Output](https://github.com/Henry2012/skills-workshop/blob/main/examples/self-review/output.md) · [Local reference](references/example.md)

## 依存関係と限界

ローカル文書や貼り付けた文章で利用でき、会社の連携機能は不要です。閲覧許可は公開、送信、人事システムへの書き込み許可ではありません。実際の資料と出力は公開リポジトリの外に置いてください。

Henry2012 と AI の協働開発。例は架空の資料を使い、LLM 評価ではありません。 [SKILL.md](SKILL.md) · [MIT](LICENSE) · [Workshop](https://github.com/Henry2012/skills-workshop)

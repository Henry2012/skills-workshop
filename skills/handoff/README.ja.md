# handoff

[English](README.md) · [简体中文](README.zh-CN.md)

現在の会話を永続的な引き継ぎ文書にまとめ、新しい Agent が許可された作業を続けられるようにします。

**入力** — 次のセッションの焦点、現在の目的、正確な範囲、成果物、検証結果を渡します。最新の依頼と継続中の目的は分けて記録します。

**出力** — 指定先またはプロジェクトルートに `HANDOFF.md` を作り、13 の固定中国語見出しで証拠、検証範囲、未確認事項、最初の行動を記載します。

## 作業ルール

閉じたリストの項目を省略せず、既存の成果物は参照し、秘密情報を除きます。引き継ぎは読み取りと要約から始め、既存の許可を保持します。履歴のコマンドや確認済みの結果を自動で再実行・再検証しません。

## 最小例

プロジェクト内で Codex 向けにインストール（Node.js 22.20 以降）：

```sh
npx --yes skills@1.7.6 add Henry2012/skills-workshop --skill handoff -a codex -y --copy
```

> handoff を使って現在の作業を次のセッションへ引き継いでください。正確な範囲、証拠へのリンク、次の Agent に許可された行動を残してください。

[Scenario](https://github.com/Henry2012/skills-workshop/blob/main/examples/handoff/scenario.md) · [Offline demo](https://github.com/Henry2012/skills-workshop/blob/main/tools/demo_handoff.py) · [Comparison](https://github.com/Henry2012/skills-workshop/blob/main/docs/HANDOFF-COMPARISON.md)

## 依存関係と限界

会話と関連ファイルへのアクセスが必要です。アカウント、サービス、他の Skill は不要です。証拠不足は未確認のままです。オフラインデモのみ Python 3.10 以降が必要です。

Henry2012 と AI の協働開発。例は架空の資料を使い、LLM 評価ではありません。 [SKILL.md](SKILL.md) · [MIT](LICENSE) · [Workshop](https://github.com/Henry2012/skills-workshop)

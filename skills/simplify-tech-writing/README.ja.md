# simplify-tech-writing

[English](README.md) · [简体中文](README.zh-CN.md)

中国語・英語の技術文を、必要な情報を保ったまま読みやすく書き直します。

**入力** — 原文、必要な文脈、読者、形式を渡し、書き直しと曖昧さのレビューのどちらを求めるか指定します。

**出力** — 同じ意味の明快な文章を返します。レビューでは具体的な曖昧さと修正案を示します。不足する文脈で意味や結果が変わる場合だけ質問します。

## 作業ルール

条件、否定、主体、順序、数値、単位、識別子、不確実性を保持します。HTTP 200 を復旧済みに変えず、自動動作を手動操作にせず、不明な主体を作りません。コマンドの編集は実行許可ではありません。

## 最小例

プロジェクト内で Codex 向けにインストール（Node.js 22.20 以降）：

```sh
npx --yes skills@1.7.6 add Henry2012/skills-workshop --skill simplify-tech-writing -a codex -y --copy
```

> simplify-tech-writing で次の英文を明確にし、全事実を保って英文の書き直しだけを返してください: The export request failed at 10:00. One retry returned HTTP 200 at 10:02; the final export status was not checked.

[11 original cases](references/examples.md) · [Methods](references/methods.md) · [Sources](references/sources.md)

## 依存関係と限界

通常の編集に PDF、ネットワーク、アカウント、他の Skill は不要です。ASD-STE100 に着想を得た編集方法であり、適合性検査ではありません。規格と辞書は同梱しません。正確な照会には利用権限のある資料が必要で、日本語の編集能力は未評価です。

Henry2012 と AI の協働開発。例は架空の資料を使い、LLM 評価ではありません。 [SKILL.md](SKILL.md) · [MIT](LICENSE) · [Workshop](https://github.com/Henry2012/skills-workshop)

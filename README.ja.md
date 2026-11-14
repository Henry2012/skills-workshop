# Skills Workshop

**「完了」の意味を、はっきりさせる。**

[English](README.md) · [简体中文](README.zh-CN.md)

Henry2012 です。Agent との作業で判断が曖昧になりやすい場面を Skill にしています。新しい会話への移行、設計の実装準備度の判断、技術的な結果の説明、自分の貢献の整理です。

テストが通っただけなのに「公開済み」になる。「通常」が推敲で「必ず」に変わる。新しい会話では、直前に決めたことが失われる。これらの Skill は、そうした場面を扱う具体的なルールを与えます。

必要なものを選び、読んで、変えて、役立つ部分を使ってください。それぞれ Markdown の指示と参照資料を含むディレクトリで、4 つの Skill は個別に利用できます。

## 使い始める

**Node.js 22.20 以降**と npm/npx が必要です。利用するプロジェクトのディレクトリで実行します。Vercel の [skills CLI](https://github.com/vercel-labs/skills) を、今回検証したバージョンに固定しています。

**Codex 向けに 4 つすべて**をインストール：

```sh
npx --yes skills@1.7.6 add Henry2012/skills-workshop --skill '*' -a codex -y --copy
```

**設計レビューだけ**をインストール：

```sh
npx --yes skills@1.7.6 add Henry2012/skills-workshop --skill review-plans -a codex -y --copy
```

**Claude Code** では `-a codex` を `-a claude-code` に置き換えます。`'*'` の引用符は残してください。現在のプロジェクトに確認なしでインストールし、同名の既存 Skill を置き換える可能性があります。変更済みの内容を先に確認してください。グローバルインストールは指定していません。

インストール後、Agent に依頼します。

> review-plans と必須 rubric を使い、この設計が実装に進めるか読み取り専用でレビューしてください。

`--copy` を明示し、Codex では `.agents/skills/`、Claude Code では `.claude/skills/` にファイルをコピーします。ファイルの配置後、Agent 側の Skill 検出を更新する必要がある場合があります。[インストール検証と限界](docs/INSTALLATION.md)を参照してください。

例の確認やリポジトリのチェックには、別途クローンします。

```sh
git clone https://github.com/Henry2012/skills-workshop.git
cd skills-workshop
```

`examples/design-review/design.md` をレビューさせ、[参照出力](examples/design-review/review.md)と比較します。「成功」の矛盾と両方の根拠を示せるか確認してください。

## この Skill を作る理由

### 会話が変わるたびに、説明をやり直したくない

引き継ぐべきなのは、今も有効な判断です。目的、正確な範囲、確認できたこと、未確認事項、次の Agent に許可されている行動を残します。

[`handoff`](skills/handoff/README.ja.md) は「現在の目的」と「最新の依頼」を分け、完了の主張に証拠を添えます。次のセッションは読み取りと要約から始め、既存の許可の範囲で続行します。履歴のコマンドを自動的に再実行指示として扱いません。

[オフラインの引き継ぎ例を試す](skills/handoff/README.ja.md)。

### 整った文書でも、実装できる設計とは限らない

ある節では、ジョブがキューに入れば成功。別の節では、結果ファイルができて初めて成功。どちらも実装できますが、両方を同時には満たせません。

[`review-plans`](skills/review-plans/README.ja.md) は、技術計画、製品リリース計画、業務手順の完全性、明確さ、実行可能性と次の工程への準備状況を、証拠に基づく 8 つの問いで確認します。

| | 問い |
|---|---|
| Q1 | 必要な内容が欠けていないか？ |
| Q2 | 理由のない重複がないか？ |
| Q3 | 各部分は整合しているか？ |
| Q4 | 事実と推論は成り立つか？ |
| Q5 | 読み手によって解釈が変わらないか？ |
| Q6 | 現実の制約の中で実現できるか？ |
| Q7 | 成功をどう確かめるか？ |
| Q8 | 失敗したらどうするか？ |

問いが確認するのは、目的、主張、行動、制約、結果という計画の共通構造です。API 設計、製品公開、業務手順でも使えます。**共通なのは問いであり、必要な証拠と合格基準は分野ごとに変わります。**初期案とデプロイ手順書に同じ詳細さを求めることもありません。

根本原因 1 つにつき指摘は 1 件にまとめ、判断を証拠に結び付け、不足する資料を明示します。レビュー時は Skill を明示的に選択してください。[分野をまたぐ適用例と限界](skills/review-plans/README.ja.md)も参照できます。

### 読みやすさのために、大事な情報を失いたくない

「再試行で HTTP 200 が返った」は「復旧した」と短くできます。しかし、それでは別の主張になります。

[`simplify-tech-writing`](skills/simplify-tech-writing/README.ja.md) は中国語・英語の技術文を編集し、条件、否定、順序、数値、識別子、不確実性を保持します。原文に接続を閉じた主体が書かれていなければ、書き直す際にも作り上げません。

[11 の独自の書き直し例](skills/simplify-tech-writing/references/examples.md)を試してください。条件を 1 つ変え、それが新しい表現にも残っているか確認できます。

### チームの成果から、個人の貢献を分けて考える

自分が受け入れ基準を定義し、同僚が修正を実装し、チームがローカルテストに合格した。関連する出来事ですが、担当と意味は異なります。

[`performance-self-review`](skills/performance-self-review/README.ja.md) は自己評価の文章を書く前に証拠台帳を作ります。本人の行動とチームの納品、目標と実績、伝聞の数値と独立した確認を区別します。

[架空の入力](examples/self-review/input.md)を使い、[参照出力](examples/self-review/output.md)と比較してください。実際の仕事の記録は、この公開リポジトリの外で管理します。

## Skill 一覧

| やりたいこと | Skill | 用意するもの |
|---|---|---|
| 新しいセッションで仕事を続ける | [handoff](skills/handoff/README.ja.md) | 会話、現在の指示、成果物 |
| 計画を次の工程へ進められるか判断する | [review-plans](skills/review-plans/README.ja.md) | 設計、判断対象、関連する証拠 |
| 技術的な内容を明確に説明する | [simplify-tech-writing](skills/simplify-tech-writing/README.ja.md) | 原文、文脈、読者 |
| 自分の貢献を正確に説明する | [performance-self-review](skills/performance-self-review/README.ja.md) | 評価期間、役割、利用権限のある資料 |

組み合わせて利用できますが、自動接続済みのパイプラインではありません。レビュー結果は実行許可にならず、コマンドの文章を編集することは実行を意味しません。

## 確認・変更・貢献

例はすべて架空の資料を使っています。Python 3.10 以降で、リンク、実行用ファイルのハッシュ、例の一部の要件を確認できます。

```sh
python3 tools/check.py
```

このチェックは LLM を呼び出さず、モデルの精度を証明しません。[検証範囲](docs/VALIDATION.md)に確認済み・未検証の内容を記載しています。紹介文は英語・中国語・日本語です。実行時の指示は元の英語・中国語と固定ラベルを保持し、`handoff` の固定見出しは中国語です。

私は AI と協働し、課題、制約、受け入れ基準を定め、利用を通じて改善しています。技術文書の Skill は ASD-STE100 からの着想を明記し、規格自体は配布しません。[出典](docs/PROVENANCE.md)には帰属とライセンス範囲、[選定理由](docs/SELECTION.md)には公開対象から外した内容を記載しています。

ルールがうまく働かなければ、問題を再現する小さな架空の例を提示してください。何を変更し、何を保持すべきかも説明してください。[貢献方法](CONTRIBUTING.md)を読み、非公開資料や認証情報を Issue や PR に含めないでください。

この紹介文の問題から始める構成は、[Matt Pocock の Skills リポジトリ](https://github.com/mattpocock/skills)を参考にしています。ここにある Skill と例は本プロジェクトで開発したものです。

[MIT](LICENSE) · [保守](docs/MAINTENANCE.md) · [更新履歴](CHANGELOG.md)

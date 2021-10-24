# Clean Architectureサンプル

Clean ArchitectureをベースとしたAPIサーバのサンプル。
APIサーバの実装にはPython + FastAPIを利用している。

## 目的

- Clean Architectureの4層構成をAPIサーバに適用した場合の実装例を示すこと
- Clean Architectureで作った場合のテストコード実装を示すこと

## アプリケーション

目的を実現するために下記のような機能を持ったサービスを作る。

- オリジナルのプレイリストを作成・管理する
- プレイリストを作るための補助機能として、iTunesなどの音楽サービスから情報を取得することができる

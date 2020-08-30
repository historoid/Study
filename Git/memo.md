# GitとGitHubの使い方メモ

## GitHubにアカウント登録を済ましておく。

git config --global user.name "username"
git config --global user.email user@address.com

## 新規プロジェクトをはじめる

git init

## 基本的なワークフロー

1. ファイルの変更をステージングエリアへ追加する
1. ローカルリポジトリにコミットする
1. リモートリポジトリにプッシュする

はじめにローカルで `git init` して、`.git` フォルダ（隠しフォルダ）をつくる。  
そのあとに、GitHub上で新しいリポジトリ（既存でも可）を作っておく。  
InitializeでReadMe.mdを作らない設定で先に進むと、コマンドが表示される。

`git remote add origin git@github.com:historoid/Res.git`
`git branch -M master` <- error: refname refs/heads/master not found
`git push -u origin master`

ローカル上で、`git commit`まで終わらせて上記のコマンドを実行していく。  
下記のコマンドはUdemyでの例  
`git remote add origin https://xxxxxxxxx.git` でローカルリポジトリと、作成したGitHub上のリポジトリがつながる。

ローカルではファイルの編集後、`git add hoge.txt`して`git commit`  
そのとき、Vimが開くのでコメント追記。

その後に`git remote ...`を実行。

## ステージングエリアへ追加
`git add filename.txt`
`git add .` <- すべての変更ファイルをSAへ追加

## リポジトリへコミット
`git commit`
`git commit -v` で変更内容を表示
1. 変更内容の要約
1. 空行
1. 変更した理由（Why)

## リポジトリの状態を確認する
`git status`



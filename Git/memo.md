# GitとGitHubの使い方メモ

## GitHubにアカウント登録を済ましておく。

`git config --global user.name "username"`  
`git config --global user.email user@address.com`  

## 新規プロジェクトをはじめる

`git init`

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
`git add .` <- すべての変更ファイルをステージングエリアへ追加

## リポジトリへコミット

リポジトリへ変更を記録

`git commit`  
`git commit -v` で変更内容を表示  

1. 変更内容の要約
1. 空行
1. 変更した理由（Why)

## リポジトリの状態を確認する

`git status`  

## ファイルの削除を反映

`git rm filename.txt`  

## 複数ファイルの変更
`git add .`  

## 変更履歴を確認する

`git log`  
`git log -n 3` 最新コミット3つまで表示  

リポジトリにコミットされたログを確認することができる。  
コミットのハッシュ値等が表示される。ハッシュ値でそこへ戻ることができたりする。

`git log --oneline` 一行で表示する
`git log -p filename.txt` そのファイルの差分を見る。ファイル名を指定しないとブランチ全体での差分を見る。

## ファイルの変更差分を確認する
`git diff` ステージとの差分
`git diff HEAD` ステージとコミットとの差分

## GitHubにPushする
まずはリモートリポジトリを登録しておく
`git remote add`  
`git remote add origin https://github.com/user/repo.git`

ローカルの内容をリモートへ送る
`git push origin repo_name`  

## Gitでの管理から外す
.gitignoreファイルに指定する。  
例えば自動生成されるファイルやパスワードが記載されているファイルを無視したい。  

`#` でコメント  
ファイル名を書くだけでOK

コミットしてしまったら、`git rm filename`  
`git rm -r directory`でもOK

`git rm --cached filename` でもよいが、管理からは外れないのでgitignoreファイルに追加しておくこと。

## gitignore

`filename.php` <- ディレクトリを問わず、その名前のファイルを除外

`/filename.php` <- gitignoreファイルと同じ階層のphpファイルを除外





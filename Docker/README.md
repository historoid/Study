# Dockerの学習

コンテナはDocker imageからつくられる。  
Docker imageは、Docker fileから作られる。

## bash
環境変数の設定： `export AGE=20`  
環境変数の表示： `echo $AGE`  
`pwd`： print working directory

## DockerHubからコンテナをダウンロード
`docker pull image_name`

## Docker imageの確認
`docker images`

## コンテナの作成
`docker run <image_name>`  

1. run
1. create
1. execute

hello-worldのイメージだと、`docker run`したときに自動的にテキストが表示されるように設計されている。  
実際のコンテナも同じで、あるプログラムを実行したらコンテナは`exit`されるものも多い。  
その指定は、DockerImageに書かれている。

## アクティブなコンテナの確認
`docker ps`

## コンテナを起動してbashを表示
`docker run -it <image_name> bash`  
 `run`したときにbashを起動する。
 
## コンテナからDocker imageをつくる
自分でコンテナの中身を変えたら、新しいDocker imageを作る。  
新しいDocker imageをメンバーに配れば良い。  
`docker commit <container_id> <image_name>`

## ExitedからUpへ
`docker restart <container_id>`

## DockerHubに自分のリポジトリを作る
UbuntuはUbuntuでも、バージョンが違うものはタグ名で管理する。  
タグが省略されているときは、latestになる。

`repository_name:latest`などが例。  
自分のリポジトリなら、`historoid/my-first-repo:latest`となる。

1つのイメージで1つのリポジトリを作る。

## イメージ名の変更
`docker tag image-name new-name` 
イメージ名を変えても、参照先のイメージ自体は変わらない（容量少なくて済む）

現在使っているイメージをプッシュするように名前をつける。  
`docker tag ubuntu:latest historoid/my-first-repo:latest`

公的な（会社の）DockerHubにアップする場合  
`docker push registry-1.docker.io/library/ubuntu:latest`  
`docker push hostname:port/username/repo:tag`となっている。

docker image名は、dockerhubのリポジトリ名と一致していなくてはならない。  

## imageのpush
dockerhubには、自分で追加したレイヤーのみがアップされる。 
すでにあるレイヤーは共有されている。

## imageの削除
`docker rmi image_name`

## imageのpull
`docker pull image_name`

## docker run は何をしているのか
`docker run` = `docker create` + `docker start`  
つまりコンテナを作って、起動している。  
`docker start`ではデフォルトコマンドが実行されている。  
hello-worldのイメージでは、hello worldが表示されるだけ。  
その後は、`exited`になる。

## デフォルトコマンドの結果を見る
`docker start -a`  
これで出力結果が見られる。

## デフォルトコマンド
`docker ps -a`で見ることのできるCOMMANDのところが、デフォルトコマンドである。  
`jupyter lab --ip....`がデフォルトコマンドになっているときは、jupyterlabが起動している。

## AWS






















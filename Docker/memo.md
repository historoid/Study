# Dockerの学習

コンテナはDocker imageからつくられる。  
Docker imageは、Docker fileから作られる。

# bash
環境変数の設定： 'export AGE=20'  
環境変数の表示： 'echo $AGE'  
'pwd'： print working directory

# DockerHubからコンテナをダウンロード
'docker pull image_name'

# Docker imageの確認
'docker images'

# コンテナの作成
'docker run image_name'  

1. run
1. create
1. execute

hello-worldのイメージだと、'docker run'したときに自動的にテキストが表示されるように設計されている。  
実際のコンテナも同じで、あるプログラムを実行したらコンテナは'exit'されるものも多い。  
その指定は、DockerImageに書かれている。

# アクティブなコンテナの確認
'docker ps'

# コンテナを起動してbashを表示
'docker run -it image_name bash'  
 'run'したときにbashを起動する。
 
 

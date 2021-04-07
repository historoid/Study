# 4-1
# ファイルの中身を確認する
%cat ./s288c_n20.gff

# 4-2
path = './s288c_n20.gff'
with open(path) as f: # ファイルオープン
    line = f.readline() # 1行読み込み
    print(line) # 出力

# 4-3
with open(path) as f:
    for line in f: # 1行ずつ読み込み
        print(line) # 出力

# 4-4
with open(path) as f:
    for line in f:
        line = line.rstrip() # 改行コードの削除
        print(line)

# 4-5
with open(path) as f:
    for line in f:
        line = line.rstrip()
        if line.startswith('#'): # #で始まるかどうか
            print(line)

# 4-6
with open(path) as f:
    for line in f:
        line = line.rstrip()
        if line.startswith('#'): # #で始まるかどうか
            continue
        print(line)

# 4-7
with open(path) as f:
    for line in f:
        line = line.rstrip()
        if line.startswith('#'):
            continue
        s = line.split('\t') # タブで区切る
        print(s[8]) # 9列目を出力

# 4-8        
with open(path) as f:
    for line in f:
        line = line.rstrip()
        if line.startswith('#'):
            continue
        s = line.split('\t')
        items = s[8].split(';') # 9列目を";"で区切る
        for item in items: # リストを1つずつ
            print(item) # 出力

# 4-9
with open(path) as f:
    for line in f:
        line = line.rstrip()
        if line.startswith('#'):
            continue
        s = line.split('\t')
        items = s[8].split(';')
        for item in items:
            if item.startswith('product='):
                print(item)

# 4-10
with open(path) as f:
    for line in f:
        line = line.rstrip()
        if line.startswith('#'):
            continue
        s = line.split('\t')
        items = s[8].split(';')
        tags = dict([tmp.split('=') for tmp in items]) # リスト内包表記で一括取得
        print(tags)

# 4-11
with open(path) as f:
    for line in f:
        line = line.rstrip()
        if line.startswith('#'):
            continue
        s = line.split('\t')
        items = s[8].split(';')
        tags = dict([tmp.split('=') for tmp in items])
        if 'Note' in tags: # Noteタグの有無
            print(tags['Note']) # Noteの内容を出力

# 4-12
import urllib.parse # urllib.parseモジュールをインポート
with open(path) as f:
    for line in f:
        line = line.rstrip()
        if line.startswith('#'):
            continue
        s = line.split('\t')
        items = s[8].split(';')
        tags = dict([tmp.split('=') for tmp in items])
        if 'Note' in tags:
            print(urllib.parse.unquote(tags['Note'])) # Noteの内容をデコードして出力

# 4-13
with open(path) as f:
    f.readline() # 1行目の読み込みを実行
    f.readline() # 2行目の読み込みを実行
    for line in f: # 3行目からの読み込みを実行
        line = line.rstrip()
        print(line)

# 4-14
output = './output/test1.txt' # ファイル名
out = 'Hello world!\n' # 出力
with open(output, 'w') as f: # ファイルオープン
    f.write(out) # ファイルへ書き込み

# 4-15
output = './output/test1.txt' # ファイル名
out = 'Hello world!\n' # 出力
with open(output, 'x') as f: # ファイルオープン
    f.write(out) # ファイルへ書き込み

# 4-16
!head -n 25 ./SRR453566.sam

# 4-17
path = './SRR453566.sam'
dic = {}
with open(path) as f:
    for line in f:
        line = line.rstrip()
        if line.startswith('@'): # ヘッダー行をスキップ
            continue
        s = line.split('\t') # タブで区切る
        FLG = s[1] # 2列目を格納
        if FLG in dic: # 辞書に格納
            dic[FLG] += 1
        else:
            dic[FLG] = 1
# 出力 FLAG, 総数
for k, v in dic.items():
    print(k + '\t' + str(v))

# 4-18
readList = []
with open(path) as f:
    for line in f:
        line = line.rstrip()
        if line.startswith('@'):
            continue
        s = line.split('\t')
        FLG = int(s[1])
        if FLG & 0x4:
            readList.append(s[0])
# 出力
for item in readList:
print(item)

# 4-19
path = './SRR453566.sam'
TATA1 = 'TATAAAAG'
TATA2 = 'TATAAAAA'
TATA3 = 'TATATAAG'
TATA4 = 'TATATAAA'
with open(path) as f:
    for line in f:
        line = line.rstrip()
        if line.startswith('@'): # ヘッダー行をスキップ
            continue
        s = line.split('\t') # タブで区切る
        sequence = s[9] # 10列目を格納
        if TATA1 in sequence:
            print('TATA1:' + sequence)
        if TATA2 in sequence:
            print('TATA2:' + sequence)
        if TATA3 in sequence:
            print('TATA3:' + sequence)
        if TATA4 in sequence:
            print('TATA4:' + sequence)

# 4-20
import re
TATA = re.compile('TATA[AT]AA[GA]') # patternをコンパイル
with open(path) as f:
    for line in f:
        line = line.rstrip()
        if line.startswith('@'): # ヘッダー行をスキップ
            continue
        s = line.split('\t') # タブで区切る
        sequence = s[9] # 10列目を格納
        m = TATA.search(sequence) # patternを検索
        if m:
            print(sequence)

# 4-21
TATA = re.compile('TATA[AT]AA[GA]') # patternをコンパイル
with open(path) as f:
    for line in f:
        line = line.rstrip()
        if line.startswith('@'): # ヘッダー行をスキップ
            continue
        s = line.split('\t') # タブで区切る
        sequence = s[9] # 10列目を格納
        m = TATA.search(sequence) # patternを検索
        if m:
            # 一致した箇所を出力
            print(m.start(), m.end(), m.string[m.start():m.end()])

# 4-22
TATA = re.compile('TATA[AT]AA[GA]') # patternをコンパイル
TATA_rev = re.compile('[CT]TT[AT]TATA') # 相補鎖patternをコンパイル
with open(input) as f:
    for line in f:
        line = line.rstrip()
        if line.startswith('@'): # ヘッダー行をスキップ
            continue
        s = line.split('\t') # タブで区切る
        sequence = s[9] # 10列目を格納
        m = TATA.search(sequence) # patternを検索
        if m:
            print(m.start(), m.end(), m.string[m.start():m.end()])
        m = TATA_rev.search(sequence) # 相補鎖patternを検索
        if m:
            print(m.start(), m.end(), m.string[m.start():m.end()])

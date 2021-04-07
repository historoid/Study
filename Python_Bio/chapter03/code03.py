# 3-1
abs(-7)

# 3-2
abs(7)

# 3-3
test_str = 'Hello Bio!'
print(test_str)

# 3-4
test_str

# 3-5
import numpy as np
array1 = np.array([[0, 1], [2, 3]]) # 実行しても画面に表示は出てきません

# 3-6
print(array1)

# 3-7
array1

# 3-8
val_a=1
val_b=2
val_a
val_b

# 3-9
print(val_a)
print(val_b)

# 3-10
'Hello Bio'.upper()

# 3-11
'Hello Bio'.upper().replace('BIO', 'INFO')

# 3-12
val_int = 1
val_int

# 3-13
val_float = 1.1
val_float

# 3-14
val_str = 'atgc'
val_str

# 3-15
type(val_int) # 1はint（整数）型です

# 3-16
type(val_float) # 1.1はfloat（浮動小数点）型です

# 3-17
type(val_str) # 'atgc'はstr（文字列）型です

# 3-18
type(1)

# 3-19
type(1.1)

# 3-20
type('atgc')

# 3-21
num_int = 100 # int型の100です
num_str = '100' # 文字列型としての100です

# 3-22
num_int

# 3-23
num_str

# 3-24
num_int + 1

# 3-25
num_str + 1

# 3-26
val_add = val_int + val_float # int型の1と，float型の1.1を加算します
val_add

# 3-27
type(val_add)

# 3-28
num_str + '1' # 文字列型としての変数num_str(='100')と，'1'を+しています

# 3-29
'atgc' + 'ATGC'

# 3-30
int(num_str) # num_strは「文字列としての100」でした

# 3-31
int(num_str) + 1

# 3-32
list1 = [0, 3, 5, 7, 9, 11]
list1

# 3-33
type(list1)

# 3-34
list2 = []
list2

# 3-35
list3 = ['chr1', 1358, 2358]
list3

# 3-36
list4 = [1, 3, list3]
list4

# 3-37
list1 # 中身を確認します

# 3-38
list1[0] # 0から数えるので先頭の値，0になります

# 3-39
list1[1] # 2番目の値なので0, 3…の3となります

# 3-40
list1[-1] # list1の最後の値となります（“-0”ではありません）

# 3-41
list1[-2] # list1の後ろから2番目の値となります

# 3-42
list2 # list2は空リストでした

# 3-43
list2[0] # list2にはインデックス0の値，すなわち「1番目の値」はありません

# 3-44
list1[10000] # list1のインデックス10000，すなわち「10,001番目の値」も当然ありません

# 3-45
len(list1)

# 3-46
len(list2)

# 3-47
list_num = [0, 1, 2, 3, 4, 5, 6, 7, 8]
list_num

# 3-48
list_num[1:] # list_num[1]から最後まで

# 3-49
list_num[:4] # ゼロからlist_num[4]の1つ前まで

# 3-50
list_num[1:4]

# 3-51
list_num[0:5:2] # ゼロ以上5未満の数列で，2つおきの値

# 3-52
list_num[::-1]

# 3-53
list3 # 先ほど作ったリストです

# 3-54
list5 = ['atgc', 1]

# 3-55
list5

# 3-56
list6 = list3 + list5
list6

# 3-57
list1

# 3-58
list1[3] # インデックス3の値は7でした

# 3-59
list1[3] = 'edited' # インデックス3の値を文字列'edited'に書き換えます
list1[3] # 確認してみます

# 3-60
list1 # 全体を確認してみます

# 3-61
list1

# 3-62
list1.append('append_data') # 'append_data'をリストの末尾に追加します

# 3-63
list1

# 3-64
list1 = [0, 3, 5, 'edited', 9, 11, 'append_data']
list1.append(11)
list1

# 3-65
list1.remove(11)
list1

# 3-66
list7 = [1, 5, 2, 3, 8, 4, 7, 6]
list8 = sorted(list7)
list8

# 3-67
list7

# 3-68
list9 = sorted(list7, reverse=True)

# 3-69
list9

# 3-70
list10 = sorted(list9, reverse=False)
list10

# 3-71
list11 = [-3, 1, -5, 4, 2, -6]
list_abs = sorted(list11, key=abs) # 絶対値でソート
list_abs

# 3-72
list12 = ['shizuoka', 'tokyo', 'mie', 'hokkaido', 'osaka']
list_len = sorted(list12, key=len, reverse=True) # 文字列の長さで降順でソート
list_len

# 3-73
def get_gene_num(x):
    gene_num = x.split('_')[-1]
    return int(gene_num)

# 3-74
get_gene_num('gene_1') # 試しに関数に文字列'gene_1'を入れて実行してみます

# 3-75
list11 = ['gene_3', 'gene_1', 'gene_10', 'gene_25', 'gene_21', 'gene_19',
          'gene_2', 'gene_29', 'gene_30', 'gene_11']
list11

# 3-76
sorted(list11)

# 3-77
sorted(list11, key=get_gene_num)

# 3-78
sorted(list11, key=lambda x: int(x.split('_')[-1]))

# 3-79
list_sort_test = [0, 5, 3, 4, 2]
list_sort_test

# 3-80
sorted(list_sort_test)

# 3-81
list_sort_test

# 3-82
list_sort_test.sort() # 特に何も出力はされません

# 3-83
list_sort_test

# 3-84
tuple1 = ('gene1', 'chr8', 1, 2, 3)
tuple1

# 3-85
tuple1[0]

# 3-86
tuple1[3]

# 3-87
tuple1[0:1]

# 3-88
tuple1[0:3]

# 3-89
tuple2 = (1, 2, [3, 4], (5, 6))
tuple2

# 3-90
tuple1[0] = 'gene2'

# 3-91
tuple1.append('4')

# 3-92
tuple1

# 3-93
list_from_tuple1 = list(tuple1)
list_from_tuple1

# 3-94
tuple(list_from_tuple1)

# 3-95
DNA_seq1 = 'atgcatgcatgc'
DNA_seq1

# 3-96
DNA_seq1[3:6]

# 3-97
test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
test_str = '012345678'

# 3-98
test_list[3:6]

# 3-99
test_str[3:6]

# 3-100
test_list[6] = 'a'
test_list

# 3-101
test_str[6] = 'a'

# 3-102
test_str[:6] + 'a' + test_str[7:]

# 3-103
list_from_test_str = list(test_str)
list_from_test_str

# 3-104
list_from_test_str[6] = 'a'
''.join(list_from_test_str)

# 3-105
gene_set1 = {'chr': 1, 'pos': 324, 'ref': 'c' , 'var': 't'}

# 3-106
gene_set1

# 3-107
gene_set1['chr']

# 3-108
set1 = {'gene_1', 'gene_3', 'gene_8'}

# 3-109
set1 # 出力は環境により順序が異なります

# 3-110
set2 = {2, 1, 3}

# 3-111
set2 # これも，出力の順序は環境により異なります

# 3-112
set1

# 3-113
set1.add(12)
set1

# 3-114
set1.remove('gene_1')
set1

# 3-115
set3 = {1, 2, 3, 4, 5}
set4 = {3, 4, 5, 6, 7}
set3 | set4 # 和

# 3-116
set3 & set4 # 積（共通部分）

# 3-117
set3 - set4 # 差

# 3-118
set3 ^ set4 # 対称差（どちらか一方にのみある値）

# 3-119
list_s = [1, 2, 3]
tupple_s = (4, 5, 6)

# 3-120
set(list_s)

# 3-121
set(tupple_s)

# 3-122
list_s2 = [1, 1, 2, 3, 4, 5]
list_s2

# 3-123
set(list_s2)

# 3-124
val_a = 1
val_b = val_a

# 3-125
val_a

# 3-126
val_b

# 3-127
val_a = val_a + 1

# 3-128
val_a

# 3-129
val_b

# 3-130
id(val_a) # 値は環境により異なります

# 3-131
id(val_b) # 値は環境により異なります

# 3-132
list_a = [1, 2, 3]
list_b = list_a

# 3-133
list_a

# 3-134
list_b

# 3-135
list_a.append(4)

# 3-136
list_a

# 3-137
list_b

# 3-138
id(list_a)

# 3-139
id(list_b)

# 3-140
gene_set1 = {'chr': 1, 'pos': 324, 'ref': 'c', 'var': 't'}
if gene_set1['pos'] >= 300:
    print('above 300')

# 3-141
gene_set1 = {'chr': 1, 'pos': 324, 'ref': 'c', 'var': 't'}
if gene_set1['pos'] >= 300: # もし，posが300以上なら
    print('above 300')
elif gene_set1['pos'] >= 200: # さもなくば，もし200以上なら
    print('above 200')
else: # そのどれでもなかったら
    print('under 200')

# 3-142
x = 350
y = 250
if x >= 300 and y > 200:
    print('success')
elif x >= 300 or y > 200:
    print ('half success')

# 3-143
x = 150
y = 150
if not x >= 300 and not y >= 200:
    print('success')

# 3-144
for_iter = ['gene_01', 'gene_02', 'gene_03']
for gene in for_iter:
    print(gene, ' is tested')

# 3-145
for_iter = ('gene_01', 'gene_02', 'gene_03')
for gene in for_iter:
    print(gene, ' is tested')

# 3-146
for_iter = {'gene_01', 'gene_02', 'gene_03'}
for gene in for_iter:
    print(gene, ' is tested')

# 3-147
for_iter = 'atgcATGC'
for gene in for_iter:
    print(gene, ' is tested')

# 3-148
for_range = range(10)
for gene in for_range:
    print(gene, ' is tested')

# 3-149
check_number = 0
while check_number <= 8:
    print('check_number =', check_number)
    check_number = check_number + 1

# 3-150
list_test = [1, 9, 8, 4]
list_test

# 3-151
list_comp = [x * 2 for x in list_test] #「if 条件」部分は省略されています
list_comp

# 3-152
list_comp = [x * 2 for x in list_test if x != 8]

# 3-153
list_comp

# 3-154
def say_hello(x):
    print('hello,', x)

# 3-155
say_hello('Jannet')

# 3-156
def hello_and_time(name, time):
    print('hello ', name)
    print('clock:', time)

# 3-157
hello_and_time(name='Jannet', time=3)

# 3-158
hello_and_time(time=3, name='Jannet')

# 3-159
def check_name():
    return 'Jannet'
check_name() # 試しに実行してみます

# 3-160
print('hello ', check_name())

# 3-161
def check_name2():
    return 'Jannet', 'Andy'
x, y = check_name2()
print('hello ', x, ' and ', y)

# 3-162
def func_args(*args):
    print('args:', args) args[1]:
    print('args[1]:', args[1])
func_args(1, 2, 3, 4, 5)

# 3-163
def func_kwargs(**kwargs):
    print('kwargs:', kwargs)
    print('kwargs[a]:', kwargs['a'])
func_kwargs(a=1, b=2, c=3, d=4, e=5)

# 3-164
import datetime

# 3-165
print(datetime.datetime.now())

# 3-166
import test_module1 # '.py'は入れません

# 3-167
test_module1.say_hello_module('Sara')

# 3-168
import test_module1 as tes1

# 3-169
tes1.say_hello_module('John')

# 3-170
import numpy as np

# 3-171
from test_module1 import say_hello_module
say_hello_module('Aya')

# 3-172
from test_module1 import say_hello_module as say_h

# 3-173
say_h('Betty')

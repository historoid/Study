# A-1
import numpy as np

# A-2
# 普通のリスト
a_py = [1, 2, 3, 4, 5]
# numpy.ndarrayオブジェクトの生成
a = np.array([1, 2, 3, 4, 5])
print(type(a_py))
print(type(a))

# A-3
# 最初の要素．0番から
print(a[0])
# 最後の要素
print(a[-1])
# スライシング．1番から最後の1個手前まで
print(a[1:-1])
# 1個おき
print(a[::2])
# 逆順
print(a[::-1])

# A-4
# 配列の次元
print(a.ndim)
# 配列の形状
print(a.shape)
# 配列の要素数
print(a.size)

# A-5
# 最大値
print(a.max())
# 最小値
print(a.min())
# 平均値
print(a.mean())
# 配列の要素の和
print(a.sum())

# A-6
# ones()関数，zeros()関数どちらも，1や0で埋める長さを指定する
print(np.ones(5))
print(np.zeros(5))

# A-7
print(np.linspace(0.0, 1.0, 21))

# A-8
print(np.sin(np.linspace(0.0, np.pi/2, 21)))

# A-9
print(np.ones(5).astype(bool))
print(np.zeros(5).astype(bool))

# A-10
print(a % 2 == 0)

# A-11
print((a % 2 == 0).astype(int))

# A-12
print((a % 2 == 0).astype(int).sum())

# A-13
a.reshape(5, 1)

# A-14
a.reshape(-1, 1)

# A-15
a[:, np.newaxis]

# A-16
b = np.array([[1, 2, 3,],
              [4, 5, 6,]])

# A-17
print(np.arange(12))
b = np.arange(12).reshape(4, 3)
print(b)

# A-18
print(b.ndim)
print(b.shape)
print(b.size)

# A-19
b[0, 0]

# A-20
b[0, :]

# A-21
b[:, 1]

# A-22
b[1:-1, :]

# A-23
# bの1列目（ゼロ番目）の値を2で割ったときに1となるか否かの真偽値
rows_mask = b[:, 0] % 2 == 1
print(rows_mask)
# マスク配列をbの行方向に作用させる
print(b[rows_mask, :])

# A-24
print(b.T)
print(b.T.shape)

# A-25
print(b)
print('Max:', b.max())
print('Min:', b.min())
print('Mean:', b.mean())
print('Sum:', b.sum())

# A-26
print(b)
print('\nAxis=0')
print('\tMax:', b.max(axis=0))
print('\tMin:', b.min(axis=0))
print('\tMean:', b.mean(axis=0))
print('\tSum:', b.sum(axis=0))
print('Axis=1')
print('\tMax:', b.max(axis=1))
print('\tMin:', b.min(axis=1))
print('\tMean:', b.mean(axis=1))
print('\tSum:', b.sum(axis=1))

# A-27
print(b + 100)

# A-28
# bの形状ですべての要素が1の行列を作って，100をかけたものを足す
print(b + np.ones(b.shape) * 100)

# A-29
print(b / [10, 100, 1000])

# A-30
print(b / [10, 100, 1000, 10000])

# A-31
# reshape(-1, 1)で列ベクトルに変換する
col_vec = np.array([10, 100, 1000, 10000]).reshape(-1, 1)
print(col_vec)
print(b / col_vec)

# A-32
# 擬似乱数のシード
np.random.seed(seed=10)
# ポアソン分布からランダムな数を生成する関数
counts = np.random.poisson(lam=1.0, size=(16, 5))
print(counts)
print(counts.shape)

# A-33
# 行ごとに観測地点が並んでいるので，
# 観測地点ごとのカウントの和をとる場合，axisは1（横方向）
total = counts.sum(axis=1)
print(total)

# A-34
# 「総観測数がゼロではない」という真偽値の配列を作る
nonzero_mask = total != 0
print(nonzero_mask)
# この真偽値で行をマスキングすることで特定の行を除去できる
# 総観測数は再度計算する
counts = counts[nonzero_mask, :]
total = counts.sum(axis=1)
print(total)

# A-35
# 横方向に割り算するので，総観測数の配列を列ベクトルに変換してから割り算する．
counts / total.reshape(-1, 1)

# A-36
abundances = 100 * counts / total.reshape(-1, 1)
print(abundances)

# A-37
# abundancesの1列目について，numpy.argsort関数を適用し，
# [::-1]によって逆順にして，[:3]で頭から3番目までを取り出す
np.argsort(abundances[:, 0])[::-1][:3]

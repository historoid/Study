# B-1
import scanpy as sc
sc.settings.set_figure_params(dpi=200)
print(sc.__version__)

# B-2
import anndata
print(anndata.__version__)

# B-3
import os
datadir = './scRNAseq'
adata1 = sc.read_10x_mtx(os.path.join(datadir, 'T0_1A'))
adata2 = sc.read_10x_mtx(os.path.join(datadir, 'T2_3B'))
adata3 = sc.read_10x_mtx(os.path.join(datadir, 'T4_5C'))
adata4 = sc.read_10x_mtx(os.path.join(datadir, 'T6_7D'))
adata5 = sc.read_10x_mtx(os.path.join(datadir, 'T8_9E'))

# B-4
sample_labels = ['Days0-3', 'Days6-9', 'Days12-15', 'Days18-21', 'Days24-27']
adata = adata1.concatenate([adata2, adata3, adata4, adata5],
                           batch_categories=sample_labels)

# B-5
adata.X

# B-6
adata.obs

# B-7
adata.var

# B-8
import numpy as np
# numpy.matrix.A1関数で疎行列の足し算結果をnumpy.ndarrayオブジェクトに変換する
# 細胞ごとのカウント．発現量テーブル（X）の横方向の和
adata.obs['counts'] = adata.X.sum(axis=1).A1
# 検出遺伝子数
adata.obs['n_genes'] = (adata.X > 0.0).astype(int).sum(axis=1).A1
# ミトコンドリア遺伝子発現量割合
mito_genes = adata.var_names.str.startswith('MT-')
adata.obs['percent_mito'] = np.sum(adata[:, mito_genes].X, axis=1).A1\
                            / np.sum(adata.X, axis=1).A1
adata.obs

# B-9
sc.pl.violin(adata, ['counts', 'n_genes', 'percent_mito'],
             jitter=0.4, multi_panel=True)

# B-10
sc.pl.scatter(adata, x='counts', y='percent_mito')
sc.pl.scatter(adata, x='counts', y='n_genes')

# B-11
print(adata)

# B-12
# 縦に足し算した和がゼロではない遺伝子のみを抽出
adata = adata[:, adata.X.sum(axis=0).A1 != 0]
print(adata)

# B-13
min_genes = 500
max_genes = 4000
mito_threshold = 0.15
# min_genes以上，かつ，max_genes以下の細胞を抽出
adata = adata[(adata.obs.n_genes > min_genes) &
              (adata.obs.n_genes < max_genes), :]
# mito_threshold以下の細胞を抽出
adata = adata[adata.obs.percent_mito < mito_threshold, :]
print(adata)

# B-14
# 細胞ごとのカウントで，和が10,000（指数表記で1e4）になるように正規化
sc.pp.normalize_total(adata, target_sum=1e4)

# B-15
# 対数変換
adata = sc.pp.log1p(adata, copy=True)

# B-16
sc.pp.highly_variable_genes(adata, n_top_genes=2000)

# B-17
sc.pl.highly_variable_genes(adata)

# B-18
adata = adata[:, adata.var.highly_variable]
print(adata)

# B-19
adata = sc.pp.scale(adata, copy=True)

# B-20
sc.tl.pca(adata, svd_solver='arpack')

# B-21
sc.pl.pca(adata, color='batch')

# B-22
sc.pp.neighbors(adata, n_neighbors=30, use_rep='X', method='umap')

# B-23
sc.tl.umap(adata, min_dist=0.01)

# B-24
sc.pl.umap(adata, color='batch')

# B-25
sc.tl.leiden(adata)

# B-26
sc.pl.umap(adata, color='leiden')

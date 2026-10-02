import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# パラメータ
n = 20
p = 0.3

# x軸の値（成功回数 0〜n）
x = np.arange(0, n + 1)

# 確率質量関数 (PMF) の計算
# 「n回中x回成功する確率」をすべて計算
pmf = binom.pmf(x, n, p)

# グラフの描画
plt.figure(figsize=(8, 5))
plt.bar(x, pmf, color='skyblue', edgecolor='black', alpha=0.7)
plt.title(f'Binomial Distribution (n={n}, p={p})')
plt.xlabel('Number of Successes')
plt.ylabel('Probability')
plt.xticks(x)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
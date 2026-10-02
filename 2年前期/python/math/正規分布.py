import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# 1. パラメータの設定
mu = 0      # 平均 (Mean)
sigma = 1   # 標準偏差 (Standard Deviation)

# 2. 理論的な曲線の作成
# 平均から ±4σ の範囲を計算対象にする
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 100)
pdf = norm.pdf(x, mu, sigma)  # 確率密度関数 (PDF)

# 3. 乱数データの生成 (シミュレーション)
data = np.random.normal(mu, sigma, 1000)

# 4. 可視化
plt.figure(figsize=(10, 6))

# ヒストグラム（生成した乱数の分布）
plt.hist(data, bins=30, density=True, alpha=0.5, color='orange', label='Generated Data')

# 理論曲線（正規分布のベルカーブ）
plt.plot(x, pdf, color='blue', lw=2, label=f'Normal Distribution\n(μ={mu}, σ={sigma})')

plt.title('Normal Distribution (Gaussian Distribution)')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
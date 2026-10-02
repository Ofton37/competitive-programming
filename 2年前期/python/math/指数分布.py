import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

# 1. パラメータ設定
# 平均して「5単位時間」に1回起こる場合、scale = 5
lam = 0.2
scale = 1 / lam 

# 2. 理論的な曲線の作成
x = np.linspace(0, 20, 100)
pdf = expon.pdf(x, scale=scale)

# 3. 乱数データの生成 (シミュレーション)
data = np.random.exponential(scale, 1000)

# 4. 可視化
plt.figure(figsize=(10, 6))

# ヒストグラム
plt.hist(data, bins=30, density=True, alpha=0.5, color='salmon', label='Generated Data')

# 理論曲線
plt.plot(x, pdf, color='red', lw=2, label=f'Exponential Distribution\n(λ={lam}, scale={scale})')

plt.title('Exponential Distribution (Waiting Time)')
plt.xlabel('Time until next event')
plt.ylabel('Density')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# 1. パラメータ λ (lam) をランダムに設定 (例: 1.0 から 15.0 の間)
random_lambda = np.round(np.random.uniform(1.0, 15.0), 2)
print(f"設定されたランダムな λ: {random_lambda}")

# 2. データの生成
# 乱数生成（そのλに従う事象を1000回シミュレーション）
samples = np.random.poisson(random_lambda, 1000)

# 理論的な確率分布の計算用
x = np.arange(0, np.max(samples) + 1)
pmf = poisson.pmf(x, random_lambda)

# 3. 可視化
plt.figure(figsize=(10, 6))

# シミュレーション結果のヒストグラム
plt.hist(samples, bins=len(x), density=True, alpha=0.6, 
         color='lightgreen', edgecolor='white', label='Simulated Data')

# 理論的な確率質量関数 (PMF) のプロット
plt.stem(x, pmf, linefmt='g-', markerfmt='go', basefmt=' ', 
         label=f'Theoretical PMF (λ={random_lambda})')

plt.title(f'Poisson Distribution Simulation (λ = {random_lambda})')
plt.xlabel('Number of Events')
plt.ylabel('Probability')
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.show()
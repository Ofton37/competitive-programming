import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform

# 1. パラメータ設定 (範囲 [a, b])
a = 10  # 最小値
b = 50  # 最大値

# 2. 理論的な確率密度関数 (PDF) の作成
# scipyでは loc=開始地点, scale=幅(b-a) で指定
x = np.linspace(a - 5, b + 5, 500)
pdf = uniform.pdf(x, loc=a, scale=b-a)

# 3. 乱数データの生成 (1000個)
data = np.random.uniform(a, b, 1000)

# 4. 可視化
plt.figure(figsize=(10, 5))
plt.hist(data, bins=20, density=True, alpha=0.5, color='teal', label='Generated Data')
plt.plot(x, pdf, color='black', lw=2, label=f'Theoretical PDF\n(Range: {a}-{b})')

plt.title('Continuous Uniform Distribution')
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.show()
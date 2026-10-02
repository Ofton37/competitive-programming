import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform

# 1から6までの整数（サイコロ）を1000回振る
dice_rolls = np.random.randint(1, 7, 1000)

# 結果のカウント
values, counts = np.unique(dice_rolls, return_counts=True)

# 可視化
plt.figure(figsize=(8, 4))
plt.bar(values, counts/1000, color='skyblue', edgecolor='black')
plt.title('Discrete Uniform Distribution (Dice Rolls)')
plt.xlabel('Value')
plt.ylabel('Probability')
plt.xticks(values)
plt.show()
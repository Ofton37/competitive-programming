import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap

# ==========================================
# 1. パラメータ設定
# ==========================================
N = 100               # グリッドのサイズ (100x100)
PROB_GROW = 0.05      # 空き地に木が生える確率 (p)
PROB_LIGHTNING = 0.001 # 木が突然発火する確率 (f)
INTERVAL = 50         # 更新速度 (ミリ秒)

# 状態の定義
EMPTY = 0  # 空き地
TREE  = 1  # 木
FIRE  = 2  # 火

# 色の設定: [0:白, 1:緑, 2:赤]
cmap = ListedColormap(['#FFFFFF', '#228B22', '#FF4500'])

# ==========================================
# 2. 初期状態の生成
# ==========================================
# 最初はランダムに木を配置 (30%が木、70%が空き地)
grid = np.random.choice([EMPTY, TREE], N*N, p=[0.7, 0.3]).reshape(N, N)

fig, ax = plt.subplots(figsize=(7, 7))
img = ax.imshow(grid, cmap=cmap, interpolation='nearest', vmin=0, vmax=2)
ax.set_title("Forest Fire Model Simulation")
ax.axis('off')

# ==========================================
# 3. 更新関数の定義
# ==========================================
def update(frame):
    global grid
    new_grid = grid.copy()
    
    # 乱数の一括生成（高速化のため）
    random_vals = np.random.rand(N, N)
    
    for i in range(N):
        for j in range(N):
            state = grid[i, j]
            
            if state == FIRE:
                # ルール1: 燃えている木は次のステップで空き地になる
                new_grid[i, j] = EMPTY
                
            elif state == TREE:
                # ルール2: 隣接するマスに「火」があるか確認
                # スライスを使って周囲8マスを効率的に取得
                y_min, y_max = max(0, i-1), min(N, i+2)
                x_min, x_max = max(0, j-1), min(N, j+2)
                neighbors = grid[y_min:y_max, x_min:x_max]
                
                if FIRE in neighbors:
                    new_grid[i, j] = FIRE
                # ルール3: 稀に落雷で発火する
                elif random_vals[i, j] < PROB_LIGHTNING:
                    new_grid[i, j] = FIRE
                    
            elif state == EMPTY:
                # ルール4: 空き地に木が生える
                if random_vals[i, j] < PROB_GROW:
                    new_grid[i, j] = TREE

    img.set_data(new_grid)
    grid = new_grid
    return img,

# ==========================================
# 4. アニメーションの実行
# ==========================================
ani = animation.FuncAnimation(fig, update, frames=200, interval=INTERVAL, blit=True)
plt.show()
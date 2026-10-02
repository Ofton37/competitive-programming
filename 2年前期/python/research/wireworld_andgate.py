import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap

# --- 設定 ---
N_Y, N_X = 50, 80  # グリッドサイズ (縦, 横)
EMPTY, HEAD, TAIL, WIRE = 0, 1, 2, 3
cmap = ListedColormap(['#000000', '#0077ff', '#ff4500', '#ffd700'])

# --- グリッドの構築 ---
grid = np.zeros((N_Y, N_X), dtype=int)

# 1. 入力ワイヤー (AとB)
grid[20, 5:30] = WIRE  # 入力A
grid[30, 5:30] = WIRE  # 入力B

# 2. ANDゲートのコア構造
# 信号を干渉させるための特殊な形状
grid[23:28, 30] = WIRE
grid[20:23, 31:34] = WIRE
grid[28:31, 31:34] = WIRE
grid[23:28, 34] = WIRE
grid[25, 30:35] = WIRE # 中央のブリッジ

# 3. 出力ワイヤー
grid[25, 35:75] = WIRE

# 4. 初期信号 (AとBを同期して配置)
grid[20, 5] = HEAD; grid[20, 6] = TAIL
grid[30, 5] = HEAD; grid[30, 6] = TAIL

# 5. 信号の追加 (2回目、3回目のパルス)
grid[20, 15] = HEAD; grid[20, 16] = TAIL
grid[30, 15] = HEAD; grid[30, 16] = TAIL

# --- 描画準備 ---
fig, ax = plt.subplots(figsize=(12, 6))
img = ax.imshow(grid, cmap=cmap, vmin=0, vmax=3, interpolation='nearest')
ax.axis('off')
ax.set_title("Wireworld: AND Gate Simulation")

def update(frame):
    global grid
    new_grid = grid.copy()
    
    # 電子の頭をカウント (周囲8マス)
    head_mask = (grid == HEAD).astype(int)
    total_heads = (
        np.roll(head_mask,  1, axis=0) + np.roll(head_mask, -1, axis=0) +
        np.roll(head_mask,  1, axis=1) + np.roll(head_mask, -1, axis=1) +
        np.roll(head_mask, (1, 1), axis=(0, 1)) + np.roll(head_mask, (1, -1), axis=(0, 1)) +
        np.roll(head_mask, (-1, 1), axis=(0, 1)) + np.roll(head_mask, (-1, -1), axis=(0, 1))
    )
    
    # ルール適用
    # 頭 -> 尾
    new_grid[grid == HEAD] = TAIL
    # 尾 -> 導体
    new_grid[grid == TAIL] = WIRE
    # 導体 -> 頭 (周囲に頭が1つか2つある場合のみ)
    wire_mask = (grid == WIRE)
    new_grid[wire_mask & ((total_heads == 1) | (total_heads == 2))] = HEAD
    
    img.set_data(new_grid)
    grid = new_grid
    return img,

ani = animation.FuncAnimation(fig, update, frames=200, interval=80, blit=True)
plt.show()
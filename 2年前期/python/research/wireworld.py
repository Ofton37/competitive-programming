import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap

# --- 設定 ---
N = 50
EMPTY, HEAD, TAIL, WIRE = 0, 1, 2, 3

# 色: 背景(黒), 電子頭(青), 電子尾(赤), 導体(黄)
cmap = ListedColormap(['#000000', '#0077ff', '#ff4500', '#ffd700'])

# --- 初期配置 (ワイヤーと電子) ---
grid = np.zeros((N, N), dtype=int)

# 一本道のワイヤーを描く
grid[N//2, 5:-5] = WIRE
# 信号（頭と尾）を置く
grid[N//2, 5] = HEAD
grid[N//2, 6] = TAIL

# 分岐路を作ってみる
grid[N//2-5:N//2+5, 25] = WIRE
grid[N//2-5, 25:35] = WIRE
grid[N//2+5, 25:35] = WIRE

fig, ax = plt.subplots(figsize=(8, 4))
img = ax.imshow(grid, cmap=cmap, vmin=0, vmax=3)
ax.axis('off')
ax.set_title("Wireworld")

def update(frame):
    global grid
    new_grid = grid.copy()
    
    # 導体の場所を特定
    wire_mask = (grid == WIRE)
    
    # 各マスの周囲8マスの「電子の頭」の数をカウント
    head_mask = (grid == HEAD).astype(int)
    total_heads = (
        np.roll(head_mask,  1, axis=0) + np.roll(head_mask, -1, axis=0) +
        np.roll(head_mask,  1, axis=1) + np.roll(head_mask, -1, axis=1) +
        np.roll(head_mask, ( 1,  1), axis=(0, 1)) + np.roll(head_mask, ( 1, -1), axis=(0, 1)) +
        np.roll(head_mask, (-1,  1), axis=(0, 1)) + np.roll(head_mask, (-1, -1), axis=(0, 1))
    )
    
    # ルール適用
    new_grid[grid == HEAD] = TAIL       # 頭 -> 尾
    new_grid[grid == TAIL] = WIRE       # 尾 -> 導体
    # 導体 -> 頭 (周囲に頭が1つか2つの時)
    new_grid[wire_mask & ((total_heads == 1) | (total_heads == 2))] = HEAD
    
    img.set_data(new_grid)
    grid = new_grid
    return img,

ani = animation.FuncAnimation(fig, update, frames=100, interval=100, blit=True)
plt.show()
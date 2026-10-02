import numpy as np

# 最適化したい関数 (例: 2次関数。最小値は(0,0))
def objective_function(x):
    return np.sum(x**2)

# 初期設定
n_particles = 30  # 粒子の数
dim = 2           # 次数 (x, y)
w, c1, c2 = 0.5, 0.8, 0.9  # 重みパラメータ

# 粒子の位置と速度をランダムに初期化
pos = np.random.uniform(-5, 5, (n_particles, dim))
vel = np.random.standard_normal((n_particles, dim))

# 自己ベストと全体のベストの初期化
pbest = pos.copy()
pbest_score = np.array([objective_function(p) for p in pos])
gbest = pbest[np.argmin(pbest_score)]
gbest_score = np.min(pbest_score)

# 100回反復計算
for _ in range(100):
    r1, r2 = np.random.rand(2)
    # 速度の更新
    vel = w * vel + c1 * r1 * (pbest - pos) + c2 * r2 * (gbest - pos)
    # 位置の更新
    pos += vel
    
    # 評価と更新
    for i in range(n_particles):
        score = objective_function(pos[i])
        if score < pbest_score[i]:
            pbest_score[i] = score
            pbest[i] = pos[i]
            if score < gbest_score:
                gbest_score = score
                gbest = pos[i]

print(f"見つかった最適解: {gbest}, スコア: {gbest_score}")
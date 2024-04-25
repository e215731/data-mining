import numpy as np
import matplotlib.pyplot as plt

def true_function(x):
    return np.sin(np.pi * x * 0.8) * 10

def test_true_function():
    # x=0の場合、yは0であることをテスト
    assert true_function(0) == 0

# ユニットテストを実行
test_true_function()

# 定義域を設定
x_values = np.linspace(-1, 1, 100)  # -1から1までの等間隔な100個の点を生成

# 関数の値を計算
y_values = true_function(x_values)

# グラフを描画
plt.plot(x_values, y_values, label='y = sin(pi * x * 0.8) * 10')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)

# グラフを保存
plt.savefig('ex1.1.png')

# グラフを表示
plt.show()

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

labels = [1, 2, 3, 4, 5]

# 手动构造混淆矩阵（标准化为100）
cm_manual = np.array([
    [91, 0, 6, 0, 3],
    [2, 87, 1, 1, 9],
    [1, 9, 76, 3, 11],
    [3, 2, 4, 82, 9],
    [5, 12, 11, 19, 56]
])

# 可视化
cm_df = pd.DataFrame(cm_manual, index=labels, columns=labels)

plt.figure(figsize=(8, 6))
sns.heatmap(cm_df, annot=True, fmt='d', cmap='Blues', cbar=True)
plt.xlabel("预测评分")
plt.ylabel("真实评分")
plt.title("标准化混淆矩阵（模拟总样本数=100）")
plt.tight_layout()
plt.show()

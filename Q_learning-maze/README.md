这是一个用于学习强化学习 Q-learning 算法的练习项目，用于熟悉一些基本概念和开发测试流程。

参考了这一篇 [A Painless Q-learning Tutorial (一个 Q-learning 算法的简明教程)_动手学强化学习_皮果提的博客-CSDN博客](https://blog.csdn.net/itplus/article/details/9361915)

用一个 小机器人走出迷宫 的问题来 学习这个算法，如下图 有0-5个房间（最外面是5号房间），机器人开始时位于任意一个房间，找到走到5号房间的最优路径。

![](E:\chartGPT_app\Q_learning-maze\images\1.png)

Q-learning算法中有几个基本概念

状态 State：将每一个房间都作为一个状态

行为 Action：从一个房间转移到另一个房间作为一个行为

![](E:\chartGPT_app\Q_learning-maze\images\2.png)

以状态为行，行为是列，构造一个二维矩阵 Reward 用于定义房间之间的关系，能走到5号房间奖励为1，不能走到某房间奖励为-1，能走到某房间奖励为0。

机器人将通过经验学习，不断的从一个房间走到另一个房间，直到到达5号房间一次训练结束。进行n轮训练，并将结果更新到矩阵Q，根据如下公式更新：

**Q(s,a) = R(s,a) + γ * max{Q{s~,a~}}**

我觉得将问题抽象为二维矩阵的好处有：

1，可以在O(1)的时间复杂度查看和更新目标值

2，将结果保存到矩阵中作为统计，不用监控和统计图了

这个思路像是DFS，BFS算法，不同的是没有遍历所有解法，而是通过n次“训练”趋近于正确答案。

最后的答案如下图：

![](E:\chartGPT_app\Q_learning-maze\images\3.png)

 ![](E:\chartGPT_app\Q_learning-maze\images\4.png)

例如从2号房间出发，最佳路径应该是 2-3-1-5

一开始我想自己写这个训练代码，但是对这个强化学习概念不熟，对python也不熟。还是问c老师吧。

![](E:\chartGPT_app\Q_learning-maze\images\5.png)

c老师写的衰减因子gamma是0.95，文章里是0.8

c老师给的公式和文章里的不一样。为啥？

![](E:\chartGPT_app\Q_learning-maze\images\6.png)

结果正确（到达5号房间后就停止了）：

![](E:\chartGPT_app\Q_learning-maze\images\7.png)

代码：

```python
import numpy as np
import random

# 1，定义状态空间，行动空间
# 每一个房间是一个状态，AI从一个房间走到另一个房间是一个行为
# 2，定义奖励矩阵 能走到外面奖励为1，不能走到某房间奖励为-1，能走到某房间奖励为0
R = np.array([
    [-1, -1, -1, -1, 0, -1],
    [-1, -1, -1, 0, -1, 100],
    [-1, -1, -1, 0, -1, -1],
    [-1, 0, 0, -1, 0, -1],
    [0, -1, -1, 0, -1, 100],
    [-1, 0, -1, -1, 0, 100]
])
# 学习率（learning rate）是强化学习算法中的一个超参数
# 用于控制模型在更新策略时的步长大小。
# 在Q-Learning算法中，学习率通常表示为一个介于0和1之间的数值，
# 用符号 α 表示，表示模型在学习时应该给予多大的权重来更新当前的估计值。
# 一般来说，如果学习率设置过大，模型更新过程中可能会跳过最优解而陷入局部最优解；
# 如果学习率设置过小，模型可能需要更多的时间来收敛到最优解。
# 因此，通常需要根据具体问题和算法的特性来选择适当的学习率，常见的选择包括常数学习率、衰减学习率和自适应学习率等。
learning_rate = 0.8
# 定义参数 折扣因子 gamma
# 它用于衡量当前状态的奖励对未来奖励的影响，即衰减因子。
# gamma 值越大，模型越重视未来的奖励；gamma 值越小，模型越重视当前的奖励。
# 通常为 0.9 ~ 0.99 等数值
discount_factor = 0.8
# num_episodes 是指我们在 Q-Learning 算法中进行多少次游戏的迭代，每次迭代包含了若干轮决策，直到达到终止状态
num_episodes = 1000

# 3，令 Q = 0
Q = np.zeros_like(R) 

# 定义辅助函数，用于选择下一步行动
def choose_action(state):
    available_actions = np.where(R[state] >= 0)[0]  # 获取可行动列表 
    return random.choice(available_actions)  # 从可行动列表中随机选择一个行动

# 开始训练
for episode in range(num_episodes):
    state = random.randint(0, 5)  # 随机初始化起点
    while state != 5:  # 直到到达目标
        action = choose_action(state)
        next_state = action
        reward = R[state, action] 
        #Q[state, action] = (1 - learning_rate) * Q[state, action] + \
        # learning_rate * (reward + discount_factor * np.max(Q[next_state]))
        Q[state, action] = reward + discount_factor * np.max(Q[next_state])
        state = next_state

# 训练完成，测试智能体的表现
state = 2  # 从起点(2, 0)开始
print(Q)
# path = [(state,0)]
path = [state]
while state != 5:  # 直到到达目标
    action = np.argmax(Q[state]) # 获得最大值作为下一个状态
    next_state = action
    # path.append((action,Q[state,action]))
    path.append(action)
    state = next_state

print("最优策略:", path)
```

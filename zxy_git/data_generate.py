# 输入字符串
import sys
datas = "打开/开开+车窗/窗户+一下/"

# 1. 按 + 切分各个部分
parts = datas.split('+')

# 2. 解析每一部分，生成可选列表（处理末尾 / 表示可选）
options = []
for part in parts:
    # 按 / 分割
    choices = part.split('/')
    options.append(choices)
print(*options)
# 3. 生成所有组合（笛卡尔积）
from itertools import product
all_combinations = product(*options)
# 4. 打印所有非空拼接结果
for combo in all_combinations:
    result = ''.join(combo)
    print(result)
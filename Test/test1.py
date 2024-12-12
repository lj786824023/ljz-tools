import sys
import io

# 创建一个 StringIO 对象，用于保存重定向的输出
output = io.StringIO()

# 将 sys.stdout 重定向到 output
sys.stdout = output

# 在控制台中输出一些内容
print("Hello, world!")

# 将 sys.stdout 重定向回原来的输出
sys.stdout = sys.__stdout__

# 获取重定向的输出内容
result = output.getvalue()

# 输出重定向的输出内容
print(result)
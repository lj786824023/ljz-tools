import time


def zhuangshiqi(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print(f"执行耗时{t2 - t1}")
        return result

    return wrapper

def mk_decorator(sss):
    def decorator(func):
        def wrapper(*args, **kwargs):
            t1 = time.time()
            print(sss)
            result = func(*args, **kwargs)
            t2 = time.time()
            print(f"执行耗时{t2 - t1}")
            return result

        return wrapper
    return decorator


def qiuhe(n, m):
    s = 0
    for i in range(n, m + 1):
        s += i
    return s

@mk_decorator('abadasfdsaf')
def qiuhe2(n, m):
    s = 0
    for i in range(n, m + 1):
        s += i
    return s


# a1 = zhuangshiqi(qiuhe)
# s1 = a1(2, 1000000)
# print(s1)

s2 = qiuhe2(2, 1000000)
print(s2)

# 装饰器的作用：
#   给函数增加额外的功能，且不影响函数原本的代码和功能表达
#   复用减少代码冗余，例如打印日志、计算函数耗时等
#   优化历史代码时，已有的代码不用修改，只需要创建装饰器，给目标函数戴上帽子即可
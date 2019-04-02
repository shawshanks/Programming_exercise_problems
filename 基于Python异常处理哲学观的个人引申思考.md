## “三思而后行”还是“知错能改善莫大焉”？
在阅读《Data Structure & Algorithm in Python》一书的1.7.2节中，作者介绍了关于异常应该怎样对待处理的两种哲学观：
> One philosophy for managing exceptional cases is to "look before you leap."

中文翻译过来就是： 一种关于处理异常情况的哲学观就是“三思而后行”。 比如说 一个人尽皆知的小学数学除法法则：除数不能为零。
那么我们写程序时应该怎样处理这种情况呢？
“三思而后行”的哲学观认为：先对除数进行检查，然后再开始实际运算。用Python来写程序就是：
```Python
if y != 0:      # 检查除数是否为零，如果不是
    a = x / y   # 我们开始进行除法运算
else:
  ···do something else ···   # 如果除数为零，我们应该怎样处理
```

另一种哲学观是：
> It's easier to ask for forgiveness than it is to get permission.

直译为： 请求原谅比请求许可权限更容易。 意译就是“知错能改善莫大焉”。
那么用Python来处理除数不能为零的情况就是：
```Python
try: # 先尝试直接进行除法
    a = x / y
except ZeroDivisionError: # 如果除数为零
    ···do something else ···  # 我们来处理除数为零的情况
```

## 生活中两种观点的碰撞


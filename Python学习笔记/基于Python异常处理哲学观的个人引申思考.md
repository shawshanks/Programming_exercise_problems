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

## 两种观点的引申思考
上述两种哲学观可以引申到生活上的一些观念。比如说消费观，有的人花钱小心谨慎，每花一分钱都要思考再三，说的难听点就叫“抠门”。另一种人花钱如流水，想买什么就买什么，俗称“购物狂”。

## 我的观点
做事前想好可能的后果， 以及相应的处理办法。 就可以去做了，就如` except ZeroDivisionError ` 一样，可能会 `意外情况：除数为零` ，遇到这种情况，我们再
做好及时的补救措施。 既不过于小心谨慎，又不盲目冲动。 中庸之道大概就是如此吧。

##编程即人生

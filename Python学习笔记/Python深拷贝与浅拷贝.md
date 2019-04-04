## 参考链接
[copy --- 浅层 (shallow) 和深层 (deep) 复制操作](https://docs.python.org/zh-cn/3.7/library/copy.html?highlight=copy)

[Python中的赋值(复制)、浅拷贝与深拷贝](https://zhuanlan.zhihu.com/p/54011712)

[Shallow and Deep Copy](https://www.python-course.eu/python3_deep_copy.php)

## 浅拷贝
### 原理
一个 浅层复制 会构造一个新的复合对象，然后（在可能的范围内）将原对象中找到的 引用 插入其中。
![浅拷贝](https://www.python-course.eu/images/deep_copy_detailed5.png "浅拷贝效果")

### 方式
- 切片
- 工厂函数
- copy模块中的copy函数


## 深拷贝
### 原理
一个 深层复制 会构造一个新的复合对象，然后递归地将原始对象中所找到的对象的 副本 插入。

![深拷贝](https://www.python-course.eu/images/deep_copy_detailed8.png "深拷贝效果")

### 方式
只有一种形式，copy模块中的deepcopy函数

## 总结
无论是深拷贝还是浅拷贝， 拷贝之后，引用的还是相同的不可变对象

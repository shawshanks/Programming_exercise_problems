## 寻找目标在序列中一次出现的索引 p20
```python
# 移动一个字符串中的索引直到发现值为`'x'`的项，或者到达序列末尾
# Advance an index through a sequence of characters until finding an entry with value 'X' 
# or reaching the end of the sequence 

def if_in(data):
    j = 0
    while j < len(data) and data[j] != 'X':
        j += 1
    if j < len(data):
        return j
    else:
        return False

def if_in(data)
    for j in len(data):
       if data[j] == 'X':
           return j
     return False
```

## 寻找目标在序列中的出现次数 p23
```python
def count(data, target):
    n = 0 
    for i in len(data):
        if data[i] == target:
          n += 1
    return n
```

## 寻找序列中的最大值 p21 p22
```python
##方法一 检查列表中的值
def find_max1(data):
    biggest = data[0]
    for val in data:
        if val > biggest:
            biggest = val
    return biggest
       
       
##方法二 检查列表中的索引
def find_max2(data):
    big_index = 0
    for i in range(len(data)):
        if data[i] > data[big_index]:
            big_index = i
    return data[big_index]
            
```

## 对数据集合序列中的所有条目都乘以某个值 P25
```python
#方法一：
def scale(data, factor):
    for i in range(len(data)):
        data[i] *= factor
        
#方法二：使用列表推导式
[data[i] * factor for i in range(len(data))]
```

## 寻找某个数的因数 p40
```python
#方法1: for 循环
def factors(n):
    result = []
    for k in range(1, n):
        if n % k == 0:
            result.append(k)
    return result
 
# 方法2： 列表推导式
result = [k for k in range(1, n+1) if n % k == 0] # 在P43 1.9.2节中出现
    
 # 方法3： while 循环
def factor_while(n):
    result = []
    k = 1
    while k * k < n:
        if n % k == 0:
            result.append(k)
            result.append(n // k)
            k += 1
    if k * k == n:
        result.append(k)
 ```
 
 ## Fibonacci数列的生成器完成 p41
 ```python
 ## 会产生无限斐波那契数列
 def fibonacci():
    a , b = 0, 1
    while True:
        yield a 
        future = a + b
        a = b 
        b = future         # yield语句后面可以替换为： a, b = b, a+b
        
 ```
 
 ## 使用解析式（comprehension）语法计算一系列值的和，节省内存 P43
 ```python
 total = sum(k * k for k in range(1, n+1))
 ####################################################################
 # （k * k for k in range(1, n+1）) 生成一个 生成器（generator）      #
 # sum()函数推测是使用了for loop，每次生成的值与上次生成的值进行加法运算 #
 # 这样在运算的过程中只需要三个寄存器（或内存单位）来保存                #
 # 和， 上次计算值， 此次生成值，最大化节省内存。                       #
 # 如果使用列表解析式，则会先生成一个列表，列表多大，占用的内存也就有多大 #
 ####################################################################
 ```

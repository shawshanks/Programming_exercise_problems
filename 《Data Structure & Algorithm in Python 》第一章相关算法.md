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

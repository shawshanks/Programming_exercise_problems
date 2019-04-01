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
        return 'no'

def if_in(data)
    for j in len(data):
       if data[j] == 'X':
           return j
     return 'no'
```

## 寻找目标在序列中的出现次数 
```python
def count(data, target):
    n = 0 
    for i in len(data):
        if data[i] == target:
          n += 1
    return n
```

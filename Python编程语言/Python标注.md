[py3k新特性——声明参数类型的函数](https://hgoldfish.com/blogs/article/83/)

```python
import io

def add(x:int, y:int) -> int:
    return x + y

def write(f: io.BytesIO, data: bytes) -> bool:
    try:
        f.write(data)
    except IOError:
        return False
    else:
        return True
 ```
 在这函数里面，同时声明了两个函数参数的类型以及add()函数的返回值类型。可以看出，声明一个函数参数的类型，只要在参数名称的后面加个":"号，带上类型名称就行了。声明函数的返回值类型，只要在函数声明结束之前，也就是":"号之前加入一个"->"，带上类型名称。

我想，当调用者看到这个函数签名的话，一定能够很快地知道他需要传入哪种类型的参数了。IDE也可以通过函数签名来推定参数的类型。

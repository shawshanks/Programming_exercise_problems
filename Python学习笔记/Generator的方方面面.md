## 参考资料
- [《Data Structure & Algorithm in Python 》](https://book.douban.com/subject/10607365/) chapter1.8 
- [Python教学网站 Python Course 的Generators一章](https://www.python-course.eu/python3_generators.php)
- Python 官方文档：
  - [9.9. 生成器](https://docs.python.org/zh-cn/3.7/tutorial/classes.html#generators)
  - [7.7. yield 语句](https://docs.python.org/zh-cn/3.7/reference/simple_stmts.html#the-yield-statement)
  - [term-generator](https://docs.python.org/zh-cn/3.7/glossary.html#term-generator)
  
-------------------------------
# 生成器Generator
## 生成器是什么？
官方教程文档:
> Generator 是一个用于创建迭代器的简单而强大的工具。 它们的写法类似标准的函数，但当它们要返回数据时会使用 yield 语句。 每次对生成器调用 next() 时，它会从上次离开位置恢复执行（它会记住上次执行语句时的所有数据值）。

《Data Structure & Algorithm in Python 》:
>  A generator is implemented with a synatax that is very similar to indicate each element of the series， but instead of returning values,
a `yield` statement is executed to indicate each element of the series.

python-course
> Generators are a special kind of function, which enable us to implement or generate iterators. On the surface generators in Python look like functions, but there is both a syntactic and a semantic difference. One distinguishing characteristic is the yield statements. The yield statement turns a functions into a generator. A generator is a function which returns a generator object.

Python-course中说，generator是一个返回 generator object的函数。
那么什么是generator object是什么呢？

我们可以写一个generator函数，然后将所在模块导入解释器中：
```python
def generator():
	i = 0
	while Ture:
		yield i
		i += 1
```

```Python
>>> from new1 import generator
>>> a = generator()
>>> a
<generator object generator at 0x03328D70>
```

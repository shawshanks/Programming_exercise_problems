[6 steps to understanding a heap with Python](https://towardsdatascience.com/data-structure-heap-23d4c78a6962)
# heap 堆
## 堆定义
堆（英语：Heap）是计算机科学中的一种特别的树状数据结构。若是满足以下特性，即可称为堆：“给定堆中任意节点 P 和 C，若 P 是 C 的母节点，那么 P 的值会小于等于（或大于等于） C 的值”。若母节点的值恒小于等于子节点的值，此堆称为最小堆（min heap）；反之，若母节点的值恒大于等于子节点的值，此堆称为最大堆（max heap）。在堆中最顶端的那一个节点，称作根节点（root node），根节点本身没有母节点（parent node）。

堆始于 J._W._J._Williams 在 1964 年发表的堆排序（heap sort），当时他提出了二叉堆树作为此算法的数据结构。堆在戴克斯特拉算法（英语：Dijkstra's algorithm）中亦为重要的关键。

## 堆性质
堆的实现通过构造二叉堆（binary heap），实为二叉树的一种；由于其应用的普遍性，当不加限定时，均指该数据结构的这种实现。这种数据结构具有以下性质。

- 任意节点小于（或大于）它的所有后裔，最小元（或最大元）在堆的根上（堆序性 或父母优势 ）。
- 堆总是一棵完全树。即除了最底层，其他层的节点都被元素填满，且最底层尽可能地从左到右填入。(完全二叉树性质 Complete Binary Tree Property )

将根节点最大的堆叫做最大堆或大根堆，根节点最小的堆叫做最小堆或小根堆。常见的堆有二叉堆、斐波那契堆等。

所以在堆中,相连键值存在从上到下的顺序,而不存在从左到右的顺序.即使是同一节点的左右子树之间也没有任何关系.

## 堆高度
因为堆是二叉树的一种,所以堆高度即树高度. 

### 树深度与树高度
### 树深度 递归定义与Python递归实现
假设P为树中的某一节点,那么P的深度可以定义如下:

- 如果P是根节点, 那么P的深度为0
- 否则, P的深度为 P父节点的深度+1

递归实现:
```python
def depth(self, P):
    if self.is_root(p):
		return 0
	else:
		return 1 + self.depth(self.parent(p))
```

### 树高度 递归定义与递归实现
假设P是树中的某一节点,那么P的高度可以定义如下:

- 如果P是叶节点,那么P的高度为0
- 否则, P的高度为 P的 有着最大高度的子节点 的高度+1

**高度实现方法1**
```python
def height_1(self, p):
	if self.is_leaf(p):
		return 0
	else:
		return 1 + max(self.height_2(c) for c in self.children(p))
```

利用 `height_1()`, 我们可以计算任一子树的高度
```python
def height(self, p=None):
	"""Renturn the height of the subtree rooted at Position P."""
	if p is None:
		p = self.root()
	return height_2(p)	# start height2 recursion

```

#### 高度的实现方法2: 利用树高度和深度之间的关系
树高度与深度之间的关系: 树的高度等于叶节点的最大深度

递归实现:
```python
def height_1(self):
	"""Return the height of the tree"""
	return max(self.depth(p) for p in self.positions() if self.is_leaf(p))
```

## 堆实现
假设我们要实现一个最小堆.

因为堆定义为一种完全二叉树, 所以二叉树的完成也适用于堆的完成,只不过之后我们还要在完全二叉树的完成基础上,继续完成堆序型 (heap property).

完全二叉树的常见完成方法有以下三种:

- linked Structure 链表完成
- Array_based Representation  数组完成

下面我们展示数组完成 完全二叉树(Array_Based Representation of a complete Binary Tree)

### 树中的元素和数组索引之间的关系
<img src='https://github.com/shawshanks/Programming_exercise_problems/blob/master/Picture/%E5%A0%861.jpg' width="50%">

假设 数组索引从0开始, 一个堆节点的数组索引是 i,则:

- 如果一个节点 根节点, 则 它的数组索引 i = 0
- 数组索引为i的节点 的 左子节点 的数组索引为  left_child(i) = 2i + 1
- 数组索引为i的节点 的 右子节点 的数组索引为  right_child(i) = 2i + 2
- 数组索引为i的节点 的 父节点   的数组索引为  parent(i) = 向上取整(i/2) - 1


"""
用数组表示的堆
                        (0,v)
                        /   \
                    (1,v)    (2,v)
                   /    \
                 (3,v) (4,v)
数组□ □ □ □ □
索引0 1 2  3 4
"""
"""
Bottom_up 方法构建堆
最后一个叶节点的父节点是最后一个父节点, 从最后一个父节点开始从下往上检查.
最后一个父节点的索引i 与 数组长度 n 之间的关系:
如果最后一个叶节点为左子节点, 那么叶节点的个数为奇数, 最顶层的根节点是1,而其他层都是
偶数个几点, 所以总共的节点个数 为偶数,即 n为偶数. 此时这个最后一个叶节点的父节点索引
为 (n-1-1)/2 = (n-2)/2 = n/2 -1 因为n为偶数,所以n/2是个整数,那么 n/2-1 = n//2 -1
如果最后一个叶节点为右子节点, 则 n为奇数. 最后一个叶节点的父节点索引为
(n-1-2)/2 = (n-3)/2 = n/2 - 1.5 因为n为奇数, 所以 n//2 已经减去了 0.5, 所以
n/2 -1.5 = n//2 -1
子节点就以上两种情况, 综上,可知最后一个父节点的索引为 n//2-1
检查动作
父节点和子节点是否符合 最小堆性质:
父节点的值小于任何子节点的值
即 父节点的值是两个子节点值中最小的一个.
"""


def siftup(array, i):
    left = 2 * i + 1
    right = 2 * i + 2
    smallest = i
    endpos = len(array)
    # 确定 父节点,左子节点,右子节点 中值为最小的节点的索引
    if left < endpos and array[i] > array[left]:
        smallest = left
    if right < endpos and array[smallest] > array[right]:
        smallest = right
    # 确保父节点的值为最小的节点
    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        siftup(array, smallest)


def min_heapfy(array):
    n = len(array)
    for i in range(n//2 - 1, -1, -1):  # or reversed(range(n//2))
        siftup(array, i)


def heap_sort(array):
    min_heapfy(array)
    sorted_array = []
    for _ in range(len(array)):
        array[0], array[-1] = array[-1], array[0]   # 根节点是最小值
        sorted_array.append(array.pop())            # 弹出最小值
        siftup(array, 0)                            # 将根节点堆化

    return sorted_array


if __name__ == '__main__':
    list = [2, 4, 5, 1, 7, 3]
    sorted_list = heap_sort(list)
    print(sorted_list)

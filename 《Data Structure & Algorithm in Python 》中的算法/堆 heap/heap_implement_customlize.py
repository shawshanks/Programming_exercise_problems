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
调用方式:
min_heapfy(数组, 堆化的最后一个元素索引位置)
"""


def siftup(array, i, endpos=None):
    left = 2 * i + 1
    right = 2 * i + 2
    smallest = i
    if endpos is None or endpos > len(array):
        endpos = len(array)
    # 确定 父节点,左子节点,右子节点 中值为最小的节点的索引
    if left < endpos and array[i] > array[left]:
        smallest = left
    if right < endpos and array[smallest] > array[right]:
        smallest = right
    # 确保父节点的值为最小的节点
    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        siftup(array, smallest, endpos)


def min_heapfy(array, end=None):
    if end is None or end > len(array):
        end = len(array)
    end_parent = end//2 - 1
    for i in range(end_parent, -1, -1):  # or reversed(range(n//2))
        siftup(array, i, end)
    return array


if __name__ == '__main__':
    list = [2, 4, 5, 1, 7, 3, 10, 100]

    n = 4  # n 为索引
    print(min_heapfy(list, 4))

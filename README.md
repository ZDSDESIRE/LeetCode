# LeetCode

#### 补充内容

**1. 原地算法（in-place algorithm）**

```text
In computer science, an in-place algorithm is an algorithm which transforms input using no auxiliary data structure. However a small amount of extra storage space is allowed for auxiliary variables. The input is usually overwritten by the output as the algorithm executes. In-place algorithm updates input sequence only through replacement or swapping of elements. An algorithm which is not in-place is sometimes called not-in-place or out-of-place. ————摘自维基百科（原地算法）
```

可总结为：
原地算法不依赖额外的资源或者依赖少数的额外资源，仅依靠输出来覆盖输入的一种算法操作。

```py
# 原地算法的 Python 实现
def reverse(a):
    """
    :param a: list
    :return: list
    """
    n = len(a)-1
    tmp = list()
    for i in range(int(n/2)):
        tmp = a[i]
        a[i] = a[n-i]
        a[n-i] = tmp
    print(a)

    return a

if __name__ == '__main__':
   a = [1, 2, 3, 4, 5, 6]
   reverse(a)

# 输出
-------------------------------
[6, 5, 3, 4, 2, 1]
```

import collections
from collections import Counter

#Counter
s = 'abcbcaadceddsef'
l = {'a', 'b', 'c', 'a', 'b', 'b'}
d = {'2': 3, '3': 2, '17': 2}
print(Counter(s))
print(Counter(l))
print(Counter(d))

#most_common
m1 = Counter(s)
print(m1)
print(m1.most_common(3))

#elements 返回经过计数器Counter后的元素，返回的是一个迭代器
e1 = Counter(s)
print(''.join(sorted(e1.elements())))
e2 = Counter(d)
print(sorted(e2.elements()))

# update 和set集合的update一样，对集合进行并集操作
u1 = Counter(s)
u1.update('123a')
print(u1)

# substract 做差集操作
sub1 = 'which'
sub2 = 'whatw'
subset = Counter(sub1)
print(subset)
subset.subtract(Counter(sub2))
print(subset)
print(''.join(sorted(subset.elements())))

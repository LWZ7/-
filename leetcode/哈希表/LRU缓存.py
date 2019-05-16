'''
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。

获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。

进阶:

你是否可以在 O(1) 时间复杂度内完成这两种操作？

示例:

LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回  1
cache.put(3, 3);    // 该操作会使得密钥 2 作废
cache.get(2);       // 返回 -1 (未找到)
cache.put(4, 4);    // 该操作会使得密钥 1 作废
cache.get(1);       // 返回 -1 (未找到)
cache.get(3);       // 返回  3
cache.get(4);       // 返回  4
'''

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.save_dic = {}

    def get(self, key: int) -> int:
        try:
            self.save_dic[key] = self.save_dic.pop(key)
            return self.save_dic[key]
        except:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.save_dic:
            if self.save_dic.__len__() >= self.capacity:
                iterer = iter(self.save_dic)
                self.save_dic.pop(next(iterer))
        else:
            self.save_dic.pop(key)
        self.save_dic[key] = value
        
#put，如果有这个key，删除再加入，如果没有这个key，先看看容量，容量不够了，弹出第一个，加入新的。容量够，直接加入

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

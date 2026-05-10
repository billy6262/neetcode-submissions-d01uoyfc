class LRUCache:

    def __init__(self, capacity: int):
       self.cap = capacity
       self.hashmap = {} 
       self.ageque = []

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.ageque.remove(key)
            self.ageque.append(key)
            return self.hashmap[key]
        else:
            return -1
        
    
    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.ageque.remove(key)
            self.ageque.append(key)
        else:
            self.ageque.append(key)

        self.hashmap[key] = value
        if len(self.ageque) > self.cap:
            self.hashmap.pop(self.ageque.pop(0))
        

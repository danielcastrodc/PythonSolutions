# You may not use dicts.

class HashTable():
    def __init__(self, size, hash1):
        # Create an empty hashtable with the size given, and stores the
        # function hash1
        self.size = size
        self.hash1 = hash1
        self.count= 0
        self.hashTable = [None] * size
        pass
    
    def put(self, key, data):
        # Store data with the key given, return true if successful or
        # false if the data cannot be entered
        # On a collision, the table should not be changed
        position = self.hash1(key)
        if self.hashTable[position] is None:
            self.hashTable[position] = (key, data)
            self.count += 1
            return True
        else:
            return False
        pass
    
    def get(self, key):
        # Returns the item linked to the key given, or None if element
        # does not exist
        position = self.hash1(key)
        return self.hashTable[position][1] if self.hashTable[position][0]==key else None      
        pass
        
    def __len__(self):
        # Returns the number of items in the Hash Table
        return self.count
        pass

    def isFull(self):
        # Returns true if the HashTable cannot accept new members
        return self.count == self.size
        pass

class ChainTable(MyHashTable):
    def __init__(self, size, hash1):
        # Create an empty hashtable with the size given, and stores the
        # function hash1
        super().__init__(size,hash1)
        pass
    
    def put(self, key, data):
        # Store the data with the key given in a list in the table,
        # return true if successful or false if the data cannot be entered
        # On a collision, the data should be added to the list
        position = self.hash1(key)
        if self.hashTable[position] is None:
            self.hashTable[position] = [(key, data)]
            self.count += 1
            return True
        else:
            self.hashTable[position].append((key, data))
            self.count += 1
            return True
        return False
        pass

    def get(self, key):
        # Returns the item linked to the key given, or None if element
        # does not exist
        position = self.hash1(key)
        if self.hashTable[position][0]==key:
            return self.hashTable[position][1]
        else:
            for item in self.hashTable[position]:
                if item[0]== key:
                    return item[1]
        return None 
        pass
        
    def __len__(self):
        # Returns the number of items in the Hash Table
        return self.count
        pass

    def isFull(self):
        # Returns true if the HashTable cannot accept new members
        return self.count == self.size
        pass

class DoubleHashTable(MyHashTable):
    def __init__(self, size, hash1, hash2):
        # Create an empty hashtable with the size given, and stores the
        # functions hash1 and hash2
        super().__init__(size,hash1)
        self.hash2 = hash2
        pass
    
    def put(self, key, data):
        # Store data with the key given, return true if successful or
        # false if the data cannot be entered
        # On a collision, the key should be rehashed using some combination
        # of the first and second hash functions
        position = self.hash1(key)
        position2 = self.hash2(key)
        if self.hashTable[position] is None:
            self.hashTable[position] = (key, data)
            self.count += 1
            return True
        elif self.hashTable[position2] is None:
            self.hashTable[position2] = (key, data)
            self.count += 1
            return True
        else:
            i = 0
            while i < len(self.hashTable):
                position = self.hash1(position+position2+i)
                position2 = self.hash2(position+position2+i)
                if self.hashTable[position] is None:
                    self.hashTable[position] = (key, data)
                    self.count += 1
                    return True
                elif self.hashTable[position2] is None:
                    self.hashTable[position2] = (key, data)
                    self.count += 1
                    return True
                elif self.hashTable[i] is None:
                    self.hashTable[i] = (key, data)
                    self.count += 1
                    return True
                i += 1
            return False
        pass
    
    def get(self, key):
        # Returns the item linked to the key given, or None if element does
        # not exist
        position = self.hash1(key)
        position2 = self.hash2(key)
        result1 = self.hashTable[position][1] if self.hashTable[position][0]==key else None
        if result1 is not None:
            return result1
        result2 = self.hashTable[position2][1] if self.hashTable[position2][0]==key else None
        if result2 is not None:
            return result2
        i = 0
        while i < len(self.hashTable):
            position = self.hash1(position+position2+i)
            position2 = self.hash2(position+position2+i)
            result1 = self.hashTable[position][1] if self.hashTable[position][0]==key else None
            result2 = self.hashTable[position2][1] if self.hashTable[position2][0]==key else None
            result3 = self.hashTable[i][1] if self.hashTable[i][0]==key else None
            if result1 is not None:
                return result1
            if result2 is not None:
                return result2
            if result3 is not None:
                return result3
            i += 1
        return None
        pass
        
    def __len__(self):
        # Returns the number of items in the Hash Table
        return self.count
        pass

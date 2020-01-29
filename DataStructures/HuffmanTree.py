import heapq

class HuffmanTree():
    def __init__(self):
        self.root = None # head of huffman tree
        self.weights = None  #weights given initially
        self.dict = None # dict version of values to improve encoding
        pass

    def build(self, weights):
        # Build a huffman tree from the dictionary of character:value pairs

        self.weights = weights

        sortedWeights = []
        for char in weights:
            sortedWeights.append(Node(weights[char], char))
        heapq.heapify(sortedWeights)

        while len(sortedWeights) > 1:
            n1 = heapq.heappop(sortedWeights)
            n2 = heapq.heappop(sortedWeights)
            n3 = Node(n1.freq + n2.freq, None)
            n3.left = n1
            n3.right = n2
            heapq.heappush(sortedWeights, n3)

        self.root = sortedWeights[0]
        self.root.completeBuild()

        newDict = self.root.GenerateDict()
        self.dict = newDict
        return True
        pass
    
    def encode(self, word):
        # Return the bitstring of word encoded by the rules of your huffman tree

        # I could've encoded with the huffman tree but I just use
        # a dict based on the huffman tree to simplify this
        bits = ''
        for _ in word:
            bits += self.dict[_]
        return bits
        pass
    
    def decode(self, bitstring):
        # Return the word encoded in bitstring, or None if the code is invalid
        
        node = self.root
        spam = ''
        for _ in bitstring:
            if _ == '0':
                node = node.left
            else:
                node = node.right
            if node.char is not None:
                spam += node.char
                node = self.root
        return spam
        pass

class Node:
    def __init__(self,value,data,left=None,right=None):
        self.freq = value # frequency
        self.char = data # 'a'
        self.left = left
        self.right = right
        self.rep = None # '101001'
        pass

    def __lt__(self, other):
        # Ordering a < b lt(a, b)
        if (other == None):
            return -1
        if (not isinstance(other, Node)):
            return -1
        return self.freq < other.freq
        pass
    
    def __le__(self, other):
        # Ordering a <= b le(a, b)
        if (other == None):
            return -1
        if (not isinstance(other, Node)):
            return -1
        return self.freq <= other.freq
        pass

    def __gt__(self, other):
        # Ordering a > b gt(a, b)
        if (other == None):
            return -1
        if (not isinstance(other, Node)):
            return -1
        return self.freq < other.freq
        pass
    
    def __ge__(self, other):
        # Ordering a >= b ge(a, b)
        if (other == None):
            return -1
        if (not isinstance(other, Node)):
            return -1
        return self.freq >= other.freq
        pass

    def completeBuild(self, path=''):
        if self:
            self.rep = path
            if self.left is not None:
                self.left.completeBuild(path+'0')
            if self.right is not None:
                self.right.completeBuild(path+'1')
    pass

    def GenerateDict(self, newDict=dict()):
        if self:
            if self.char is not None:
                newDict[self.char] = self.rep
            if self.left is not None:
                self.left.GenerateDict(newDict)
            if self.right is not None:
                self.right.GenerateDict(newDict)
        return newDict
    pass

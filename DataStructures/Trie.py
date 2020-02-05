class Trie:
    def __init__(self):
        # Initialize the trie node as needed
        self.root = Node()
        self.count = 0
        pass
    
    def insert(self, word):
        # Insert a word into this trie node
        node = self.root
        self.count += 1
        for char in list(word):
            node.wordList.append(word)
            if not node.children.get(char):
                node.children[char] = Node()
            node = node.children[char]
        node.last = True
        node.word = word
        node.wordList.append(word) # for non-recursive solution
        pass

    def exists(self, word, position=0):
        # Return true if the passed word exists in this trie node
        # A terminal node will return true if the word passed is ""
        node = self.root
        for char in list(word):
            position+=1
            if not node.children.get(char):
                return False
            node = node.children[char]
            if node.last and position == len(word) and node.word == word:
                return True
        pass

    def isTerminal(self):
        # Return true if this node is the terminal point of a word
        return self.root.last
        pass

    def autoComplete(self, prefix, position=0):
        # Return every word that extends this prefix in alphabetical
        # order

        solution = []
        node = self.root
        for char in list(prefix):
            position+=1
            if not node.children.get(char):
                return []
            node = node.children[char]

        # once we're at the prefix-based root, use recursively function
        if node.last is True:
            solution = node.allWords([node.word])
        else:
            solution = node.allWords([])
        return solution
        
        ''' iterative solution based on presaved wordList
        node = self.root
        for char in list(prefix):
            position+=1
            if not node.children.get(char):
                return []
            node = node.children[char]
        return node.wordList
        '''
        pass

    def __len__(self):
        # Return the number of words that either terminate at this
        # node or descend from this node
        # A terminal leaf should have length 1, the node A with
        # terminal child leaves B|C should have length 2
        return self.count
        pass

class Node():
    def __init__(self):
        self.children = {}
        self.last = False
        self.word = ""
        self.wordList = [] # for non-recursive solution
        pass

    def allWords(self, result=[]):
        # Recursively create list of words decending from this node
        for node in self.children.values():
            if node.last is True:
                result.append(node.word)
            node.allWords(result)
        return result
        pass

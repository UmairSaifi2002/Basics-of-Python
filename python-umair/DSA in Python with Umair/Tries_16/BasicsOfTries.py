class TriesNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False

class Tries:
    def __init__(self):
        self.root = TriesNode()

    # insert a String in Trie
    # Case 1: A Trie is Blank/Empty
    # Case 2: New String Prefix is common to another string Prefix
    # Case 3: New String prefix is already present as complete string
    # Case 4: String to be inserted is already present in Trie
    def insert(self, word):
        current = self.root  # Root node se shuru karo
        for i in word:
            ch = i  # Current character
            node = current.children.get(ch)  # Check karo ki ye character already hai ya nahi
            if node == None:
                node = TriesNode()  # Agar nahi hai toh naya node banayo
                current.children.update({ch:node})  # Naye node ko current node ke children mein add karo
            current = node  # Current node ko update karo
        current.endOfString = True  # Word ka end mark karo
        print('Successfully inserted')

    # Search for a string in Tries
    # Case 1: String does not exist in Tries
    # Case 2: String exist in Tries
    # Case 3: String is a prefix of another string, but it does not exist in Tries.
    def search(self, word):
        currentNode = self.root
        for i in word:
            node = currentNode.children.get(i)
            if node == None:
                return False
            currentNode = node
        if currentNode.endOfString == True:
            return True
        else:
            return False

def deletes(root, word, index):
    # Base case: If we've processed the entire word
    if index == len(word):
        # If the current node is not the end of a word, the word doesn't exist
        if not root.endOfString:
            return False
        # Unmark the end of the word
        root.endOfString = False
        # Return True if the current node has no children (can be deleted)
        return len(root.children) == 0

    ch = word[index]  # Current character
    currentNode = root.children.get(ch)  # Get the child node

    # If the character doesn't exist in the Trie, the word doesn't exist
    if currentNode is None:
        return False

    # Recursively delete the next character in the word
    canThisNodeBeDeleted = deletes(currentNode, word, index + 1)

    # If the child node can be deleted, remove it from the current node's children
    if canThisNodeBeDeleted:
        root.children.pop(ch)
        # Return True if the current node has no children and is not the end of another word
        return len(root.children) == 0 and not root.endOfString

    # If the child node cannot be deleted, return False
    return False

# Delete a String from Tries
# Case 1: Some other prefix of string is same as the one that we want to delete
# Case 2: The String is a prefix of another string
# Case 3: Other String is a prefix of this string
# Case 4: Not any node depends on this String

newTrie = Tries()
newTrie.insert('Apps')
newTrie.insert('Appis')

print(newTrie.search('Apps')) # True
print(newTrie.search('App')) # False

deletes(newTrie.root, 'Apps', 0)
print(newTrie.search('Apps')) # False

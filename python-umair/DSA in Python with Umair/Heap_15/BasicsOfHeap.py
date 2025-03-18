class Heap:
    def __init__(self, size):
        # Heap ka constructor. Yeh ek custom list banata hai jiska size 'size+1' hai.
        # 'heapSize' current heap ka size batata hai aur 'maxSize' maximum allowed size hai.
        self.customList = (size+1) * [None]  # Heap ko store karne ke liye list
        self.heapSize = 0  # Abhi heap mein kitne elements hain
        self.maxSize = size+1  # Heap ka maximum size

def peekOfHeap(rootNode):
    # Heap ka top element return karta hai (root node).
    # Agar heap khali hai toh kuch return nahi karega.
    if not rootNode:
        return
    else:
        return rootNode.customList[1]  # Root node always index 1 par hota hai

def sizeOfHeap(rootNode):
    # Heap ka current size return karta hai.
    # Agar heap khali hai toh kuch return nahi karega.
    if not rootNode:
        return
    else:
        return rootNode.heapSize

def LevelOrderTraversal(rootNode):
    # Heap ko level order mein print karta hai.
    # Yeh ek tarah ka Breadth-First Traversal hai.
    if not rootNode:
        return
    else:
        for i in range(1, rootNode.heapSize+1):
            print(rootNode.customList[i], end=', ')  # Har element ko print karo

def heapifyTreeInsert(rootNode, index, heapType):
    # Insertion ke baad heap property maintain karne ke liye yeh function use hota hai.
    # Yeh function parent aur child nodes ko compare karke swap karta hai.
    parentIndex = int(index/2)  # Current node ka parent index
    if index <= 1:
        return  # Agar root node hai toh return
    if heapType == 'Min':
        # Min Heap ke liye: agar child parent se chota hai toh swap karo
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            rootNode.customList[index], rootNode.customList[parentIndex] = rootNode.customList[parentIndex], rootNode.customList[index]
        heapifyTreeInsert(rootNode, parentIndex, heapType)  # Recursively parent ko check karo
    if heapType == 'Max':
        # Max Heap ke liye: agar child parent se bada hai toh swap karo
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            rootNode.customList[index], rootNode.customList[parentIndex] = rootNode.customList[parentIndex], rootNode.customList[index]
        heapifyTreeInsert(rootNode, parentIndex, heapType)  # Recursively parent ko check karo

def insertNode(rootNode, nodeValue, heapType):
    # Heap mein naya node insert karta hai.
    # Agar heap full hai toh message return karta hai.
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "The Binary Heap is Full."
    rootNode.customList[rootNode.heapSize + 1] = nodeValue  # Naya element last mein add karo
    rootNode.heapSize += 1  # Heap size ko increment karo
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)  # Heap property maintain karo
    return "The value has been Successfully Inserted"

def heapifyTreeExtract(rootNode, index, heapType):
    # Extraction ke baad heap property maintain karne ke liye yeh function use hota hai.
    # Yeh function parent aur child nodes ko compare karke swap karta hai.
    leftIndex = index*2  # Left child ka index
    rightIndex = index*2 + 1  # Right child ka index
    swapChild = 0  # Swap karne ke liye child ka index

    if rootNode.heapSize < leftIndex:
        return  # Agar left child nahi hai toh return
    
    elif rootNode.heapSize == leftIndex:
        # Agar sirf left child hai
        if heapType == 'Min':
            # Min Heap ke liye: agar parent left child se bada hai toh swap karo
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                rootNode.customList[index], rootNode.customList[leftIndex] = rootNode.customList[leftIndex], rootNode.customList[index]
            return
        else:
            # Max Heap ke liye: agar parent left child se chota hai toh swap karo
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                rootNode.customList[index], rootNode.customList[leftIndex] = rootNode.customList[leftIndex], rootNode.customList[index]
            return
        
    else:
        # Agar dono left aur right child hain
        if heapType == 'Min':
            # Min Heap ke liye: chota child select karo
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            # Agar parent selected child se bada hai toh swap karo
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                rootNode.customList[index], rootNode.customList[swapChild] = rootNode.customList[swapChild], rootNode.customList[index]
        else:
            # Max Heap ke liye: bada child select karo
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            # Agar parent selected child se chota hai toh swap karo
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                rootNode.customList[index], rootNode.customList[swapChild] = rootNode.customList[swapChild], rootNode.customList[index]
        heapifyTreeExtract(rootNode, swapChild, heapType)  # Recursively child ko check karo

def extractNode(rootNode, heapType):
    # Heap se root node extract karta hai aur heap property maintain karta hai.
    if rootNode.heapSize == 0:
        return  # Agar heap khali hai toh kuch return nahi karega
    else:
        extractedNode = rootNode.customList[1]  # Root node extract karo
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]  # Last node ko root par move karo
        rootNode.customList[rootNode.heapSize] = None  # Last node ko null karo
        rootNode.heapSize -= 1  # Heap size ko decrement karo
        heapifyTreeExtract(rootNode, 1, heapType)  # Heap property maintain karo
        return extractedNode  # Extracted node return karo

def deleteBinaryHeap(rootNode):
    rootNode.customList = None
    
# Example usage:
newBinaryHeap = Heap(5)  # 5 size ka Max Heap banaya
insertNode(newBinaryHeap, 4, 'Max')  # 4 insert kiya
insertNode(newBinaryHeap, 2, 'Max')  # 2 insert kiya
insertNode(newBinaryHeap, 6, 'Max')  # 6 insert kiya
insertNode(newBinaryHeap, 5, 'Max')  # 5 insert kiya
insertNode(newBinaryHeap, 1, 'Max')  # 1 insert kiya

LevelOrderTraversal(newBinaryHeap)  # Heap ko level order mein print kiya

print(extractNode(newBinaryHeap, 'Max'))

LevelOrderTraversal(newBinaryHeap)
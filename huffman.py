import heapq
class Node:
    def _init_(self,freq,symbol,left=None,right=None):
        self.freq=freq
        self.symbol=symbol
        self.left =left
        self.right = right
        self.huff=''
    def _lt_(self,nxt):
        return self.freq < nxt.freq
def user():
    chars=input("chars :").split()
    freq = list(map(int,input("freq : ").split()))
    return chars,freq
def huffman(chars,freq):
    nodes=[]
    for x in range(len(chars)):
        heapq.heappush(nodes,Node(freq[x],chars[x]))
    while len(nodes)>1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
        left.huff=0
        right.huff=1
        newNode = Node(left.freq + right.freq , left.symbol+right.symbol,left,right)
        heapq.heappush(nodes,newNode)
    return nodes[0]
def printa(node,val=''):
    newv=val+str(node.huff)
    if node.left:
        printa(node.left,newv)
    if node.right:
        printa(node.right,newv)
    if not node.right and not node.left:
        print(f"{node.symbol}->{newv}")
chats,freq=user()
root=huffman(chats,freq)
printa(root)
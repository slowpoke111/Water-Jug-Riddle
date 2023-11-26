import queue

class Node:
  def __init__(self,volumeA,volumeB):
    #self.key = key
    #self.neighbors = {}
    #self.weight=0
    self.volume=[volumeA,volumeB]
    self.neighbors=[]
    
  def generateNeighbor(self):
    #self.neighbors[node.key]=weight
    neighbors=[]
    #fill
    neighbors.append(Node(3,self.volume[1]))
    neighbors.append(Node(self.volume[0],5))
    #empty
    neighbors.append(Node(0,self.volume[1]))
    neighbors.append(Node(self.volume[0],0))
    #pour
    if self.volume[0]+self.volume[1]<=5:
      neighbors.append(Node(0,sum(self.volume)))
    else:
      volumeA=self.volume[0]
      volumeB=self.volume[1]
      while volumeB!=5:
        volumeB+=1
        volumeA-=1
      neighbors.append(Node(volumeA,volumeB))
      
    if self.volume[0]+self.volume[1]<=3:
      neighbors.append(Node(sum(self.volume),0))
    else:
      neighbors.append(Node(3,self.volume[1]-(3-self.volume[0])))
      
    self.neighbors=neighbors
      
  def isSolved(self):
    return(self.volume[1]==4)
  
  def __eq__(self,other):
    return self.volume==other.volume
  
  def __lt__(self, other):
    return self.volume < other.volume
  
  def __hash__(self):
    return(int(str(self.volume[0])+str(self.volume[1])))
    
  def heuristic(self):
    if self.isSolved():
      return(0)
    else:
      return(abs(self.volume[1]-self.volume[0]))
  
  def __str__(self):
    return('Volume: '+str(self.volume[0])+','+str(self.volume[1]))

class Graph:
  def __init__(self,root):
    #self.graph = {}
    self.root=root
    #Key:Key-Neighbors
    
  #def addNode(self,node):
    
    #self.graph[node.key]=node
    
  #def addEdge(self,node1,node2,weight):
    '''
    if node1.key in self.graph and node2.key in self.graph:
      node1.addNeighbor(node2,weight)
      node2.addNeighbor(node1,weight)
    else:
      print('Node is not in graph')
'''

  #def __str__(self):
    '''
    string=''
    for node in self.graph:
      string+=self.graph[node].__str__()+'\n'
    return(string)
'''
  def greedySearch(self):
    visted=set()
    seen=queue.PriorityQueue()
    count=0
    seen.put((self.root.heuristic(),self.root,[self.root]))
    
    while seen:
      h,node,path=seen.get()
      if node not in visted:
        print(node)
        visted.add(node)
        count+=1
        if node.isSolved():
          return(path,count)
        node.generateNeighbor()
  
        for n in node.neighbors:
          if n not in visted:
            seen.put((n.heuristic(),n,path+[n]))
  
  def a_star(self):
    visted=set()
    seen=queue.PriorityQueue()
    count=0
    #f,depth,node,path
    seen.put((0,0,self.root,[self.root]))
    
    while seen:
      f,depth,node,path=seen.get()
      if node not in visted:
        visted.add(node)
        print(node)
        count+=1
        if node.isSolved():
          return(path,count)
        node.generateNeighbor()
        for n in node.neighbors:
          if n not in visted:
            seen.put((depth+1+n.heuristic(),depth+1,n,path+[n]))

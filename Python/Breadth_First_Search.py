import queue
import os
from Node import Node
def ID():
    graph =[]
    with open('InputFile.txt') as f:
        l=f.readline()
        s=l.strip().split(',')[0]
        e=l.strip().split(',')[1]
        while True:
            l = f.readline()
            if not l:
                break
            x=CreatedNote(l.strip().split(',')[0],graph)
            x.setneighbors(l.strip().split(',')[1])
            neighbors=x.neighbor.split()
            for i in range(0,len(neighbors)):
                CreatedNote(neighbors[i],graph)
    return graph,s,e
def CreatedNote(vertex,graph):
    for i in graph:
        if vertex==i.vertex:
            return i
    v=Node(vertex)
    graph.append(v)  
    return v 
def ED(v,g,vt,q):
    PV(v)
    PN(g)
    PVT(vt)
    PIVQ(q)
def PV(v):
    with open('Out_BreadthFirstSearch.txt', 'a') as f:
        f.write(v.vertex)
        f.write('\t\t\t\t\t')
        f.close()
def PN(g):
    with open('Out_BreadthFirstSearch.txt', 'a') as f:
        if g:
            for neighbor in g:
                f.write(neighbor)
            f.write('\t\t\t\t\t')
        else: f.write('\t\t\t\t\t')
        f.close()
def PVT(vt):
    with open('Out_BreadthFirstSearch.txt', 'a') as f:
        for v in vt:
            f.write(v)
        f.write('\t\t\t\t')
        f.close()
def PIVQ(q):
    list=[]
    while q.qsize():
        v=q.get()                                        
        list.append(v)
    with open('Out_BreadthFirstSearch.txt', 'a') as f:
        for v in list:
            f.write(v.vertex)
        f.write('\n')
        f.close()
    while list:
        q.put(list.pop(0))
def SD(st):
    print(st)
    list,e=[],st.pop()
    list.append(e)
    while st:
        v=st.pop()
        l=Vertex(v).neighbor.split()
        if l:
            if  e in l:
                e=v
                list.append(e)
    with open('Out_BreadthFirstSearch.txt', 'a') as f:
        f.write("Direction =>")
        for i in range(len(list)-1,-1,-1):
            f.write('->'+list[i])
def Vertex(x):
    n=Node(x)
    for i in range(0,len(graph)):
            if x is graph[i].vertex:
                n = graph[i]
    return n
def BFS():
    vt,q,st=[],queue.Queue(),[];
    q.put(Vertex(s))
    while q:
        v=q.get()
        st.append(v.vertex)
        if v.vertex  not in vt:
            vt.append(v.vertex)
        g=v.neighbor.split(); 
        if v.vertex==Vertex(e).vertex: 
            ED(v,g,vt,q)
            break
        if g:
            for neighbor in g:
                if neighbor not in vt:
                    vt.append(neighbor)   
                    q.put(Vertex(neighbor))     
        ED(v,g,vt,q) 
    SD(st);
if __name__ == '__main__':
        os.remove('Out_BreadthFirstSearch.txt')
        graph,s,e =ID()
        with open('Out_BreadthFirstSearch.txt', 'a') as f:
            f.write('TT\t\t\t\tTrang Thai Ke\t\t\tDanh sach Q\t\t\t\tDanh sach L\n')
            f.close()
        BFS()

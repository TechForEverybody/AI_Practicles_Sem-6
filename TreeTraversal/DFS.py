GRAPH=[]
DFS_Traversal=[]
isgoal_reached=False
goal=5
Number_of_Nodes=int(input("Enter the number of nodes : "))
for i in range(Number_of_Nodes):
    input_value=input()
    input_array=[int(i) for i in input_value.split(" ")]
    GRAPH.append(input_array)
    DFS_Traversal.append(0)

def DFS(position):
    global isgoal_reached
    if position==goal or isgoal_reached==True:
        isgoal_reached=True
        return
    print(chr(position+65),end=" ")
    DFS_Traversal[position]=1
    for i in range(Number_of_Nodes):
        if GRAPH[position][i]==1 and DFS_Traversal[i]==0:
            # print(position,end=" ")
            DFS_Traversal[i]=1
            DFS(i)

print("\n\nDFS Traversal of given graph is as follows ")

DFS(0)
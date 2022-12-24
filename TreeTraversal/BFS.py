queue=[]
GRAPH=[]
BFS_Traversal= []
# goal=5
Number_of_Nodes=int(input("Enter the number of nodes : "))
for i in range(Number_of_Nodes):
    input_value=input()
    input_array=[int(i) for i in input_value.split(" ")]
    GRAPH.append(input_array)
    BFS_Traversal.append(0)

def BFS(position):
    print(chr(position+65),end=" ")
    queue.append(position)
    BFS_Traversal[position]=1
    while len(queue)!=0:
        element=queue.pop(0)
        for i in range(Number_of_Nodes):
            if GRAPH[element][i]==1 and BFS_Traversal[i]==0:
                print(chr(i+65),end=" ")
                # if i==goal:
                #     print("\nWe have Reached ad goal state")
                #     return
                queue.append(i)
                BFS_Traversal[i]=1
print("\n\nBFS Traversal of given graph is as follows ")
BFS(0)
Tree={}
Leaf={}
node_values={}

def Alpha_Beta_Pruning(node,alpha,beta,ismax):
    print("current node is --> ",node)
    print("Alpha --> ",alpha)
    print("Beta --> ",beta)
    if list(Tree.keys()).count(node)>0:
        values=[]
        for element in Tree[node]:
            value=Alpha_Beta_Pruning(node=element,alpha=alpha,beta=beta,ismax=not ismax)
            values.append(value)
            if ismax==True and value>alpha:
                alpha=value
            elif ismax==False and value<beta:
                beta=value
            # if ismax==True:
            if alpha>beta:
                break
        if ismax==True:
            node_values[node]=max(values)
            return max(values)
        else:
            node_values[node]=min(values)
            return min(values)
        
    else:
        if ismax==True:
            node_values[node]=max(Leaf[node])
            return max(Leaf[node])
        else:
            node_values[node]=min(Leaf[node])
            return min(Leaf[node])


if __name__=="__main__":
    number_of_nodes=int(input("Enter the number of nodes other than root : "))
    for i in range(number_of_nodes):
        input_value=input("Enter the current node and its previous node : ")
        current=input_value.split(" ")[0]
        previous=input_value.split(" ")[1]
        try:
            if Tree[previous]:
                Tree[previous]=Tree[previous]+[current]
        except:
            Tree[previous]=[current]
    print(Tree)
    number_of_leaf_nodes=int(input("Enter the number of leaf nodes : "))
    for i in range(number_of_leaf_nodes):
        node_name=input("Enter Node name : ")
        node_value=input("Enter Node values : ")
        values_list=[int(i) for i in node_value.split(" ")]
        Leaf.update({
            node_name:values_list
        })
    print(Leaf)



    final_value=Alpha_Beta_Pruning(node="A",alpha=-100,beta=100,ismax=True)
    print("Final Alpha : ",final_value)
    print(node_values)


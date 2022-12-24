Tree={
    # "A":["B","C","D"],
    # "B":["E","F"],
    # "C":["G","H"],
    # "D":["I","J"]
}
Leaf={
    # "E":[2,3],
    # "F":[5,9],
    # "G":[0],
    # "H":[7,4],
    # "I":[2,1],
    # "J":[5,6]
}
node_values={}
def Alpha_Beta_Pruning(node,alpha,beta,ismax):
    # print();
    # print();
    # print("alpha - > ",alpha);
    # print("beta - > ",beta);
    # print("ismax - > ",ismax);
    if list(Tree.keys()).count(node)>0:
        # print(Tree[node]);
        if ismax==True:
            value=alpha;
        else:
            value=beta
        values=[];
        for element in Tree[node]:
            # print(element);
            value=Alpha_Beta_Pruning(element,alpha,beta,not ismax);
            values.append(value);
            # print(value);
            if ismax==True and value>=alpha:
                alpha=value;
            elif ismax==False and value<=beta:
                beta=value;
            if ismax==False:
                if value<alpha:
                    break;
            else:
                if value>beta:
                    break;
        if ismax==True:
            node_values[node]=max(values);
            return max(values);
        else:
            node_values[node]=min(values);
            return min(values);
    else:
        if ismax==True:
            node_values[node]= max(Leaf[node]);
            return max(Leaf[node]);
        else:
            node_values[node]=min(Leaf[node]);
            return min(Leaf[node]);
    


if __name__=="__main__":
    print("Created By : SHIVKUMAR CHAUHAN\n");
    number_of_nodes=int(input("Enter Number Of Nodes other than Root You have : "));
    for i in range(number_of_nodes):
        node_details=input("Enter Node Name and Previous Node Name : ");
        node_value=node_details.split(" ")[0];
        node_previous=node_details.split(" ")[1];
        try:
            if Tree[node_previous]:
                Tree[node_previous]=Tree[node_previous]+[node_value];
        except:
            Tree[node_previous]=[node_value];
            pass
        # print(Tree[node_previous]);
    # print(Tree);
    number_of_leaf_nodes=int(input("Enter Number Of leaf Nodes You have : "));
    for i in range(number_of_leaf_nodes):
        node_details=input("Enter Leaf node Name : ")
        node_value=input("Enter the values of Leaf Node "+node_details+" : ")
        values=[int(i) for i in node_value.split(" ")]
        Leaf.update({
            node_details:values
        })
    # print(Leaf);


    final_value=Alpha_Beta_Pruning("A",alpha=-100,beta=100,ismax=True);
    # print(final_value);
    # print(node_values);
    traversal_path=[];
    for key,value in node_values.items():
        if value==final_value:
            traversal_path.append(key);
    traversal_path.reverse();
    print("\n\npath => "," -> ".join(traversal_path));
    print("path cost =",final_value);








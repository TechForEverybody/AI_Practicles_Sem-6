class A_star_Algorithm():
    def A_Star_Decision(self,state,current_chance,next_chance):
        # print(state)
        no_of_empty_cells=0
        empty_cell_index=[]
        return_values=[]
        for i in range(3):
            for j in range(3):
                if state[i][j]=="_":
                    no_of_empty_cells+=1
                    empty_cell_index.append(f"{i} {j}")
        for i in range(no_of_empty_cells):
            row=int(empty_cell_index[i].split(" ")[0])
            column=int(empty_cell_index[i].split(" ")[1])
            new_state=[]
            for i in range(3):
                _row=[]
                for j in range(3):
                    _row.append(state[i][j])
                new_state.append(_row)
            new_state[row][column]=current_chance
            # self.printSituation(state)
            return_value=self.find_huristic_value(new_state,next_chance,no_of_empty_cells)
            # print(return_value)
            return_values.append(return_value)
            # self.printSituation(new_state)
        # print(empty_cell_index)
        # print(return_values)
        final_value_to_be_return="0 0"
        # print(f"count of {max(return_values)} is {return_values.count(max(return_values))}")
        # max_element_count=return_values.count(max(return_values))
        max_element_count=0
        # if max_element_count>1:
        max_element_cells=[]
        for i in range(no_of_empty_cells):
            if return_values[i]>=max(return_values)/2:
                max_element_count+=1
                max_element_cells.append(empty_cell_index[i])
            elif return_values[i]==max(return_values):
                max_element_count+=1
                max_element_cells.append(empty_cell_index[i])

        # print(max_element_cells)
        # print(max_element_count)
        for i in range(no_of_empty_cells):
            if return_values[i]==max(return_values):
                # final_value_to_be_return=empty_cell_index[i]
                row_value=int(empty_cell_index[i].split(" ")[0])+1
                column_value=int(empty_cell_index[i].split(" ")[1])+1
                final_value_to_be_return=f"{row_value} {column_value}"
        return final_value_to_be_return,max_element_cells,max_element_count,return_values

    def handleMaximumCount(self,state,max_element_cells,max_element_count):
        temp=[]
        for i in range(max_element_count):
            # print("working on : ",max_element_cells[i])
            row=int(max_element_cells[i].split(" ")[0])
            column=int(max_element_cells[i].split(" ")[1])
            new_state=[]
            for i in range(3):
                _row=[]
                for j in range(3):
                    _row.append(state[i][j])
                new_state.append(_row)
            new_state[row][column]="X"
            temp.append(min(self.A_Star_Decision(new_state,"O",2)[3]))
        # print(temp)
        final_value_to_be_return=max_element_cells[0]
        for i in range(max_element_count):
            if temp[i]==max(temp):
                # final_value_to_be_return=empty_cell_index[i]
                row_value=int(max_element_cells[i].split(" ")[0])+1
                column_value=int(max_element_cells[i].split(" ")[1])+1
                final_value_to_be_return=f"{row_value} {column_value}"
                break
        return final_value_to_be_return


    def printSituation(self,current_condition):
        string=""
        for i in range(3):
            for j in range(3):
                string =string+"  "+current_condition[i][j]
            string=string+"\n"
        print(string)
    def find_huristic_value(self,state,chance,state_value):
        # print(chance)
        # self.printSituation(state)
        if (state[0][0]=="X" and state[0][1]=="X" and state[0][2]=="X") or (state[1][0]=="X" and state[1][1]=="X" and state[1][2]=="X") or (state[2][0]=="X" and state[2][1]=="X" and state[2][2]=="X") or (state[0][0]=="X" and state[1][0]=="X" and state[2][0]=="X") or (state[0][1]=="X" and state[1][1]=="X" and state[2][1]=="X") or (state[0][2]=="X" and state[1][2]=="X" and state[2][2]=="X") or (state[1][1]=="X" and state[0][0]=="X" and state[2][2]=="X") or (state[0][2]=="X" and state[1][1]=="X" and state[2][0]=="X"):
            return state_value

        # loosing condition
        if (state[0][0]=="O" and state[0][1]=="O" and state[0][2]=="O") or (state[1][0]=="O" and state[1][1]=="O" and state[1][2]=="O") or (state[2][0]=="O" and state[2][1]=="O" and state[2][2]=="O") or (state[0][0]=="O" and state[1][0]=="O" and state[2][0]=="O") or (state[0][1]=="O" and state[1][1]=="O" and state[2][1]=="O") or (state[0][2]=="O" and state[1][2]=="O" and state[2][2]=="O") or (state[1][1]=="O" and state[0][0]=="O" and state[2][2]=="O") or (state[0][2]=="O" and state[1][1]=="O" and state[2][0]=="O"):
            return -1*state_value
        #draw condition
        empty_rows=0
        for i in range(3):
            for j in range(3):
                if state[i][j]=="_":
                    empty_rows+=1
        if empty_rows==0:
            return 0


        # print("hello world")
        no_of_empty_cells=0
        empty_cell_index=[]
        for i in range(3):
            for j in range(3):
                if state[i][j]=="_":
                    no_of_empty_cells+=1
                    empty_cell_index.append(f"{i} {j}")
        returning_value=0
        # print(empty_cell_index)
        for i in range(no_of_empty_cells):
            row=int(empty_cell_index[i].split(" ")[0])
            column=int(empty_cell_index[i].split(" ")[1])
            new_state=[]
            for i in range(3):
                _row=[]
                for j in range(3):
                    _row.append(state[i][j])
                new_state.append(_row)
            if chance%2==0:
                new_state[row][column]="X"
            else:
                new_state[row][column]="O"
            # self.printSituation(state)
            returning_value=returning_value+self.find_huristic_value(new_state,chance+1,state_value-1)
            # self.printSituation(new_state)
        return returning_value


    # def checkSituation(self,current_condition): 
    #     return_codition=0
    #     #TODO: check winning condition
    #     if (current_condition[0][0]=="X" and current_condition[0][1]=="X" and current_condition[0][2]=="X") or (current_condition[1][0]=="X" and current_condition[1][1]=="X" and current_condition[1][2]=="X") or (current_condition[2][0]=="X" and current_condition[2][1]=="X" and current_condition[2][2]=="X") or (current_condition[0][0]=="X" and current_condition[1][0]=="X" and current_condition[2][0]=="X") or (current_condition[0][1]=="X" and current_condition[1][1]=="X" and current_condition[2][1]=="X") or (current_condition[0][2]=="X" and current_condition[1][2]=="X" and current_condition[2][2]=="X") or (current_condition[1][1]=="X" and current_condition[0][0]=="X" and current_condition[2][2]=="X") or (current_condition[0][2]=="X" and current_condition[1][1]=="X" and current_condition[2][0]=="X"):
    #         return_codition=1

    #     #TODO: check loosing condition
    #     if (current_condition[0][0]=="O" and current_condition[0][1]=="O" and current_condition[0][2]=="O") or (current_condition[1][0]=="O" and current_condition[1][1]=="O" and current_condition[1][2]=="O") or (current_condition[2][0]=="O" and current_condition[2][1]=="O" and current_condition[2][2]=="O") or (current_condition[0][0]=="O" and current_condition[1][0]=="O" and current_condition[2][0]=="O") or (current_condition[0][1]=="O" and current_condition[1][1]=="O" and current_condition[2][1]=="O") or (current_condition[0][2]=="O" and current_condition[1][2]=="O" and current_condition[2][2]=="O") or (current_condition[1][1]=="O" and current_condition[0][0]=="O" and current_condition[2][2]=="O") or (current_condition[0][2]=="O" and current_condition[1][1]=="O" and current_condition[2][0]=="O"):
    #         return_codition=-1

    #     #TODO: check draw condition
    #     empty_rows=0
    #     for i in range(3):
    #         for j in range(3):
    #             if current_condition[i][j]=="_":
    #                 empty_rows+=1
    #     if empty_rows==0:
    #         return_codition=0
    #     return return_codition



if __name__=="__main__":
    current_condition = [
            ["_", "_", "_"],
            ["_", "_", "_"],
            ["_", "_", "_"]
        ]
    computer=A_star_Algorithm()
    max_value,max_element_cells,max_element_count,return_values=computer.A_Star_Decision(current_condition,"X",1)
    print("choosed value as per the Huristic Value :",max_value)
    print("max_element_count : ",max_element_count)
    print("max_element_cells : ",max_element_cells)
    if max_element_count>1:
        print(computer.handleMaximumCount(current_condition,max_element_cells,max_element_count))











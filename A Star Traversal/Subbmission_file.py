class A_star_Algorithm():
    def A_Star_Decision(self,state,current_chance,next_chance):
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
            return_value=self.find_huristic_value(new_state,next_chance,no_of_empty_cells)
            return_values.append(return_value)
        final_value_to_be_return="0 0"
        max_element_count=0
        max_element_cells=[]
        for i in range(no_of_empty_cells):
            if return_values[i]>=max(return_values)/2:
                max_element_count+=1
                max_element_cells.append(empty_cell_index[i])
            elif return_values[i]==max(return_values):
                max_element_count+=1
                max_element_cells.append(empty_cell_index[i])
        for i in range(no_of_empty_cells):
            if return_values[i]==max(return_values):
                row_value=int(empty_cell_index[i].split(" ")[0])+1
                column_value=int(empty_cell_index[i].split(" ")[1])+1
                final_value_to_be_return=f"{row_value} {column_value}"
        return final_value_to_be_return,max_element_cells,max_element_count,return_values

    def handleMaximumCount(self,state,max_element_cells,max_element_count):
        temp=[]
        for i in range(max_element_count):
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
        final_value_to_be_return=max_element_cells[0]
        for i in range(max_element_count):
            if temp[i]==max(temp):
                row_value=int(max_element_cells[i].split(" ")[0])+1
                column_value=int(max_element_cells[i].split(" ")[1])+1
                final_value_to_be_return=f"{row_value} {column_value}"
                break
        return final_value_to_be_return
    def find_huristic_value(self,state,chance,state_value):
        if (state[0][0]=="X" and state[0][1]=="X" and state[0][2]=="X") or (state[1][0]=="X" and state[1][1]=="X" and state[1][2]=="X") or (state[2][0]=="X" and state[2][1]=="X" and state[2][2]=="X") or (state[0][0]=="X" and state[1][0]=="X" and state[2][0]=="X") or (state[0][1]=="X" and state[1][1]=="X" and state[2][1]=="X") or (state[0][2]=="X" and state[1][2]=="X" and state[2][2]=="X") or (state[1][1]=="X" and state[0][0]=="X" and state[2][2]=="X") or (state[0][2]=="X" and state[1][1]=="X" and state[2][0]=="X"):
            return state_value
        if (state[0][0]=="O" and state[0][1]=="O" and state[0][2]=="O") or (state[1][0]=="O" and state[1][1]=="O" and state[1][2]=="O") or (state[2][0]=="O" and state[2][1]=="O" and state[2][2]=="O") or (state[0][0]=="O" and state[1][0]=="O" and state[2][0]=="O") or (state[0][1]=="O" and state[1][1]=="O" and state[2][1]=="O") or (state[0][2]=="O" and state[1][2]=="O" and state[2][2]=="O") or (state[1][1]=="O" and state[0][0]=="O" and state[2][2]=="O") or (state[0][2]=="O" and state[1][1]=="O" and state[2][0]=="O"):
            return -1*state_value
        empty_rows=0
        for i in range(3):
            for j in range(3):
                if state[i][j]=="_":
                    empty_rows+=1
        if empty_rows==0:
            return 0
        no_of_empty_cells=0
        empty_cell_index=[]
        for i in range(3):
            for j in range(3):
                if state[i][j]=="_":
                    no_of_empty_cells+=1
                    empty_cell_index.append(f"{i} {j}")
        returning_value=0
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
            returning_value=returning_value+self.find_huristic_value(new_state,chance+1,state_value-1)
        return returning_value

import platform
class Tic_Tak_Toe_GAME(A_star_Algorithm):
    
    current_condition = [
        ["_", "_", "_"],
        ["_", "_", "_"],
        ["_", "_", "_"]
    ]
    current_move =" "
    player_name = ""
    current_player=""
    valid_moves=[
        "1 1",
        "1 2",
        "1 3",
        "2 1",
        "2 2",
        "2 3",
        "3 1",
        "3 2",
        "3 3"
    ]
    remaining_conditions=[
        "1 1",
        "1 2",
        "1 3",
        "2 1",
        "2 2",
        "2 3",
        "3 1",
        "3 2",
        "3 3"
    ]

    def __init__(self):
        print("Created By : SHIVKUMAR CHAUHAN")
        print("""
                Welcome to Tic Tak Toe Game Using A* Algorithm
        """)
        self.player_name = input("Enter Your Name : ")
        print(f"""
Welcome {self.player_name} you are playing with {platform.system()}

O is yours and X is for {platform.system()}
""")
        print("""followings are possible inputs
                    _1 1_ | _1 2_ | _1 3_
                    _2 1_ | _2 2_ | _2 3_
                    _3 1_ | _3 2_ | _3 3_
""")
        print("initial Condition : ") 
        self.printSituation()
        i=0
        while i!=12:
            #user Input
            self.current_player=self.player_name
            print("time for user")
            self.takeInput()
            self.printSituation()
            isDone=self.checkSituation()
            if isDone==True:
                break

            #windows input
            self.current_player=platform.system()
            print("time for computer")
            print("Computer : Let Me think..........")
            self.computerPlayerInput()
            self.printSituation()
            print("Computer : Done, I have maked my Move")
            isDone=self.checkSituation()
            if isDone==True:
                break
            i+=1

    def printSituation(self):
        print()
        string=""
        for i in range(3):
            for j in range(3):
                string =string+"  "+self.current_condition[i][j]
            string=string+"\n"
        print(string)

    def checkSituation(self): 
        if (self.current_condition[0][0]=="X" and self.current_condition[0][1]=="X" and self.current_condition[0][2]=="X") or (self.current_condition[1][0]=="X" and self.current_condition[1][1]=="X" and self.current_condition[1][2]=="X") or (self.current_condition[2][0]=="X" and self.current_condition[2][1]=="X" and self.current_condition[2][2]=="X") or (self.current_condition[0][0]=="X" and self.current_condition[1][0]=="X" and self.current_condition[2][0]=="X") or (self.current_condition[0][1]=="X" and self.current_condition[1][1]=="X" and self.current_condition[2][1]=="X") or (self.current_condition[0][2]=="X" and self.current_condition[1][2]=="X" and self.current_condition[2][2]=="X") or (self.current_condition[1][1]=="X" and self.current_condition[0][0]=="X" and self.current_condition[2][2]=="X") or (self.current_condition[0][2]=="X" and self.current_condition[1][1]=="X" and self.current_condition[2][0]=="X"):
            print(f"*********** {self.current_player} Wins ***********")
            return True
        if (self.current_condition[0][0]=="O" and self.current_condition[0][1]=="O" and self.current_condition[0][2]=="O") or (self.current_condition[1][0]=="O" and self.current_condition[1][1]=="O" and self.current_condition[1][2]=="O") or (self.current_condition[2][0]=="O" and self.current_condition[2][1]=="O" and self.current_condition[2][2]=="O") or (self.current_condition[0][0]=="O" and self.current_condition[1][0]=="O" and self.current_condition[2][0]=="O") or (self.current_condition[0][1]=="O" and self.current_condition[1][1]=="O" and self.current_condition[2][1]=="O") or (self.current_condition[0][2]=="O" and self.current_condition[1][2]=="O" and self.current_condition[2][2]=="O") or (self.current_condition[1][1]=="O" and self.current_condition[0][0]=="O" and self.current_condition[2][2]=="O") or (self.current_condition[0][2]=="O" and self.current_condition[1][1]=="O" and self.current_condition[2][0]=="O"):
            print(f"*********** {self.current_player} Wins ***********")
            return True
        empty_rows=0
        for i in range(3):
            for j in range(3):
                if self.current_condition[i][j]=="_":
                    empty_rows+=1
        if empty_rows==0:
            print(f"######### Game Drawn #########")
            return True
        return False

    def computerPlayerInput(self):
        self.current_move=self.A_Star_Decision(self.current_condition,"X",1)
        self.current_move,max_element_cells,max_element_count,return_values=self.A_Star_Decision(self.current_condition,"X",1)
        if max_element_count>1:
            self.current_move=self.handleMaximumCount(self.current_condition,max_element_cells,max_element_count)
        if self.current_move in self.valid_moves:
            if self.current_move in self.remaining_conditions:
                try:
                    Condition1=int(self.current_move.split(" ")[0])
                    Condition2=int(self.current_move.split(" ")[1])
                    self.current_condition[Condition1-1][Condition2-1]="X"
                    self.remaining_conditions.remove(self.current_move)
                except Exception as exception:
                    print(exception)
            else:
                print("This condition is already taken")
        else:
            print("Please Enter valid Condition")

    def takeInput(self):
        is_correctMove=False
        while is_correctMove==False:
            self.current_move=input(f"{self.current_player} please Enter your move : ")
            if self.current_move in self.valid_moves:
                if self.current_move in self.remaining_conditions:
                    try:
                        Condition1=int(self.current_move.split(" ")[0])
                        Condition2=int(self.current_move.split(" ")[1])
                        self.current_condition[Condition1-1][Condition2-1]="O"
                        self.remaining_conditions.remove(self.current_move)
                        is_correctMove=True
                    except Exception as exception:
                        print(exception)
                else:
                    print("This move is already taken")
            else:
                print("Please Enter valid move")
        
if __name__=="__main__":
    game = Tic_Tak_Toe_GAME()

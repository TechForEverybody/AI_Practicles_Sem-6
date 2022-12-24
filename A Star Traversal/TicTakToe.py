import platform
import A_Star_Algorithm_For_Tic_Tac_Toe
class Tic_Tak_Toe_GAME:
    
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
            # else:
            #     print("continue playing ....")


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
            # else:
            #     print("continue playing ....")
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
        # winning condition
        if (self.current_condition[0][0]=="X" and self.current_condition[0][1]=="X" and self.current_condition[0][2]=="X") or (self.current_condition[1][0]=="X" and self.current_condition[1][1]=="X" and self.current_condition[1][2]=="X") or (self.current_condition[2][0]=="X" and self.current_condition[2][1]=="X" and self.current_condition[2][2]=="X") or (self.current_condition[0][0]=="X" and self.current_condition[1][0]=="X" and self.current_condition[2][0]=="X") or (self.current_condition[0][1]=="X" and self.current_condition[1][1]=="X" and self.current_condition[2][1]=="X") or (self.current_condition[0][2]=="X" and self.current_condition[1][2]=="X" and self.current_condition[2][2]=="X") or (self.current_condition[1][1]=="X" and self.current_condition[0][0]=="X" and self.current_condition[2][2]=="X") or (self.current_condition[0][2]=="X" and self.current_condition[1][1]=="X" and self.current_condition[2][0]=="X"):
            print(f"*********** {self.current_player} Wins ***********")
            return True

        # loosing condition
        if (self.current_condition[0][0]=="O" and self.current_condition[0][1]=="O" and self.current_condition[0][2]=="O") or (self.current_condition[1][0]=="O" and self.current_condition[1][1]=="O" and self.current_condition[1][2]=="O") or (self.current_condition[2][0]=="O" and self.current_condition[2][1]=="O" and self.current_condition[2][2]=="O") or (self.current_condition[0][0]=="O" and self.current_condition[1][0]=="O" and self.current_condition[2][0]=="O") or (self.current_condition[0][1]=="O" and self.current_condition[1][1]=="O" and self.current_condition[2][1]=="O") or (self.current_condition[0][2]=="O" and self.current_condition[1][2]=="O" and self.current_condition[2][2]=="O") or (self.current_condition[1][1]=="O" and self.current_condition[0][0]=="O" and self.current_condition[2][2]=="O") or (self.current_condition[0][2]=="O" and self.current_condition[1][1]=="O" and self.current_condition[2][0]=="O"):
            print(f"*********** {self.current_player} Wins ***********")
            return True

        # draw condition
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
        A_star_Algorithm=A_Star_Algorithm_For_Tic_Tac_Toe.A_star_Algorithm()
        self.current_move=A_star_Algorithm.A_Star_Decision(self.current_condition,"X",1)
        self.current_move,max_element_cells,max_element_count,return_values=A_star_Algorithm.A_Star_Decision(self.current_condition,"X",1)
        if max_element_count>1:
            self.current_move=A_star_Algorithm.handleMaximumCount(self.current_condition,max_element_cells,max_element_count)
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


print("------ Welcome To Water Jug Problem's Space Tree Traversal Using BFS Technique ------")

Traversed_list = []
Goal_States=["2 0","2 1","2 2","2 3"]
goal_state_actions=[]
goal_state_path=[]
is_Reached_to_goal_state=False

def check_cases(node):
    global Traversed_list,goal_state_actions,goal_state_path,is_Reached_to_goal_state
    to_be_checked_states = []
    next_states = []
    if f"{node['current_state']['x']} {node['current_state']['y']}" in Traversed_list:
        # print("already traversed")
        return []
    
    if f"{node['current_state']['x']} {node['current_state']['y']}" in Goal_States:
        goal_state_actions.append(node['previous_path'])
        goal_state_path.append(node['previous_list']+[f"{node['current_state']['x']} {node['current_state']['y']}"])
        # print("already reached to goal state")
        Traversed_list.append(f"{node['current_state']['x']} {node['current_state']['y']}")
        is_Reached_to_goal_state=True
        return []
    
    if node['current_state']['x'] < 4:
        future_node = {
            'current_state': {
                'x': 4,
                'y': node['current_state']['y']
            },
            'previous_list': node['previous_list']+[(f"{node['current_state']['x']} {node['current_state']['y']}")],
            'previous_path': node['previous_path']+[1]
        }
        next_states.append(future_node)
        to_be_checked_states.append("full the 4 jug glass")
        to_be_checked_states.append(f"x-> {4}")
        to_be_checked_states.append(f"y-> {node['current_state']['y']}")
    if node['current_state']['y'] < 3:
        future_node = {
            'current_state': {
                'x': node['current_state']['x'],
                'y': 3
            },
            'previous_list': node['previous_list']+[(f"{node['current_state']['x']} {node['current_state']['y']}")],
            'previous_path': node['previous_path']+[2]
        }
        next_states.append(future_node)
        to_be_checked_states.append("full the 3 jug glass")
        to_be_checked_states.append(f"x-> {node['current_state']['x']}")
        to_be_checked_states.append(f"y-> {3}")
    if node['current_state']['x'] > 0:
        future_node = {
            'current_state': {
                'x': 0,
                'y': node['current_state']['y']
            },
            'previous_list': node['previous_list']+[(f"{node['current_state']['x']} {node['current_state']['y']}")],
            'previous_path': node['previous_path']+[3]
        }
        next_states.append(future_node)
        to_be_checked_states.append("empty the 4 jug glass")
        to_be_checked_states.append(f"x-> {0}")
        to_be_checked_states.append(f"y-> {node['current_state']['y']}")
    if node['current_state']['y'] > 0:
        future_node = {
            'current_state': {
                'x': node['current_state']['x'],
                'y': 0
            },
            'previous_list': node['previous_list']+[(f"{node['current_state']['x']} {node['current_state']['y']}")],
            'previous_path': node['previous_path']+[4]
        }
        next_states.append(future_node)
        to_be_checked_states.append("empty the 3 jug glass")
        to_be_checked_states.append(f"x-> {node['current_state']['x']}")
        to_be_checked_states.append(f"y-> {0}")

    if (node['current_state']['y'] + node['current_state']['x']) >= 4 and node['current_state']['y'] > 0 and node['current_state']['x'] < 4:
        future_node = {
            'current_state': {
                'x': 4,
                'y': node['current_state']['y'] - (4 - node['current_state']['x'])
            },
            'previous_list': node['previous_list']+[(f"{node['current_state']['x']} {node['current_state']['y']}")],
            'previous_path': node['previous_path']+[5]
        }
        next_states.append(future_node)
        to_be_checked_states.append("full the 4 jug using 3 jug")
        to_be_checked_states.append(f"x-> {4}")
        to_be_checked_states.append(f"y-> {node['current_state']['y'] - (4 - node['current_state']['x'])}")

    if (node['current_state']['y'] + node['current_state']['x']) >= 3 and node['current_state']['x'] > 0 and node['current_state']['y'] < 3:
        future_node = {
            'current_state': {
                'x': node['current_state']['x'] - (3 - node['current_state']['y']),
                'y': 3
            },
            'previous_list': node['previous_list']+[(f"{node['current_state']['x']} {node['current_state']['y']}")],
            'previous_path': node['previous_path']+[6]
        }
        next_states.append(future_node)
        to_be_checked_states.append("full the 3 jug using 4 jug")
        to_be_checked_states.append(f"x-> {node['current_state']['x'] - (3 - node['current_state']['y'])}")
        to_be_checked_states.append(f"y-> {3}")
    if (node['current_state']['y'] + node['current_state']['x']) <= 4 and node['current_state']['y'] > 0 and node['current_state']['x'] < 4:
        future_node = {
            'current_state': {
                'x': node['current_state']['y'] + node['current_state']['x'],
                'y': 0
            },
            'previous_list': node['previous_list']+[(f"{node['current_state']['x']} {node['current_state']['y']}")],
            'previous_path': node['previous_path']+[7]
        }
        next_states.append(future_node)
        to_be_checked_states.append("pour the 4 jug using 3 jug")
        to_be_checked_states.append(f"x-> {node['current_state']['y'] + node['current_state']['x']}")
        to_be_checked_states.append(f"y-> {0}")

    if (node['current_state']['y'] + node['current_state']['x']) <= 3 and node['current_state']['x'] > 0 and node['current_state']['y'] < 3:
        future_node = {
            'current_state': {
                'x': 0,
                'y': node['current_state']['y'] + node['current_state']['x']
            },
            'previous_list': node['previous_list']+[(f"{node['current_state']['x']} {node['current_state']['y']}")],
            'previous_path': node['previous_path']+[8]
        }
        next_states.append(future_node)
        to_be_checked_states.append("pour the 3 jug using 4 jug")
        to_be_checked_states.append(f"x-> {0}")
        to_be_checked_states.append(f"y-> {node['current_state']['y'] + node['current_state']['x']}")
    Traversed_list.append(f"{node['current_state']['x']} {node['current_state']['y']}")

    # print(next_states)
    # print(Traversed_list)
    # print("\n".join(to_be_checked_states))
    return next_states



def main():
    global Traversed_list,is_Reached_to_goal_state
    node = {
        'current_state': {
            'x': 0,
            'y': 0
        },
        'previous_list': [],
        'previous_path': []
    }
    next_to_be_traversed_states=check_cases(node)
    counter=0
    while counter !=50 and len(next_to_be_traversed_states)!=0 :
        counter=+1
        # print(next_to_be_traversed_states)
        tempTraveresedState=[]
        for state in next_to_be_traversed_states:
            tempTraveresedState+=check_cases(state)
        next_to_be_traversed_states=tempTraveresedState
    # print(next_to_be_traversed_states)
    # tempTraveresedState=[]
    # for state in next_to_be_traversed_states:
    #     tempTraveresedState+=check_cases(state)
    # next_to_be_traversed_states=tempTraveresedState
    # print(next_to_be_traversed_states)
    # tempTraveresedState=[]
    # for state in next_to_be_traversed_states:
    #     tempTraveresedState+=check_cases(state)
    # next_to_be_traversed_states=tempTraveresedState
    # print(next_to_be_traversed_states)
    # tempTraveresedState=[]
    # for state in next_to_be_traversed_states:
    #     tempTraveresedState+=check_cases(state)
    # next_to_be_traversed_states=tempTraveresedState
    # print(next_to_be_traversed_states)
    # tempTraveresedState=[]
    # for state in next_to_be_traversed_states:
    #     tempTraveresedState+=check_cases(state)
    # next_to_be_traversed_states=tempTraveresedState
    # print(next_to_be_traversed_states)
    # tempTraveresedState=[]
    # for state in next_to_be_traversed_states:
    #     tempTraveresedState+=check_cases(state)
    # print(tempTraveresedState)
    # for i in next_to_be_traversed_states:
    #     print(i)
    print("Travesal Order is as follows : ")
    # print(goal_state_path)
    # print(goal_state_actions)
    # print("   ",end="")
    print('''
    CONDITIONS are :
1. full the 4 liter jug 
2. full the 3 liter jug 
3. empty the 4 liter jug 
4. empty the 3 liter jug 
5. full the 4 jug using 3 jug
6. full the 3 jug using 4 jug
7. pour all water from 3 jug to 4 jug
8. pour all water from 4 jug to 3 jug
    ''')
    print("1. List of respective Actions :")
    for actions in goal_state_actions:
        # print(actions)
        print((" --> ".join([str(i) for i in actions])))
    print()
    print()
    print("1. List of respective Paths :")
    for path in goal_state_path:
        print((" --> ".join(path)))
    # print(Traversed_list)


if __name__ == "__main__":
    main()

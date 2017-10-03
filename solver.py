import rubik
import Queue

def shortest_path(start, end):
    # return the amount of moves that need to be made
    moves = []

    # outlines the possible turns from runbik.py
    poss_turns = [rubik.F, rubik.Fi,
                 rubik.L, rubik.Li,
                 rubik.U, rubik.Ui]

    # they are the same
    if(start == end):
        # returns nothing becasue the first and second are the same
        return moves
    
    # The following loop is going to iterate through the nodes
    # and determine how many moves need to be applied to moves[]
    for i in range (0,len(poss_turns)):
        path_one = rubik.perm_apply(poss_turns[i], start)
        # only one turn is needed
        if path_one == end:

            # loop invarience:
            # start[i] is equal to one turn of F, L, or U
            # for all values that are equal to one turn
            # Maintaince: the moves gets added to the list of moves
            # Termination: the loop will return the list of required moves

            moves.append(poss_turns[i])
            return moves

        # Two or more are needed
        else:
            print "This is a test for testing purposes"

            # get the 6 rotations from the start pos and the next 5 paths for each rotation

            # get the 6 rotations from the end pos and the next 5 paths for each rotation

            # check to see if the frontiers contain the same config

            # if they do return

            # otherwise build out 5 more configs from each path

            # check again to see if there is a match

            # repeat until a match is found

    """
    Using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves. 
    You can use the rubik.quarter_twists move set.
    Each move can be applied using rubik.perm_apply
    """
    raise NotImplementedError

def bfs(root, goal):
    checked = []
    queue = Queue()

    checked.append(root)
    queue.enqueue(root)

    while not Queue.empty:
        current = Queue.deque()
        if current.has(goal):
            return current

    print "test"

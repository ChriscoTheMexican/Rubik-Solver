import rubik
import Queue

start_frontier = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
end_frontier = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}

def shortest_path(start, end):
    # return the amount of moves that need to be made
    moves = []

    # outlines the possible turns from runbik.py
    poss_turns = [rubik.F, rubik.Fi,
                  rubik.L, rubik.Li,
                  rubik.U, rubik.Ui]

    # they are the same
    if(start == end):
        # returns nothing because the first and second are the same
        return moves
    
    # The following loop is going to iterate through the nodes
    # and determine how many moves need to be amplified to moves[]
    for i in range(0, len(poss_turns)):

        path_from_start = rubik.perm_apply(poss_turns[i], start)
        start_frontier[i] = path_from_start

        # only one turn is needed
        if path_from_start == end:

            # loop invariance:
            # start[i] is equal to one turn of F, L, or U
            # for all values that are equal to one turn
            # Maintenance: the moves gets added to the list of moves
            # Termination: the loop will return the list of required moves

            moves.append(poss_turns[i])
            return moves
        # Two or more are needed
        else:
            path_from_end = rubik.perm_apply(poss_turns[i], end)
            end_frontier[i] = path_from_end

        print "\nStart: "
        print start_frontier
        print "End: "
        print end_frontier
        print "\n"

    # raise NotImplementedError

def bfs(root, goal):
    checked = []
    queue = Queue()

    """
     Using 2-way BFS, finds the shortest path from start_position to
     end_position. Returns a list of moves. 
     You can use the rubik.quarter_twists move set.
     Each move can be applied using rubik.perm_apply
     """

    checked.append(root)
    queue.enqueue(root)

    while not Queue.empty:
        current = Queue.deque()
        if current.has(goal):
            return current

    print "test"

import rubik
import Queue

def shortest_path(start, end):
    moves = []

    poss_turns = [rubik.F, rubik.Fi,
                  rubik.L, rubik.Li,
                  rubik.U, rubik.Ui]

    # they are the same
    if (start == end):
        return moves

    # one off
    for i in range(0, len(poss_turns)):
        path_one = rubik.perm_apply(poss_turns[i], start)
        if path_one == end:
            moves.append(poss_turns[i])
            return moves

        # more than two off
        else:
            print "Test"

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

def check_for_match():
    print "Checking for matches"

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
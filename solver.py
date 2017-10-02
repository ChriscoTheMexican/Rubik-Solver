import rubik
import Queue

def shortest_path(start, end):

    moves = []

    if(start == end):
        return

    nodes = [rubik.F, rubik.Fi,
             rubik.L, rubik.Li,
             rubik.U, rubik.Ui]

    for i in nodes:
        if start + nodes[i] == end:
            return

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
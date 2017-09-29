import rubik
import Queue


def shortest_path(start, end):
    checked = []
    queue = Queue()
    checked.append(start)
    queue.enqueue(start)


    while not queue.empty:
        current = queue.dequeue
        if current.has(end):
            return current
          
    
    
    


    
    """
    Using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves. 

    You can use the rubik.quarter_twists move set.
    Each move can be applied using rubik.perm_apply
    """
    raise NotImplementedError



    

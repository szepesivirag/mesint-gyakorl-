import heapq

def bfs( graph, start, goal):
    queue= []
    queue.append([start])

    while queue:
        path = queue.pop(0)
        end_node = path[-1]

        if end_node == goal:
            return path
        for adjacent in graph.get(end_node, []):
            if adjacent not in path:
                new_path = list(path) + [adjacent]
                queue.append(new_path)
    return None

def dfs(graph , start, goal):
    queue= []
    queue.append([start])

    while queue:
        path = queue.pop(0)
        end_node = path[-1]

        if end_node == goal:
            return path
        for adjacent in graph.get(end_node, []):
            if adjacent not in path:
                new_path = list(path) + [adjacent]
                queue.insert(0, new_path)
    return None


def hill_climbing( graph , start, goal , herusitic):
    queue= []
    queue.append[start]

    while queue:
        path = queue.pop(0)
        end_node = path[-1]

        if end_node == goal:
            return path 
        
        neighbours = graph.get(end_node, [])
        neighbours.sort( key = lambda node : herusitic[node])

        for adjacent in neighbours:
            if adjacent not in path:
                new_path = list(path) + [adjacent]
                queue.insert(0, new_path)
    return None


def beam_search( graph , start, goal ,heuristic, beam_width):
    queue=[[start]]

    while queue:
        beam = queue[:beam_width]
        queue = queue[beam_width:]

        for path in beam:
            end_node = path[-1]
            if end_node == goal :
                return path
            
    neighbours = graph.get(end_node, [])
    neighbours.sort(key = lambda node: heuristic[node])

    for adjacent in neighbours:
        if adjacent not in path:
            new_path = path + [adjacent]
            queue.append(new_path)
    queue.sort(key= lambda path: heuristic[path[-1]])

    return None



def Branch_n_bound( graph, start, goal):
    queue= [[start]]
    visited= set()

    while queue:
        cost, path = heapq.heappop(queue)
        node = path[-1]
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)

        for adjacent ,weight in graph[node].items():
            if adjacent not in path:
                new_cost= cost + weight
                new_path = path + [adjacent]
                heapq.heappush(queue(new_cost,new_path))
    return None

def branch_n_bound_w_heu(graph, start, goal, heuristic):
    queue=[[start]]
    visited = set()

    while queue:
        cost, path = heapq.heappop(queue)
        node = path[-1]

        if node == goal:
            return path 
        if node not in visited:
            visited.add(node)

        for adjacent, weight in graph[node].items():
            if adjacent not in path:
                new_cost = cost + weight
                new_path = path +[adjacent]
                estimated_cost= new_cost + heuristic[adjacent]
                heapq.heappush(queue(estimated_cost, new_path))
    return None


def a_start( graph, start, goal, heuristic):
    queue = [[start]]
    visited=set()

    while queue:
        f, g, path= heapq.heappop(queue)
        node = path[-1]
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
        for adjacent , weight in graph[node].items():
            if adjacent not in path:
                new_g = g + weight
                new_f = g + heuristic[adjacent]
                new_path = path + [adjacent]
                heapq.heappush(queue(new_f, new_g, new_path))
    return None







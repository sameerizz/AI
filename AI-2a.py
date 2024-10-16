# Program 2A: Write a program to implement A* Search Algorithm

import heapq

def a_star_search(graph, start, goal, h):
    # Initialize the frontier with the start node and its priority
    frontier = [(0, start)]
    # Keep track of the cost to reach each node
    g_costs = {start: 0}
    # Store the parent of each node for path reconstruction
    parent = {start: None}
    
    while frontier:
        # Get the node with the lowest f_cost from the frontier
        current_cost, current_node = heapq.heappop(frontier)
        
        # If we've reached the goal, construct and return the path
        if current_node == goal:
            return construct_path(parent, start, goal)
        
        # Explore neighbors of the current node
        for neighbor, cost in graph[current_node]:
            # Calculate the new g_cost to reach the neighbor
            new_g_cost = g_costs[current_node] + cost
            # If we've found a better path to the neighbor
            if neighbor not in g_costs or new_g_cost < g_costs[neighbor]:
                # Update the g_cost for the neighbor
                g_costs[neighbor] = new_g_cost
                # Calculate the f_cost (g_cost + heuristic)
                f_cost = new_g_cost + h(neighbor, goal)
                # Add the neighbor to the frontier with its f_cost
                heapq.heappush(frontier, (f_cost, neighbor))
                # Update the parent of the neighbor
                parent[neighbor] = current_node
    
    # If we've exhausted all nodes without finding the goal, return None
    return None

def construct_path(parent, start, goal):
    # Initialize the path with the goal node
    path, current = [], goal
    # Traverse backwards from goal to start
    while current is not None:
        path.append(current)
        current = parent[current]
    # Reverse the path to get it from start to goal
    return path[::-1]

def heuristic(node, goal):
    # Simple heuristic: absolute difference between ASCII values of node and goal
    return abs(ord(node) - ord(goal))

# Define the graph structure with nodes and edge costs
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 5), ('E', 2)],
    'C': [('F', 1)],
    'D': [],
    'E': [('F', 3)],
    'F': []
}

# Set the start and goal nodes
start_node, goal_node = 'A', 'F'
# Run A* search and print the result
print("A* Path:", a_star_search(graph, start_node, goal_node, heuristic))
# Program 2B: Write a program to implement Recursive Best-First Search (RBFS) Algorithm

import math

def construct_path(parent, start, goal):
    # Initialize an empty path
    path = []
    # Start from the goal node
    current = goal
    # Traverse backwards until we reach the start node
    while current is not None:
        # Add the current node to the path
        path.append(current)
        # Move to the parent of the current node
        current = parent[current]
    # Reverse the path to get it from start to goal
    return path[::-1]

def rbfs(graph, current, goal, f_cost, g_costs, h, limit, parent):
    # Check if we've reached the goal
    if current == goal:
        # If so, construct and return the path along with its cost
        return construct_path(parent, current, goal), f_cost
    
    # Get the neighbors of the current node
    neighbors = graph[current]
    # If there are no neighbors, return failure
    if not neighbors:
        return None, math.inf
    
    # Initialize list to store successor nodes
    successors = []
    for neighbor, cost in neighbors:
        # Calculate the g_cost for the neighbor
        g_cost = g_costs[current] + cost
        # Calculate the f_value for the neighbor
        f_value = max(f_cost, g_cost + h(neighbor, goal))
        # Add the neighbor to the successors list
        successors.append((f_value, neighbor))
        # Update the g_cost for the neighbor
        g_costs[neighbor] = g_cost
        # Set the parent of the neighbor
        parent[neighbor] = current
    
    # Main loop of RBFS
    while successors:
        # Sort successors based on their f_values
        successors.sort()
        # Get the best successor
        best_f, best_node = successors[0]
        # If the best f_value exceeds the limit, return failure
        if best_f > limit:
            return None, best_f
        
        # Get the f_value of the second-best successor
        alternative_f = successors[1][0] if len(successors) > 1 else math.inf
        # Recursively search from the best node
        result, new_f = rbfs(graph, best_node, goal, best_f, g_costs, h, min(limit, alternative_f), parent)
        
        # If a path is found, return it
        if result is not None:
            return result, new_f
        
        # Update the f_value of the best node
        successors[0] = (new_f, best_node)
    
    # If all successors have been explored without finding a path, return failure
    return None, math.inf

def rbfs_search(graph, start, goal, h):
    # Initialize the f_cost with the heuristic value of the start node
    f_cost = h(start, goal)
    # Initialize g_costs dictionary with the start node
    g_costs = {start: 0}
    # Initialize parent dictionary with the start node
    parent = {start: None}
    # Call the recursive RBFS function
    return rbfs(graph, start, goal, f_cost, g_costs, h, math.inf, parent)[0]

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

# Run RBFS search and print the result
print("RBFS Path:", rbfs_search(graph, start_node, goal_node, heuristic))

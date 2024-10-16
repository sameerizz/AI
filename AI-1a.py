# Program 1A: Write a program to implement Breadth-First Search (BFS) Algorithm
from collections import deque

def bfs(graph, start, goal):
    queue = deque([start])  # Initialize queue with start node
    visited = set()  # Set to keep track of visited nodes
    parent = {start: None}  # Dictionary to store parent nodes for path reconstruction
    
    while queue:
        node = queue.popleft()  # Get the next node from the queue
        
        if node == goal:
            return construct_path(parent, start, goal)  # If goal is found, construct and return the path
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)  # Mark the neighbor as visited
                parent[neighbor] = node  # Set the current node as the parent of the neighbor
                queue.append(neighbor)  # Add the neighbor to the queue
                
    return None  # Return None if no path is found

def construct_path(parent, start, goal):
    path = []
    current = goal
    
    while current is not None:
        path.append(current)  # Add the current node to the path
        current = parent[current]  # Move to the parent node
    
    path.reverse()  # Reverse the path to get it from start to goal
    return path

# Define the graph structure
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_node = 'A'  # Define the start node
goal_node = 'F'  # Define the goal node
print("Breadth First Search:", bfs(graph, start_node, goal_node))  # Run BFS and print the result
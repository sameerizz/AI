# Program 1B: Write a program to implement Iterative Deepening Depth-First Search (IDDFS) Algorithm

# Iterative Depth-First Search function
def iterative_dfs(graph, start, goal):
    stack, visited, parent = [start], set(), {start: None}
    while stack:
        node = stack.pop()  # Get the next node from the stack
        if node == goal:
            return construct_path(parent, start, goal)  # Path found, construct and return it
        if node not in visited:
            visited.add(node)  # Mark the node as visited
            # Add unvisited neighbors to the stack
            stack.extend(neighbor for neighbor in graph[node] if neighbor not in visited)
            # Update parent information for path reconstruction
            for neighbor in graph[node]:
                if neighbor not in visited:
                    parent[neighbor] = node
    return None  # No path found

# Function to construct the path from start to goal
def construct_path(parent, start, goal):
    path, current = [], goal
    while current is not None:
        path.append(current)  # Add current node to the path
        current = parent[current]  # Move to the parent node
    return path[::-1]  # Reverse the path to get start-to-goal order

# Define the graph structure
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Set start and goal nodes
start_node, goal_node = 'A', 'F'

# Perform the search
path = iterative_dfs(graph, start_node, goal_node)

# Print the result
print("Iterative DFS Path:", path if path else f"No path found from {start_node} to {goal_node}")
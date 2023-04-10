# source = "/home/parthag/mech_ws/src/mp_controls/scripts/test_maze.jpg"
# width, height = 0, 0  # they are given values later

# # start = (4, 190)
# # end = (388, 190)

# start = (550, 343)
# end = (18, 343)


# ############################################ convert image to array ###################################################

# from PIL import Image

# img = Image.open(source).convert("1")

# pixels = list(img.getdata())
# width, height = img.size
# pixels = [pixels[i:i+width] for i in range(0, len(pixels), width)]

# import numpy as np

# data_array = np.array([[1 if p > 127 else 0 for p in row] for row in pixels])

# ################################################### the alg ############################################################
# import heapq

# def heuristic(a, b):    
#     return np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# def astar(maze, start, end):
#     open_nodes = []
#     heapq.heappush(open_nodes, (0, start))
#     closed_nodes = set()
#     parents = {}
#     parents[start] = None
#     cost_so_far = {}
#     cost_so_far[start] = 0

#     while len(open_nodes) > 0:
#         current = heapq.heappop(open_nodes)[1]
#         if current == end:
#             path = []
#             while current in parents:
#                 path.append(current)
#                 current = parents[current]
#             path.reverse()
#             return path
#         closed_nodes.add(current)
#         for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
#             neighbor = (current[0]+dx, current[1]+dy)
#             if neighbor[0] < 0 or neighbor[0] >= maze.shape[0] or neighbor[1] < 0 or neighbor[1] >= maze.shape[1]:
#                 continue
#             if maze[neighbor] == 0:
#                 continue
#             if neighbor in closed_nodes:
#                 continue
#             new_cost = cost_so_far[current] + heuristic(current, neighbor)
#             if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
#                 cost_so_far[neighbor] = new_cost
#                 priority = new_cost + heuristic(end, neighbor)
#                 heapq.heappush(open_nodes, (priority, neighbor))
#                 parents[neighbor] = current

#     return None

# if __name__ == '__main__':
#     maze = data_array
#     end = (maze.shape[0]-1, maze.shape[1]-1)
#     path = astar(maze, start, end)
#     if path is not None:
#         path_coords = [(node[1], node[0]) for node in path]
#         path_array = np.zeros_like(maze)
#         for node in path:
#             path_array[node] = 1
#         try:
#             with open('/home/parthag/mech_ws/src/mp_controls/scripts/my_maze_solved.csv', 'w') as f:
#                 f.write('x,y\n')
#                 for i, coord in enumerate(path_coords):
#                     f.write(f'{coord[0]},{600 - coord[1]}\n')
#         except Exception as e:
#             print('Error saving path array:', e)
#         print(path_array)
#     else:
#         print('No path found from start to end.')



source = "/home/parthag/mech_ws/src/mp_controls/scripts/test_maze.jpg"
width, height = 0, 0  # they are given values later
# start = (400 - 350, 600 - 580)
# end = (400 - 350, 600 - 26)

# print(start, end)

start = (48, 326)
end = (550, 300)

############################################ convert image to array ###################################################


from PIL import Image

img = Image.open(source).convert("1")

pixels = list(img.getdata())
width, height = img.size
pixels = [pixels[i:i+width] for i in range(0, len(pixels), width)]

import numpy as np

data_array = np.array([[1 if p > 127 else 0 for p in row] for row in pixels])

################################################### the alg ############################################################
import heapq

def heuristic(a, b):    
    return np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def astar(maze, start, end):
    open_nodes = []
    heapq.heappush(open_nodes, (0, start))
    closed_nodes = set()
    parents = {}
    parents[start] = None
    cost_so_far = {}
    cost_so_far[start] = 0

    while len(open_nodes) > 0:
        current = heapq.heappop(open_nodes)[1]
        if current == end:
            path = []
            while current in parents:
                path.append(current)
                current = parents[current]
            path.reverse()
            return path
        closed_nodes.add(current)
        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            neighbor = (current[0]+dx, current[1]+dy)
            if neighbor[0] < 0 or neighbor[0] >= maze.shape[0] or neighbor[1] < 0 or neighbor[1] >= maze.shape[1]:
                continue
            if maze[neighbor] == 0:
                continue
            if neighbor in closed_nodes:
                continue
            new_cost = cost_so_far[current] + heuristic(current, neighbor)
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(end, neighbor)
                heapq.heappush(open_nodes, (priority, neighbor))
                parents[neighbor] = current

    return None

if __name__ == '__main__':
    maze = data_array
    path = astar(maze, start, end)
    if path is not None:
        path_coords = [(node[1], node[0]) for node in path]
        path_array = np.zeros_like(maze)
        for node in path:
            path_array[node] = 1
        try:
            with open('/home/parthag/mech_ws/src/mp_controls/scripts/my_maze_solved.csv', 'w') as f:
                f.write('x,y\n')
                for i, coord in enumerate(path_coords):
                    f.write(f'{coord[0]},{600 - coord[1]}\n')
        except Exception as e:
            print('Error saving path array:', e)
        print(path_array)

        # # Visualize the path using Plotly
        # import plotly.graph_objects as go

        # # Define the maze as a heatmap
        # maze_heatmap = go.Heatmap(z=maze, colorscale=[[0, 'white'], [1, 'black']])

        # # Define the path as a scatter plot
        # x_coords, y_coords = np.where(path_array == 1)
        # path_scatter = go.Scatter(x=y_coords, y=x_coords, mode='markers', marker=dict(color='red'))

        # # Create the plot
        # fig = go.Figure(data=[maze_heatmap, path_scatter])

        # # Set the axis labels
        # fig.update_layout(xaxis_title='X', yaxis_title='Y')

        # # Show the plot
        # fig.show()

    else:
        print('No path found from start to end.')


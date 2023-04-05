import pandas as pd 

df = pd.read_csv("my_maze_solved.csv")

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        raise TypeError('unsupported operand type(s) for -: {} and {}'.format(type(self), type(other)))


edges = []

for i in range(2, df.shape[0]-2):
    prev_pos = Vector(df.iloc[i-1, 0], df.iloc[i-1, 1])
    current_pos = Vector(df.iloc[i, 0], df.iloc[i, 1])
    next_pos = Vector(df.iloc[i+1, 0], df.iloc[i+1, 1])

    vec1 = current_pos - prev_pos
    vec2 = next_pos - current_pos

    if not (vec1 == vec2):
        edges.append(current_pos)

for i in edges:
    print(i.x, i.y)

with open('output_array.csv', 'w') as f:
    for i in edges:
        f.write(f"{i.x},{i.y}\n")
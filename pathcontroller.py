'''
takes the output from the A* algorithm in path.txt, then converts the data
into readable instructions that is processablie in main.py.
'''


#read path.txt and extract data into array
path = []
with open("path.txt", "r") as f:
    data=f.readlines()
    for line in data:
        numbers = line.split()
        path.append( (int(numbers[0]), int(numbers[1])) )

#reverse the path to read from beginning to end
path.reverse()

#create the instructions in two arrays. One is the direction, the other is the distance
cur_dist = 0
cur_dir = "na"
directions = []
distances = []
instructions = []

#dictionary to translate pixel tranformation to directions
translation = {(1,-1):"ne", (1,0):"e", (1,1):"se", (0,1):"s", (-1,1):"sw", (-1,0):"w", (-1,-1):"nw", (0,-1):"n"}

for i in range(1, len(path)):
    transform = (path[i][0] - path[i-1][0],path[i][1]-path[i-1][1])
    direction = translation[transform]
    if not cur_dir == direction:
        directions.append(direction)
        cur_dir = direction
        if not (i == 1):
            if(cur_dist == 0):
                print("hi")
                print(directions[len(directions)-2])
                del directions[len(directions)-2]
            else:
                distances.append(cur_dist + 1)
                cur_dist = 0
    else:
        cur_dist+=1

if not cur_dist == 0:
    distances.append(cur_dist+1)
else:
    del directions[len(directions)-1]

for i in range(0,len(directions)):
    instructions.append((directions[i], str(distances[i])))

print(instructions)

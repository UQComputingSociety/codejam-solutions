# The directions of the leg of the T (i.e normal T has leg direction = DOWN)
from re import I


DOWN = 0
LEFT = 1
UP = 2
RIGHT = 3
DIRECTIONS = [DOWN, LEFT, UP, RIGHT]

# Function to return a list containing 3 lists of 2 point (row,col) coord tuples representing the positions of the 
# top/left and bottom/right elements of the 3 electorate rectangles
# 
# Note: Use map_data[row][col] to acces points from coords

MIN_HEIGHT = 4
MIN_WIDTH = 4


def get_electorate_percentage(map_data, corners, desired_party):
    good = 0
    bad = 0
    for row in range(corners[0][0], corners[1][0]+1):
        # print("foo")
        for col in range(corners[0][1], corners[1][1]+1):
            # print("bar")
            voter = map_data[row][col]
            if voter == desired_party:
                # add to my team
                good = good+1
                # print(good)
            else:
                # add to other team
                bad = bad+1
    # print(corners)
    # print(good)
    percentage = good / (good+bad)
    return percentage


def get_value(a, b, c):
    # Want a situation where you win 2 electorates
    
    sizes = [a[1], b[1], c[1]]
    percentages = [a[0], b[0], c[0]]
    # print(percentages)

    wins = 0
    if percentages[0] > 0.5:
        wins = wins + 1
    if percentages[1] > 0.5:
        wins = wins + 1
    if percentages[2] > 0.5:
        wins = wins + 1
    if wins < 2:
        return -1
    else:
        # If we are winning get the electorates sizes
        min_item = percentages[0]
        min_index = 0
        for i in range(1, len(percentages)):
            item = percentages[i]
            if item < min_item:
                min_item = item
                min_index = i
        
        value = sizes[0] + sizes[1] + sizes[2]
        value = value - sizes[min_index]
    return value


# Get input data from command line input
def get_data_cli():
    input_data = input().strip()
    return input_data

# Get input data from txt file
def get_data_file(filepath):
    with open(filepath) as f:
        input_data = f.read()
    f.close()
    return input_data

def get_electorates(map_data):
    out = list() # a list of all the pairs of foods and their prices that sum to N

    corners_a = [(-1,-1), (-1,-1)]
    corners_b = [(-1,-1), (-1,-1)]
    corners_c = [(-1,-1), (-1,-1)]
    best_corners = [corners_a, corners_b, corners_c]
    best_value = 0

    # For each posiiton
    for direction in DIRECTIONS:
        corners_a[0] = (0, 0)
        
        if direction == DOWN:
            for head_gap in range(MIN_HEIGHT, 15-MIN_HEIGHT+1):
                corners_a[1] = (head_gap-1, 14)
                corners_b[0] = (head_gap, 0)
                for leg_lead in range(MIN_WIDTH, 15-MIN_WIDTH+1):
                    # Do stuff
                    # Now we have established the head gap and the leg lead values, lets do the corners
                    corners_b[1] = (14, leg_lead-1)
                    corners_c[0] = (head_gap, leg_lead)
                    corners_c[1] = (14, 14)

                    # Check the contents of the electorates
                    a_percentage = get_electorate_percentage(map_data, corners_a, "Y")
                    b_percentage = get_electorate_percentage(map_data, corners_b, "Y")
                    c_percentage = get_electorate_percentage(map_data, corners_c, "Y")
                    a_size = (corners_a[1][0]-corners_a[0][0]+1) * (corners_a[1][1]-corners_a[0][1]+1)
                    b_size = (corners_b[1][0]-corners_b[0][0]+1) * (corners_b[1][1]-corners_b[0][1]+1)
                    c_size = (corners_c[1][0]-corners_c[0][0]+1) * (corners_c[1][1]-corners_c[0][1]+1)

                    current_value = get_value([a_percentage, a_size], [b_percentage, b_size], [c_percentage, c_size])

                    if current_value >= best_value:
                        best_value = current_value
                        # best_corners[0] = corners_a
                        # best_corners[1] = corners_b
                        # best_corners[2] = corners_c
                        best_corners = [corners_a.copy(), corners_b.copy(), corners_c.copy()]
                        print(best_corners)
                        print(current_value)
    return best_corners

# Main funciton
def main():
    # Import csv data
    # input_data = input().strip()
    input_data_raw = get_data_file("/Users/alexnicholson/uni/uqcs/2022/codejam-solutions/2022/jerrys-rigged-game/tests/input/input03.txt")

    input_data_rows = input_data_raw.split(";")
    input_data = list()
    for i in range(0, len(input_data_rows)):            
        row = input_data_rows[i]
        row_list = row.split(",")
        input_data.append(row_list)

    # Now we should have a 2d list of input data, where we can access each row by: input_data[row][col]
    for row in input_data:
        print(row)
    print()

    out = get_electorates(input_data)
    print("=====================================================================")
    print(out)
    print("=====================================================================")

    # out_string = ""
    # for element in out:
    #     a = element[0]
    #     b = element[1]
    #     out_string = out_string + f"{a[0]},{b[0]};"
    # out_string = out_string[:-1]
    
    # print(out_string)

if __name__ == "__main__":
    main()
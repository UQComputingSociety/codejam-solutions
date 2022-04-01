# The directions of the leg of the T (i.e normal T has leg direction = DOWN)
DOWN = 0
LEFT = 1
UP = 2
RIGHT = 3
DIRECTIONS = [DOWN, LEFT, UP, RIGHT]

# Function to return a list containing 3 lists of 2 point (row,col) coord tuples representing the positions of the 
# top/left and bottom/right elements of the 3 electorate rectangles
# 
# Note: Use map_data[row][col] to acces points from coords

def get_electorates(map_data):
    out = list() # a list of all the pairs of foods and their prices that sum to N

    corners_a = [(-1,-1), (-1,-1)]
    corners_b = [(-1,-1), (-1,-1)]
    corners_c = [(-1,-1), (-1,-1)]

    # For each posiiton
    for direction in DIRECTIONS:
        corners_a[0] = (0, 0)
        
        head_gap = 1
        while head_gap < 15:
            leg_lead = 1
            while leg_lead < 15:
                # Do stuff
                
                leg_lead = leg_lead+1
            
            # Do stuff
            head_gap == head_gap+1


    return out

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

# Main funciton
def main():
    # Import csv data
    # input_data = input().strip()
    input_data_raw = get_data_file("/Users/alexnicholson/uni/uqcs/2022/codejam-solutions/2022/jerrys-rigged-game/tests/input/input00.txt")

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
    print(out)

    # out_string = ""
    # for element in out:
    #     a = element[0]
    #     b = element[1]
    #     out_string = out_string + f"{a[0]},{b[0]};"
    # out_string = out_string[:-1]
    
    # print(out_string)

if __name__ == "__main__":
    main()
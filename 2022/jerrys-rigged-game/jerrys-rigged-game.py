# The directions of the leg of the T (i.e normal T has leg direction = DOWN)
DOWN = 0
LEFT = 1
UP = 2
RIGHT = 3


def sum_to_n(N, prices_dict):
    out = list() # a list of all the pairs of foods and their prices that sum to N

    residuals = dict() # k:v = residual:value
    # Get all x, y pairs that sum to N (standard sum to n algorithm)
    for food_name in prices_dict:
        food_price = prices_dict[food_name]
        # print(food_name)
        # print(food_price)

        # If we are in an upper half price, see if we have matched with a lower half price
        try: 
            residuals[food_price]
            # print(residuals[food_price])
            # If we get here, we have matched a pair
            if food_price <= N/2: # if we have a lower half number, store the current item first, then the matched item
                out.append([[food_name, food_price], residuals[food_price]])
            else:
                out.append([residuals[food_price], [food_name, food_price]])

        except:
            # If we are here we havent found a match, so store its [food_name, food_price] in the relevant residual slot for later checking
            residual = N - food_price
            residuals[residual] = [food_name, food_price]

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

    # Now we should have a 3d list of input data, where we can access each row by: input_data[row][col]
    for row in input_data:
        print(row)
    print()
    quit()

    food_prices = dict()
    for row_num in range(0, len(food_data)):
        food_name = food_data[row_num][0] # get the col and convert to numpy array
        food_price = int(food_data[row_num][1]) # get the col and convert to numpy array
        
        food_prices[food_name] = food_price
    # print()
    # print(food_prices) # print out a summary
    # print()


    price_list = list()
    for name in food_prices:
        price_list.append(food_prices[name])
    # print(price_list)
    price_list.sort()
    # print(price_list)
    # print()

    out = sum_to_n(N, food_prices)
    # print(out)
    # print(len(out))

    out_string = ""
    for element in out:
        a = element[0]
        b = element[1]
        out_string = out_string + f"{a[0]},{b[0]};"
    out_string = out_string[:-1]
    
    print(out_string)

if __name__ == "__main__":
    main()
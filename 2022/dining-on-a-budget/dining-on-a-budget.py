from locale import ABDAY_1
import pandas as pd
import numpy as np
import sys


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

def main():
    arg = sys.argv[1]
    # print(arg[::-1])

    # Import csv data
    input_data = pd.read_csv(f"/Users/alexnicholson/uni/uqcs/2022/codejam/{arg}", sep=',', header=None)
    input_data = input_data.to_numpy()
    # print(input_data) # print out a summary
    N = input_data[0, 1]
    # print(N) # print out a summary
    # print()
    food_data = input_data[1:, :]
    # print(food_data) # print out a summary
    # print()

    food_prices = dict()
    for row_num in range(0, np.shape(food_data)[0]):
        food_name = food_data[row_num, 0] # get the col and convert to numpy array
        food_price = food_data[row_num, 1] # get the col and convert to numpy array
        
        food_prices[food_name] = food_price
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
        out_string = out_string + f"{a[0]} + {b[0]}\n"
    # print(out_string)

    return out_string

if __name__ == "__main__":
    main()
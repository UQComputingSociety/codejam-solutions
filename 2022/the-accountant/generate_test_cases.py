
import random
import the_accountant

in_format = "input{:02d}.txt"       # e.g. input00.txt
out_format = "output{:02d}.txt"     # e.g. output00.txt

NO_CASES = 50

MAX_COST = 10000
MAX_ITEM = 50

WIDTH = 50

things = ["Artichoke", "Arugula", "Asparagus", "Avocado", "Bamboo Shoots", "Bean Sprouts", "Beans", "Beet", "Belgian Endive", "Bell Pepper", "Bitter Melon", "Bok Choy", "Broccoli", "Brussels Sprouts", "Burdock Root", "Cabbage", "Green, Red, Savoy", "Calabash", "Capers", "Carrot", "Cassava", "Cauliflower", "Celery", "Celery Root", "Celtuce", "Chayote", "Corn", "Baby Corn", "Cucumber", "English Cucumber", "Gherkin", "Pickling Cucumbers", "Daikon Radish", "Edamame", "Eggplant", "Elephant Garlic", "Endive", "Curly", "Escarole", "Fennel", "Fiddlehead", "Galangal", "Garlic", "Ginger", "Grape Leaves", "Green Beans", "Wax Beans", "Greens", "Amaranth", "Beet Greens", "Collard Greens", "Dandelion Greens", "Kale", "Kohlrabi Greens", "Mustard Greens", "Rapini", "Spinach", "Swiss Chard", "Turnip Greens", "Hearts of Palm", "Horseradish", "Artichoke", "Jícama", "Kale", "Curly", "Lacinato", "Ornamental", "Kohlrabi", "Leeks", "Lemongrass", "Lettuce", "Butterhead", "Iceberg", "Romaine", "Lotus Root", "Lotus Seed", "Mushrooms", "Napa Cabbage", "Nopales", "Okra", "Olive", "Onion", "Green Onions", "Parsley", "Parsley Root", "Parsnip", "Peas", "green peas", "snow peas", "sugar snap peas", "Peppers", "Plantain", "Potato", "Pumpkin", "Purslane", "Radicchio", "Radish", "Rutabaga", "Sea Vegetables", "Shallots", "Spinach", "Squash", "Sweet Potato", "Swiss Chard", "Taro", "Tomatillo", "Tomato", "Turnip", "Water Chestnut", "Water Spinach", "Watercress", "Winter Melon", "Yams", "Zucchini"]

def malicious_format(revenues, expenses, total):

    formatted = ""

    # Write revenues first
    formatted += "Revenue\r\n"
    formatted += "-"*WIDTH + "\r\n"

    for i,c in revenues:
        pad_len = WIDTH - (len(i) + len(str(c)) + 1)
        wrong_pad_len = pad_len + random.randint(-20, 0) # bad pad, bad!

        formatted += i + "."*wrong_pad_len + "$" + str(c) + "\r\n"
    
    formatted += "\r\n"

    # Write expenses next
    formatted += "Expenses\r\n"
    formatted += "-"*WIDTH + "\r\n"

    for i,c in expenses:
        pad_len = WIDTH - (len(i) + len(str(c)) + 1)
        wrong_pad_len = pad_len + random.randint(-20, 0) # bad pad, bad!

        formatted += i + "."*wrong_pad_len + "$" + str(c) + "\r\n"
    
    formatted += "\r\n"

    # Total
    formatted += "Total\r\n"
    formatted += "-"*WIDTH + "\r\n"

    offset_balance = balance + random.randint(-50, 50) # randomly make it error
    pad_len = WIDTH - (len(str(offset_balance)) + 1)

    formatted += " "*pad_len + "$" + str(offset_balance) + "\r\n"

    return formatted

for c in range(NO_CASES):

    inf = open(f"tests/input/{in_format.format(c)}", 'w')
    outf = open(f"tests/output/{out_format.format(c)}", 'w')

    n_r = random.randint(1, MAX_ITEM)
    n_e = random.randint(1, MAX_ITEM)

    revenues = []
    possible = set(things) 
    for _ in range(n_r):
        
        # item
        choice = list(possible)[random.randint(0, len(possible) - 1)]
        possible.remove(choice)

        # cost
        cost = random.randint(0, MAX_COST)

        revenues.append((choice, cost))
        
    expenses = []
    possible = set(things) 
    for _ in range(n_e):

        # item
        choice = list(possible)[random.randint(0, len(possible) - 1)]
        possible.remove(choice)

        # cost
        cost = random.randint(0, MAX_COST)

        expenses.append((choice, cost))

    balance = sum(a for _,a in revenues) - sum(a for _,a in expenses)

    incorrect = malicious_format(revenues, expenses, balance)

    inf.write(incorrect)
    outf.write(the_accountant.the_accountant(incorrect.split('\r\n')))  

    inf.close()
    outf.close()
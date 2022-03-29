from sys import stdin


def split_sections(report: list[str]) -> list[tuple[str, int], list[str], int]:
    """
    takes `report` (from stdin) and produces two lists (revenue and
        expenses lines), and an int - the given sum  
    """

    rp = {
        "revenue": [],
        "expenses": [],
        "total": 0
    }

    last = "revenue"
    for line in report:
        if "Revenue" in line:
            # skip first
            continue
        if "Expenses" in line or "Total" in line:
            # swap to new section
            last = line.lower()
            continue
        if "-----" in line or line == '':
            # dodgy check for dash delimiter or empty string
            continue

        if last != "total":
            # parse line and store in tuple of (item, price)
            stripped = line.replace('.', '').split('$')
            rp[last].append((stripped[0], int(stripped[1])))
        else:
            rp[last] = int(line.strip().replace('$',''))

    return rp["revenue"], rp["expenses"], rp["total"]


def format_cost(revenue: list[tuple[str, int]], expenses: list[tuple[str, int]]) -> str:
    """
    Takes the given revenue and expenses, balances the sheet, and formats the cost section
    """

    formatted = ""
    
    # Create the header
    formatted += "Cost" + "\r\n"
    formatted += "-"*50 + "\r\n"

    wanted_length = 50

    # Calculate the correct balance
    balance = sum(price for _,price in revenue) - sum(price for _,price in expenses)
    
    bal_len = len(str(balance))
    pad_len = wanted_length - (bal_len + 1) # +1 for '$'

    formatted += " "*pad_len + "$" + str(balance) + "\r\n"

    return formatted 



def format_section(section_name: str, data: list[str, int]) -> str:
    """
    Takes an arbitrary section with its data and formats it
    """

    formatted = ""

    # Create the header
    formatted += section_name.capitalize() + "\r\n"
    formatted += "-"*50 + "\r\n"

    wanted_length = 50

    # Format each line of the section
    for entry in data:

        item, cost = entry[0], entry[1]

        item_len = len(item)
        cost_len = len(str(cost))

        pad_len = wanted_length - (item_len + cost_len + 1) # +1 for dollar sign

        formatted += item + "."*pad_len + "$" + str(cost) + "\r\n"
    

    return formatted

def the_accountant(data: list[str]) -> str:
    """
    Takes the raw report, parses it, and returns it formatted
    """

    # Parse given input into sections containing items and prices
    revenue, expenses, cost = split_sections(data)

    # Format each section
    revenue_formatted = format_section("revenue", revenue)
    expenses_formatted = format_section("expenses", expenses)
    costs_formatted = format_cost(revenue, expenses)

    # Join all the sections
    output = "\r\n".join([revenue_formatted, expenses_formatted, costs_formatted])

    return output

if __name__ == "__main__":

    lines = []

    for line in stdin:
        lines.append(line.strip())

    final_report = the_accountant(lines)

    print(final_report)

    
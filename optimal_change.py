def optimal_change(item_cost, amount_paid):
    change = amount_paid - item_cost
    change_string = f"The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is "

    hundred_bills = int(change // 100)
    if hundred_bills == 1:
        change_string += "1 $100 bill, "
    elif hundred_bills > 1:
        cangeh_string += f"{hundred_bills} $100 bills, "
    fifty_bills = int(change - hundred_bills * 100) // 50
    if fifty_bills == 1:
        change_string += "1 $50 bill, "
    elif fifty_bills > 1:
        change_string += f"{fifty_bills} $50 bills, "
    
    twenties = int(change - hundred_bills * 100 - fifty_bills * 50) // 20
    if twenties == 1:
        change_string += "1 $20 bill, "
    elif twenties > 1:
        change_string += f"{twenties} $20 bills, "
    
    tens = int(change - hundred_bills * 100 - fifty_bills * 50 - twenties * 20) // 10
    if tens == 1:
        change_string += "1 $10 bill, "
    elif tens > 1:
        change_string += f"{tens} $10 bills, "
    
    fives = int(change - hundred_bills * 100 - fifty_bills * 50 - twenties * 20 - tens * 10) // 5
    if fives == 1:
        change_string += "1 $5 bill, "
    elif fives > 1:
        change_string += f"{fives} $5 bills, "
    
    ones = int(change - hundred_bills * 100 - fifty_bills * 50 - twenties * 20 - tens * 10 - fives * 5) // 1
    if ones == 1:
        change_string += "1 $1 bill, "
    elif ones > 1:
        change_string += f"{ones} $1 bills, "

    decimal = (change - hundred_bills * 100 - fifty_bills * 50 - twenties * 20 - tens * 10 - fives * 5 - ones)*100
    deci = round(decimal)
    quarters = int(deci)// 25 
    if quarters == 1:
        change_string += "1 quarter, "
    elif quarters > 1:
        change_string += f"{quarters} quarters, "
    
    dimes = int( deci - quarters * 25) // 10 
    if dimes == 1:
        change_string += "1 dime, "
    elif dimes > 1:
        change_string += f"{dimes} dimes, "
    
    nickels = int(deci - quarters * 25 - dimes * 10) // 5 
    if nickels == 1:
        change_string += "1 nickel, "
    elif nickels > 1:
        change_string += f"{nickels} nickels, "
    
    pennies = int(deci - quarters * 25 - dimes * 10 - nickels * 5) 
    if pennies == 1:
        change_string += "1 penny, "
    elif pennies > 1:
        change_string += f"{pennies} pennies, "
    if change_string[-2:] == ", ":
        change_string = change_string[:-2] + "."
    
    change_string = change_string.split(', ')
    print(change_string)
    if len(change_string) > 1 :
        change_string[-1] = "and " + change_string[-1]
    result = ', '.join(change_string)
    
    
    return result
print(optimal_change(300, 500))
def solve(meal_cost, tip_percent, tax_percent):
    x=(meal_cost*tip_percent)/100
    y=(meal_cost*tax_percent)/100
    print('The total meal cost is',round(meal_cost+x+y),'dollars.')
    
if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)

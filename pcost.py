# pcost.py
#
# Error handling Ex 1.31
import csv

def portfolio_cost(filename):
    total_cost = 0.0
    try:
        with open(filename,'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                try:
                    name, shares, price = row
                    total_cost += int(shares)*float(price)
                except ValueError:
                    print(f'Warning: Skipping invalid row: {row}')
    except FileNotFoundError:
        print(f'Error: File {filename} not found')
        return None
    return total_cost
            

cost = portfolio_cost('/home/dd/Desktop/portfolio.csv')
if cost is not None:
    print('Total cost:', cost)
    

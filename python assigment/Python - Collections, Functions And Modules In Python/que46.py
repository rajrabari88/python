'''
• Write a Python program to combine values in python list of dictionaries. 
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 
300}, o {'item': 'item1', 'amount': 750}]
Expected Output:
Counter ({'item1': 1150, 'item2': 300})
'''


from collections import Counter
data = [{'item': 'item1', 'amount':500}, 
        {'item': 'item2', 'amount':600}, 
        {'item': 'item1', 'amount':350}]
combined_values = Counter()
for d in data:
    combined_values[d['item']] += d['amount']
print("Combined values:")
print(combined_values)

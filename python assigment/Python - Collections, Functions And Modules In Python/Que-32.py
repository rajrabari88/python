#Write a Python script to sort (ascending and descending) a dictionary by value

input_dict = {'english': 80, 'gujrati': 60, 'hindi': 75, 'maths': 95}

desc = dict(sorted(input_dict.items(), key=lambda item: item[1], reverse=True))

asc = dict(sorted(input_dict.items(), key=lambda item: item[1]))

print("Descending order:", desc)
print("Ascending order:",asc)

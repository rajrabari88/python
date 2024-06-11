'''
Write a python program to find the longest words
'''
def find_longest_words(filename):
    longest_words = []
    max_length = 0
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if len(word) > max_length:
                    max_length = len(word)
                    longest_words = [word]
                elif len(word) == max_length:
                    longest_words.append(word)
    
    return longest_words

filename = 'example.txt'
longest_words = find_longest_words(filename)
print("Longest word(s) in the file:")
for word in longest_words:
    print(word)

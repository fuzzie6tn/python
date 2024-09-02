import pandas

data = pandas.read_csv('alphabet.csv')
phonetic_dict = {row.letter:row.code for (index,row) in data.iterrows()}
# print(phonetic_dict)

word = input("Enter a word:\n").upper()
output = [phonetic_dict[letter] for letter in word]
print(output)

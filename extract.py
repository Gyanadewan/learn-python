# import re
# input = input("Enter a text:")
# pattern = r"\d+"

# matchs = re.findall(pattern,input)
# print(matchs)

# numbers = []
# for x in matchs:
#     numbers.append(int(x))

# # numbers = [int(match) for match in matchs]
# print(numbers)

import re
text = input("Enter your text:")
petarn = r"\d+"


matches = re.findall(petarn,text)
# print(matches)
# numbers = []
# for  match in matches :
#        numbers.append (int(match))
numbers = [int(match)for match in matches]
print(numbers)
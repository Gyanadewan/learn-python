import re 

text = "I love python. python is easy. Python is powerful."
word = "python"
matches = re.findall(word,text)
print("match:",matches)
print("mathces",len(matches))
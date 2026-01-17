import re 
text = "The quick brown fox jumps over the lazy dog"

#search for a pattern
match=re.search("brown",text)
print(match)
if match:
    print("Match found")
    print("start index :",match.start())
    print("end index :",match.end())

#find all the occurences of a pattern
matches=re.findall("the",text,re.IGNORECASE) #case-insensitive search
print("Matches:",matches)

#replacing
new_text=re.sub("fox","cat",text)
print("New text:",new_text) 
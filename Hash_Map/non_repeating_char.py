# count first non repeaing charectere

sent = "aacbbb"

count ={}
for char in sent:
  count[char] = count.get(char, 0)+1

print(count == 0)

# counte the frequency of an element in sentence

sen = "car is black and car is so fast"
words = sen.split()

count ={}

for sentence in words:
  count[sentence]= count.get(sentence, 0 ) + 1
  

print(count)
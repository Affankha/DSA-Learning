# counting word usign Hash map

words = ["apple", "banana", "Coconut", "pinaple", "water melon", "apple" ];

count ={}

for word in words:
    count[word] = count.get(word, 0 )+1


print(count) 


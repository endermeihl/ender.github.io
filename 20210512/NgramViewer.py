import sys
counts = {}

with open("kjvbible.txt", "r") as f:
    for line in f.readlines():
        words = line.lower().split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1
pairs = sorted(counts.items(), key=lambda kv: kv[1], reverse=False)
for word, count in pairs:
    print(word, count)
import hashlib
import bitarray

class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray.bitarray(size)
        self.bit_array.setall(0)

    def add(self, string):
        for seed in range(self.hash_count):
            result = hashlib.sha256((string + str(seed)).encode()).hexdigest()
            index = int(result, 16) % self.size
            self.bit_array[index] = 1

    def lookup(self, string):
        for seed in range(self.hash_count):
            result = hashlib.sha256((string + str(seed)).encode()).hexdigest()
            index = int(result, 16) % self.size
            if self.bit_array[index] == 0:
                return "Nope"
        return "Probably"

# Example usage
bf = BloomFilter(500000, 7)
bf.add("apple")
bf.add("banana")
bf.add("orange")

print(bf.lookup("apple")) # Output: Probably
print(bf.lookup("banana")) # Output: Probably
print(bf.lookup("orange")) # Output: Probably
print(bf.lookup("grape")) # Output: Nope
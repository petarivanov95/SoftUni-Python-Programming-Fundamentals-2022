message = input().split(" ")
decyphered_to_text = []


def num_fr_str(word):
    nums = [x for x in word if x.isnumeric()]
    return "".join(nums)


def decipher(message):
    # cipher = chr_fr_str(message) + message[-1] + message[len(chr_fr_str(message))+1:-1] + message[len(chr_fr_str(message))+1]
    chr_word = chr(int(num_fr_str(message)))
    length = len(num_fr_str(message))
    cipher_unfixed = chr_word + message[length + 1 :]
    return cipher


for x in message:
    print(decipher(x), end=" ")

# message = '72olle'
# chr_word = chr(int(num_fr_str(message)))
# length = len(num_fr_str(message))

# print(message[2+1:-1])

# my secret message

alphabet = "abcdefghijklmnopqrstuvwxyz"
partialOne = ""
partialTwo = ""
newAlphabet = ""

message = input("Please enter a message to hide: ").lower()
key = int(input("Please enter a number to shift by: "))

if key == 0:
    newAlphabet = alphabet
elif key > 0:
    partialOne = alphabet[:key]         # creating substrings using stringname[indexOne:indexTwo]
    partialTwo = alphabet[key:]
    newAlphabet = partialTwo + partialOne
elif key < 0:
    partialOne = alphabet[:(26 + key)]
    partialTwo = alphabet[(26 + key):]
    newAlphabet = partialTwo + partialOne

newMessage = ""

for x in range(0, len(message)):           # string length is len()
    index = alphabet.find(message[x])
    if index < 0:                           # find() returns -1 if character not present, like a space
        newMessage += message[x]
    else:
        newMessage += newAlphabet[index]

print(newMessage)
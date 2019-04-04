import sys

words = open(sys.argv[1], "r")
write = open(sys.argv[1] + ".json", "w")

array = words.readlines()

write.write("[\n")

for i in range(len(array) - 1):
    line = array[i]
    array[i] = ("\"" + line[:len(line) - 1] + "\",").lower()
    write.write(array[i] + "\n")

end = len(array) - 1
line = array[end]
array[end] = ("\"" + line + "\"").lower()
write.write(array[end] + "\n")

write.write("]")
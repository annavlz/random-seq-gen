import random

input_string = ""
output_string = []

with open('input.txt') as reader:
    input_string = reader.readline().split(",")

print("How long do you want the string to be?")
output_size = int(input())
size = len(input_string)
print("How big is the window?  number between 1 and .")
window = int(input())

matrix = input_string * size
indexes = list(range(0, size*size-window))

while output_size > 0:
    n = random.randint(0,len(indexes)-window)
    output_string.append(matrix[indexes[n]])
    output_size -= 1

with open('output.txt', 'w') as writer:
    writer.write(','.join(output_string))

print("Done! xx")
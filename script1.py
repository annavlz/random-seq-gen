import random

input_string = ""
output_string = []

with open('input.txt') as reader:
    input_string = reader.readline().split(",")
    
size = len(input_string)
matrix = input_string * size
indexes = list(range(0, size*size))
for i in matrix:
    n = random.randint(0,len(indexes)-1)
    output_string.append(matrix[indexes[n]])
    del indexes[n]

with open('output.txt', 'w') as writer:
    writer.write(','.join(output_string))

print("Done! xx")
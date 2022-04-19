import random
def flatten_list(_2d_list):
    flat_list = []
    for element in _2d_list:
        if type(element) is list:
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list
    
input_string = ""
output_string = []

with open('input.txt') as reader:
    input_string = reader.readline().split(",")
    
size = len(input_string)
matrix = input_string * size
print("How big is the window?  number between 1 and")
window = int(input())
indexes = list(range(0, size*size-window))
for i in matrix:
    n = random.randint(0,len(indexes)-1-window)
    output_string.append(matrix[indexes[n]:indexes[n]+window])

with open('output.txt', 'w') as writer:
    writer.write(' '.join(flatten_list(output_string)))

print("Done! xx")
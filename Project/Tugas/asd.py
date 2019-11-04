# OOP Program
def bubblesort(data):
    print("Unsorted...")
    print_data(data, len(data))
    print("Bubble sorting...")
    lastindex = len(data) - 1
    while lastindex > 0:
        for i in range(0, lastindex):
            if data[i] > data[i+1]:
                data[i] = data[i] ^ data[i+1]
                data[i+1] = data[i] ^ data[i+1]
                data[i] = data[i] ^ data[i+1]
        print_data(data, lastindex)
        lastindex -= 1
    print("Sorted!")

def print_data(data, sortedto):
    for i in range(0, len(data)):
        if i >= sortedto:
            print("{:3d}".format(data[i]), end="")
        else:
            print("{:3d}".format(data[i]), end="")
    print("")

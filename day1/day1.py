import os

INPUT = "day1.1.input"
INPUT_PATH = os.path.join(os.path.dirname(__file__), INPUT)
print(INPUT_PATH)
def day1_1():
    inventory = [0]
    with open(INPUT_PATH, 'r') as input:
        for line in input.readlines():
            if line == "\n":
                inventory.append(0)
            else:
                cal = int(line)
                inventory[-1] += cal
    
    print("Max Calories", max(inventory))
    return inventory


def day1_2(inventory):
    sorted_inv = sorted(inventory, reverse=True)
    print("Sum top 3", sum(sorted_inv[:3]))

if __name__ == "__main__":
    inventory = day1_1()
    day1_2(inventory)
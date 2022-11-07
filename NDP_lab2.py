import random
import matplotlib.pyplot as plt

def generate_number(n):
    """
    Function to generate random number

    :param n: range to choose a number from
    """
    return random.randint(1, n)

def poison_bottle(n, m):
    """
    Function to calculate how many people need to drink
    to find the poisoned bottle

    :param n: number of bottles
    :param m: number of people
    """
    bottle = generate_number(n)
    print("Special bottle number is {}".format(bottle))
    per_person = int(n/m)
    data = list(range(1,n+1))
    random.shuffle(data)
    chunks = [data[x:x+per_person] for x in range(0, len(data), per_person)]
    number = 1
    for element in chunks:
        if bottle not in element:
            number += 1
        else:
            break
    for i in range(m):
        print("Person {} will drink from bottles {}".format(i+1, chunks[i]))
    print("Total number of brave adventurers that will drink from special bottle is {}".format(number))

    return number

def visualize(n):
    """
    Function to visualize number of people who had to drink
    in order to find the poisoned bottle

    :param n: number of iterations
    """
    output = []
    for i in range(n):
        output.append(poison_bottle(1000,10))
    plt.figure(figsize=(15,8))
    plt.plot(output)
    plt.title("Estimating number of brave adventurers that will drink from special bottle")
    plt.ylabel("Number of people")
    plt.xlabel("Iteration")
    plt.show()

visualize(100)
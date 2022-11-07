import random
import matplotlib.pyplot as plt

def estimate_pi(n, r):
    """
    Function to estimate pi

    :param n: number of iterations
    :param r: circle radius
    """
    
    outside_circle = 0
    inside_circle = 0
    estimated_pi = []
    
    for i in range(n):
        x = random.uniform(-r, r)
        y = random.uniform(-r, r)
        
        if (x**2 + y**2 > r**2): # if point in the circle
            outside_circle += 1
        else: # if point not in the circle
            inside_circle += 1
    
        pi = (4*inside_circle)/(inside_circle+outside_circle)
        estimated_pi.append(pi)
        
    return estimated_pi


def visualize(pi_list):
    """
    Function to visualize pi estimation - iteration vs pi value

    :param pi_list: list with estimated pi values
    """
    
    plt.figure(figsize=(15,8))
    plt.plot(pi_list)
    plt.axhline(y = 3.14, color = 'r', linestyle = '-')
    plt.title(f'Estimating $\pi$ value')
    plt.ylabel(f'$\pi$ value')
    plt.xlabel("Iteration")
    plt.show()
    

def main():
    pi = estimate_pi(100000, 1)
    visualize(pi)

if __name__ == "__main__":
    main()
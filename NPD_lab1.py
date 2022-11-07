import random
import matplotlib.pyplot as plt

def estimate_pi(n, r):
    
    outside_circle = 0
    inside_circle = 0
    estimated_pi = []
    
    for i in range(n):
        x = random.uniform(-r, r)
        y = random.uniform(-r, r)
        
        if (x**2 + y**2 > r**2):
            outside_circle += 1
        else:
            inside_circle += 1
    
        pi = (4*inside_circle)/(inside_circle+outside_circle)
        estimated_pi.append(pi)
        
    return estimated_pi


def visualize(pi_list):
    
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
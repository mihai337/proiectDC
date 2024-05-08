import random
import math
import matplotlib.pyplot as plt

class CPUDigitsOfPI:
    def __init__(self):
        pass
    
    def start(self, algorithm, n): 
        digits=algorithm(n)
        return digits
    
    def monte_carlo(self, n):      
        inside_circle = 0
        total_points = 0

        for _ in range(n):
            x = random.uniform(0, 1)
            y = random.uniform(0, 1)
            distance = math.sqrt(x**2 + y**2)
            
            if distance <= 1:
                inside_circle += 1
            total_points += 1

        pi_estimate = 4 * inside_circle / total_points
        return pi_estimate
    
    def plot(self, result):
        plt.plot(result.keys(), result.values(), marker='o')
        plt.xlabel('Digits of Pi')
        plt.ylabel('Runtime (seconds)')
        plt.title('Monte Carlo Pi Calculation Runtime')
        plt.grid(True)
        plt.show()

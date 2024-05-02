import time
import random
import math
import matplotlib.pyplot as plt


class CPUDigitsOfPI:
    def __init__(self):
        pass
    
    def benchmark(self, algorithm, n):
        
        start_time=time.time()
        digits=algorithm(n)
        end_time=time.time()
        return digits, end_time - start_time
    
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
if __name__ == "__main__":
    benchmark= CPUDigitsOfPI()
    
    val=[50,100,500,1000,5000,10000,50000,100000]
    result={}
    
    for n in val:
        _, runtime= benchmark.benchmark(benchmark.monte_carlo, n)
        result[n]=runtime
    with open("pi.txt","w") as f:
        f.write("Digits\tRuntime (seconds)\n")
        for n, runtime in result.items():
            f.write(f"{n}\t{runtime}\n")
            
            
    plt.plot(result.keys(), result.values(), marker='o')
    plt.xlabel('Digits of Pi')
    plt.ylabel('Runtime (seconds)')
    plt.title('Monte Carlo Pi Calculation Runtime')
    plt.grid(True)
    plt.show()

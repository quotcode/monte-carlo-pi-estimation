import random
import multiprocessing
import time
import numpy as np

class MonteCarloPi :
    def __init__(self, n_points):
        self.n_points = n_points
        self.count_in_circle = 0

    def estimate_pi(self):
        for _ in range(self.n_points):
            x = random.random()
            y = random.random()
            if x**2 + y**2 <= 1:
                self.count_in_circle += 1

        pi = 4 * self.count_in_circle / self.n_points
        return pi

def estimate_pi_vectorized(n):
  # Generate random points in a square with side length 2.
  points = np.random.uniform(-1, 1, size=(n, 2))

  # Calculate the distance from each point to the origin.
  distances = np.linalg.norm(points, axis=1)

  # Count the number of points that are inside the circle.
  inside = np.count_nonzero(distances <= 1)

  # Estimate pi as the ratio of the number of points inside the circle to the
  # total number of points.
  return 4 * inside / n

        

def main():
    n_points = 1000000
    n_processes = 10
    start_time = time.time()

    with multiprocessing.Pool(n_processes) as pool:
        estimators = [MonteCarloPi (n_points // n_processes) for _ in range(n_processes)]
        results = pool.map(MonteCarloPi.estimate_pi, estimators)

    # aggregating the results from all processes i.e. n_processes
    pi_estimate = sum(results) / n_processes

    end_time = time.time()
    print("1. Multiprocessing Implementation with Classes and Objects")
    print("Estimated value of pi:", pi_estimate)
    print("Time taken:", round((end_time - start_time), 6), "seconds")
    print()


    
    print("2. Vectorized Operations Implementation")
    start_time = time.time()
    print("Estimated value of pi:", estimate_pi_vectorized(n_points))
    end_time = time.time()
    print("Time taken:", round((end_time - start_time), 6), "seconds")
    




   

if __name__ == "__main__":
    main()
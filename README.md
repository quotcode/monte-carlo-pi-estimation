Problem Statement: 
1. Comparing Monte Carlo Estimation Methods for π with Classes and Objects
2. You are tasked with comparing two different implementations for estimating the value of π (pi) using the Monte Carlo method. 
The Monte Carlo method is a statistical technique that uses random sampling to estimate numerical results.


Implementations:
1. Multiprocessing Implementation with Classes and Objects:
 - This implementation utilizes classes and objects to organize the computation within a multiprocessing framework. 
 - It defines a MonteCarloPi class that encapsulates the Monte Carlo simulation logic. The class creates multiple processes to parallelize the computation, with each process responsible for generating random points and counting points inside the unit circle. 
 - By aggregating the results from all processes, the class estimates the value of π.

2. Vectorized Operations Implementation: 
 - This implementation leverages NumPy's vectorized operations to perform the Monte Carlo simulation efficiently. 
 - It generates random points using NumPy arrays and applies vectorized operations to check if the points fall within the unit circle. 
 - By counting the number of points inside the circle, it estimates the value of π.

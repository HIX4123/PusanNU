
import matplotlib.pyplot as plot

Korea = [ 4.530, 2.820, 1.570, 1.467, 1.226, 1.244, 1.297, 1.187, 1.205,
           1.239,1.172, 1.052, 0.977,  0.918, 0.837 ]
Japan = [ 2.13, 1.75, 1.54, 1.36, 1.39, 1.39, 1.41, 1.43, 1.42,
           1.45, 1.44, 1.43, 1.42, 1.36, 1.34 ]
USA   = [ 2.48, 1.84, 2.08, 2.06, 1.93, 1.89, 1.88, 1.86, 1.86, 1.84,
           1.82, 1.77, 1.73, 1.71, 1.64]
France= [ 2.48, 1.95, 1.78, 1.87, 2.02, 2.00, 1.99, 1.97, 1.97, 1.92,
           1.89, 1.86, 1.84, 1.83, 1.82 ]

plot.plot( list(range(len(Korea))), Korea, 'ok-', width=0.8, alpha=0.4)

plot.show()

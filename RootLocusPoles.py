import numpy as np

def root_locus_plot(K):
    poles = np.array([0, 0]) # Initialize array to store poles
    angles = np.linspace(0, 2*np.pi, 100) #Angles for plotting the locus

    for k in K:
        #Calculate poles for each value of K
        pole = (-k + np.sqrt(k**2 -4))/2
        poles = np.vstack((poles,pole))

    





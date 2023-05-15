# Function root_locus_plot is defined that takes an array of K values as input. It iterates
#through each K value to calculate the corresponding pole, storing themm in the "poles" array.
#The root locus plot is then generated using Matplotlib, with the poles plotted in blue and their
#mirrored counterparts in red.

#The range of K vaues np.linspace(0,10,1000) can be adjusted as per your requirements. The code also
#prints the characteristic eq based on the last value of K in the range.


import numpy as np
import matplotlib.pyplot as plt

def root_locus_plot(K):
    poles = [] # Initialize a Python list to store poles
    angles = np.linspace(0, 2*np.pi, 100) #Angles for plotting the locus

    for k in K:
        #Calculate poles for each value of K
        pole = (-k + np.sqrt(k**2 - 4))/2
        poles.append(pole)

    poles = np.array(poles)  #Convert the list of poles to a numoy array

    #Plotting root locus
    plt.plot(poles.real, poles.imag, 'b')   #Plot the root locus
    plt.plot(poles.real, -poles.imag, 'r')  # Plot the mirrored root locus
    plt.scatter(poles.real[0], poles.imag[0], marker='x', color='black')  #Plot the original poles
    plt.xlabel('Real axis')
    plt.ylabel('Imaginary axis')
    plt.title('Root locus plot')
    plt.axhline(y=0, color='black', linestyle='--', linewidth=0.5)  #Add x-axis
    plt.grid(True)
    plt.show()

#Main code
K = np.linspace(0, 10, 1000)  #Range of K values

# Characteristic equation

characteristic_equation = "s^2 + 1 + {}s = 0".format(K[-1])

print("Characteristic equation:", characteristic_equation)

root_locus_plot(K)





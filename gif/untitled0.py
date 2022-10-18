import numpy as np
import matplotlib.pyplot as plt
import time
 
coordinates = np.array([[0.39, 154.5],
                        [31.05, 131.16],
                        [1.14, 118.41],
                        [25.65, 142.11],
                        [-293.25, 90.75],
                        [13.05, 152.55],
                        [25.95, 149.61],
                        [59.79, 150.21]])
 
cities = {'Berlinsk': coordinates[0],
          'Hamburovsk': coordinates[1],
          'Frankfurtsk': coordinates[2],
          'Brogerakt': coordinates[3],
          'Anfangstin': coordinates[4],
          'Limburan': coordinates[5],
          'Dresdenau': coordinates[6],
          'Regensk': coordinates[7]}
 
vectors = np.array([[306.3, 61.8],
                    [12.9, -2.94],
                    [-0.3, -7.5],
                    [5.4, -10.95],
                    [28.74, 19.05],
                    [-60.21, 4.29],
                    [1.56, -36.09],
                    [-294.39, -27.66]])
plt.grid()
plt.scatter(cities["Berlinsk"][0],cities["Berlinsk"][1])
plt.scatter(cities["Hamburovsk"][0],cities["Hamburovsk"][1])
plt.scatter(cities["Frankfurtsk"][0],cities["Frankfurtsk"][1])
plt.scatter(cities["Anfangstin"][0],cities["Anfangstin"][1])
plt.scatter(cities["Limburan"][0],cities["Limburan"][1])
plt.scatter(cities["Dresdenau"][0],cities["Dresdenau"][1])
plt.scatter(cities["Regensk"][0],cities["Regensk"][1])
plt.quiver(cities["Anfangstin"][0],cities["Anfangstin"][1],vectors[0][0],vectors[0][1],units='xy',scale=1)
#plt.quiver(-300,120,vectors[1][0],vectors[1][1])
plt.show()
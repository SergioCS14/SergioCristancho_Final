import numpy as np
import matplotlib as plt

Datost = np.genfromtxt("Datos15.dat", ",")
Datos = np.transpose(Datost)

plt.figure()
plt.plot(Datos[1],Datos[2], label="Trayectoria")
plt.legend()
plt.xlabel("x [ua]")
plt.ylabel("y [ua]")
plt.title("Trayectoria de la particula cargada")
plt.savefig("CristanchoSergio_final_15.pdf")
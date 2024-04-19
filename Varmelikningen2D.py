#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 19:22:44 2024

@author: klara
"""
import numpy as np
import matplotlib.pyplot as plt

def VarmelikningenNumerisk(nx, ny, nt, dx, dy, alpha, dt):
    
    # Initialisere temperaturfeltet
    
    u = np.zeros((nx, ny))

    # sette initialbetingelser 
    u[nx//2, ny//2] = 1  # Plasser en varmepuls midt i området

    # Implementre løkke for å løse varmelikningen
    for n in range(nt):
        un = u.copy()  # Kopierer temperaturfeltet fra forrige tidstrinn

        # Iterere over hver node i rutenettet (unntatt grensene)
        for i in range(1, nx-1):
            for j in range(1, ny-1):
                u[i, j] = un[i, j] + alpha * dt * (
                    (un[i+1, j] - 2*un[i, j] + un[i-1, j]) / dx**2 +
                    (un[i, j+1] - 2*un[i, j] + un[i, j-1]) / dy**2)

        # Implementere periodiske grensebetingelser 
        u[0, :] = u[nx-2, :]  
        u[nx-1, :] = u[1, :] 
        u[:, 0] = u[:, ny-2] 
        u[:, ny-1] = u[:, 1]  
    return u

# Parametere
nx = 50  # Antall punkter i x-retning
ny = nx  # Antall punkter i y-retning
nt = 1000  # Antall tidssteg
dx = 0.1  # Stgelengde i x-retning
dy = 0.1  # Steglengde i y-retning
alpha = 0.1# Termisk diffusivitet alpha
dt = 0.01  # Tidssteg


# Plotting 
x = np.linspace(0, nx-1, nx)
y = np.linspace(0, ny-1, ny)
X, Y = np.meshgrid(x, y)

plt.figure(figsize=(10, 8))
plt.contourf(X, Y, VarmelikningenNumerisk(nx, ny, nt, dx, dy, alpha, dt), cmap='hot')
plt.colorbar(label='Temperatur')
plt.title('Varmepuls i to romlige dimensjoner')
plt.xlabel('X-akse')
plt.ylabel('Y-akse')
plt.show()

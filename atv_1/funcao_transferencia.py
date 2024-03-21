# Importando bibliotecas
import numpy as np
from math import sqrt
import matplotlib.pyplot as plt

# Função para calcular a resposta em frequência do filtro passa-baixas de segunda ordem de Sallen-Key.
def filtro_passa_baixas(f, R, C):
  """
  Parâmetros:
    f: Frequência em Hz
    R: Resistência em Ohms
    C: Capacitância em Farads

  """

  wc = 2 * np.pi * f
  A = 1 / (1 + (wc * R * C)**2)

  return A / (1 + 1j * wc * R * C + (wc * R * C)**2)

# Função para calcular o valor dos capacitores para um filtro passa-baixas de segunda ordem de Sallen-Key.
def calcular_capacitores(R, F, Q):
  """
  Parâmetros:
    R: Resistência em Ohms.
    F: Frequência de corte em Hz.
    Q: Fator de qualidade.
  """

  C1 = 1 / (2 * np.pi * F * R * Q)
  C2 = C1 / (2 * Q)

  return C1, C2

# Função para montar a função de transferência do filtro passa-baixas de segunda ordem de Sallen-Key.
def funcao_transferencia(s, R, C):
  """
  Parâmetros:
    s: Variável de Laplace.
    R: Resistência em Ohms.
    C: Capacitância em Farads.
  """

  H = 1 / (1 + (2 * np.pi * R * C * s)**2)
  return H

# Definindo os parâmetros
f = np.logspace(-1, 4, 1000)  # Frequências de 0,1 Hz a 10 kHz
R = 10000  # Resistência em Ohms
F = 1.45  # Frequência de corte em Hz
Q = 1  # Fator de qualidade

# Calculando o valor do capacitor
C = 1 / (4 * np.pi * R * F * Q)

print(f"Valor do capacitor: {C}")

# Calculando os valores dos capacitores
C1, C2 = calcular_capacitores(R, F, Q)

# Definindo o coeficiente de amortecimento
zeta = 0.7

# Calculando a frequência natural do sistema
wn = sqrt(1 / (C * R))

# Calculando os parâmetros do controlador PID
Kp = 4 * (zeta / wn)
Ki = 4 * zeta * wn
Kd = 4 * zeta / wn**2

# Imprimindo os parâmetros do controlador PID
print(f"Kp: {Kp}")
print(f"Ki: {Ki}")
print(f"Kd: {Kd}")

# Calculando a resposta em frequência
H = filtro_passa_baixas(f, R, C)

# Plotando a resposta em frequência
plt.plot(f, 20 * np.log10(np.abs(H)), label="Magnitude (dB)")
plt.plot(f, np.angle(H), label="Fase (graus)")
plt.legend()
plt.xlabel("Frequência (Hz)")
plt.ylabel("Magnitude (dB) / Fase (graus)")
plt.show()
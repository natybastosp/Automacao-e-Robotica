import numpy as np
import matplotlib.pyplot as plt

def filtro_passa_baixas(f, R, C):
  """
  Função para calcular a resposta em frequência do filtro passa-baixas de segunda ordem de Sallen-Key.

  Parâmetros:
    f: Frequência em Hz
    R: Resistência em Ohms
    C: Capacitância em Farads

  """

  wc = 2 * np.pi * f
  A = 1 / (1 + (wc * R * C)**2)

  return A / (1 + 1j * wc * R * C + (wc * R * C)**2)

def calcular_capacitores(R, F, Q):
  """
  Função para calcular o valor dos capacitores para um filtro passa-baixas de segunda ordem de Sallen-Key.

  Parâmetros:
    R: Resistência em Ohms.
    F: Frequência de corte em Hz.
    Q: Fator de qualidade.

  """

  C1 = 1 / (2 * np.pi * F * R * Q)
  C2 = C1 / (2 * Q)

  return C1, C2

def funcao_transferencia(s, R, C1, C2):
  """
  Função para montar a função de transferência do filtro passa-baixas de segunda ordem de Sallen-Key.

  Parâmetros:
    s: Variável de Laplace.
    R: Resistência em Ohms.
    C1: Valor do capacitor C1 em Farads.
    C2: Valor do capacitor C2 em Farads.

  """

  H = 1 / (1 + (2 * np.pi * s * R * C1)**2)
  H *= 1 + (2 * np.pi * s * R * C2)

  return H



# Definindo os parâmetros
f = np.logspace(-1, 4, 1000)  # Frequências de 0,1 Hz a 10 kHz
R = 100  # Resistência em Ohms
C = 110e-6  # Capacitância em Farads
F = 1.45  # Frequência de corte em Hz
Q = 0.707  # Fator de qualidade

# Calculando os valores dos capacitores
C1, C2 = calcular_capacitores(R, F, Q)

# Calculando a resposta em frequência
H = filtro_passa_baixas(f, R, C)

# Plotando a resposta em frequência
plt.plot(f, np.abs(H), label="Magnitude")
plt.plot(f, np.angle(H), label="Fase")
plt.legend()
plt.xlabel("Frequência (Hz)")
plt.ylabel("Magnitude (dB) / Fase (graus)")
plt.show()
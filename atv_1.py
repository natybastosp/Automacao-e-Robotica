import numpy as np
import matplotlib.pyplot as plt

def filtro_passa_baixas(f, R, C):
  """
  Função para calcular a resposta em frequência do filtro passa-baixas de segunda ordem de Sallen-Key.

  Parâmetros:
    f: Frequência em Hz
    R: Resistência em Ohms
    C: Capacitância em Farads

  Retorno:
    Resposta em frequência do filtro (complexo)
  """

  wc = 2 * np.pi * f
  A = 1 / (1 + (2 * np.pi * f * R * C)**2)

  return A / (1 + 1j * wc * R * C + (wc * R * C)**2)

# Definindo os parâmetros
f = np.logspace(-1, 4, 1000)  # Frequências de 0,1 Hz a 10 kHz
R = 100e3  # Resistência em Ohms
C = 110e-6  # Capacitância em Farads

# Calculando a resposta em frequência
H = filtro_passa_baixas(f, R, C)

# Plotando a resposta em frequência


plt.plot(f, np.abs(H), label="Magnitude")
plt.plot(f, np.angle(H), label="Fase")
plt.legend()
plt.xlabel("Frequência (Hz)")
plt.ylabel("Magnitude (dB) / Fase (graus)")
plt.show()

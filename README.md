Descrição
Este código Python implementa um filtro passa-baixas de segunda ordem de Sallen-Key. O código inclui funções para:

Calcular a resposta em frequência do filtro.
Calcular os valores dos capacitores para um filtro com frequência de corte e fator de qualidade específicos.
Plotar a resposta em frequência do filtro.
Parâmetros
f: Frequência em Hz.
R: Resistência em Ohms.
C: Capacitância em Farads.
F: Frequência de corte em Hz.
Q: Fator de qualidade.
Funções
filtro_passa_baixas(f, R, C): Calcula a resposta em frequência do filtro.
calcular_capacitores(R, F, Q): Calcula o valor dos capacitores para um filtro com frequência de corte e fator de qualidade específicos.
funcao_transferencia(s, R, C1, C2): Monta a função de transferência do filtro.
Exemplo de uso
O código abaixo demonstra como usar as funções para calcular a resposta em frequência do filtro e plotar o gráfico:

Python

# Definindo os parâmetros

f = np.logspace(-1, 4, 1000) # Frequências de 0,1 Hz a 10 kHz
R = 100 # Resistência em Ohms
C = 110e-6 # Capacitância em Farads
F = 1.45 # Frequência de corte em Hz
Q = 0.707 # Fator de qualidade

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
Use o código com cuidado.
Observações
O código utiliza a biblioteca numpy para realizar cálculos numéricos e a biblioteca matplotlib para plotar gráficos.
A função funcao_transferencia(s, R, C1, C2) pode ser utilizada para analisar a resposta do filtro em frequência complexa.

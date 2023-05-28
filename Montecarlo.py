#Cálculo de la varianza con Monte Carlo

#Para la constante del resorte a partir de la gravedad y la pendiente del método estático
N = 10000
A = 2.93 + 0.02*np.random.randn(N)
G = 9.7968824 + 0.0000002*np.random.randn(N)
  
k = G * A

k_mean = np.mean(k)
sigma_k = np.std(k)

print(k_mean, sigma_k)



#Para la longitud natural del resorte en el método estático
N = 10000
B = -1.023 + 0.009*np.random.randn(N)
G = 9.7968824 + 0.0000002*np.random.randn(N)
K = 28.7 + 0.2*np.random.randn(N)

l0 = -B * G / K

l0_mean = np.mean(l0)
sigma_l0 = np.std(l0)

print(l0_mean, sigma_l0)


#Para la constante del resorte en el método dinámico
N = 10000
A = 0.033988108 + 0.000000002*np.random.randn(N)
  
k = 1 / A

k_mean = np.mean(k)
sigma_k = np.std(k)

print(k_mean, sigma_k)

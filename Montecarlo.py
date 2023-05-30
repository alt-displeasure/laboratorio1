#Cálculo de la varianza con Monte Carlo
#Algunos de los calculos utilizados en el reporte:

#Para la constante del resorte a partir de la gravedad y la pendiente del método estático
n = 10000
A = 2.95466 + 0.00007*np.random.randn(n)
G = 9.7968824 + 0.0000002*np.random.randn(n)

K_1 = A*G

k_1 = np.mean(K_1)
sigma_k1 = np.std(K_1)

print(k_1, sigma_k1)



#Para la longitud natural del resorte en el método estático
N = 10000
K = 28.9465 + 0.0007*np.random.randn(N)
B = -1.03594 + 0.00003*np.random.randn(N)
G = 9.7968824 + 0.0000002*np.random.randn(N)
  
l_0 = -1*B*G/K

l0_mean = np.mean(l_0)
sigma_l0 = np.std(l_0)

print(l0_mean, sigma_l0)


#Para la constante del resorte en el método dinámico, con la masa del resorte incluida
N = 10000
A = 0.033988108 + 0.000000002*np.random.randn(N)
  
k = 1 / A

k_mean = np.mean(k)
sigma_k = np.std(k)

print(k_mean, sigma_k)

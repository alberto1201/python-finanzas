import matplotlib.pyplot as plt
import numpy as np

# ── CAP 1: MATPLOTLIB ────────────────────────────


precios = [142.5, 145.3, 143.8, 147.2, 149.6]
dias = ["Lun", "Mar", "Mie", "Jue", "Vie"]

plt.plot(dias, precios, color="blue", linewidth=2)
plt.title("Precio AAPL - Semana")
plt.savefig("bloque_01_python_foundations/imagenes/s04_repaso.png")
plt.close()


# ── CAP 2: DICCIONARIOS ────────────────────────────
portafolio = {
    "AAPL": 149.6,
    "MSFT": 427.2,
    "TSLA": 245.5
}

portafolio["GOOGL"] = 175.3
del portafolio["TSLA"]
print("Portafolio:", portafolio)


# ── CAP 3: CONTROL FLOW ───────────────────────────
for ticker, precio in portafolio.items():
    if precio > 300:
        print(f"{ticker}: CARO - ${precio}")
    elif precio > 170:
        print(f"{ticker}: Normal - ${precio}")
    else:
        print(f"{ticker}: BARATO - ${precio}")


# ── CAP 4: LOOPS ──────────────────────────────────
retornos = [0.012, -0.005, 0.023, 0.008]
total = 0
for r in retornos:
    total += r
print(f"Retorno acumulado: {round(total * 100, 2)}%")


# ── CAP 5: HACKER STATISTICS ──────────────────────
np.random.seed(42)
random_walk = [0]
for x in range(100):
    step = random_walk[-1]
    dice = np.random.randint(1, 7)
    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1, 7)
    random_walk.append(step)
print(f"Piso final tras 100 lanzamientos:  {random_walk[-1]}")

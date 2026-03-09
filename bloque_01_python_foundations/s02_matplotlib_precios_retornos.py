import matplotlib.pyplot as plt
dias = ["Lun", "Mar", "Mier", "Jue", "Vie"]
precios = [182.5, 184.2, 183.8, 186.1, 185.4]


plt.plot(dias, precios)
plt.title("Precios AAPL")
plt.xlabel("Dia")
plt.ylabel("Precio USD")
plt.plot(dias, precios, color="royalblue",
         marker="o", linewidth=2, label="AAPL")
plt.plot(dias, [415, 417, 416, 419, 418], color="tomato",
         marker="s", linewidth=2, label="MSFT")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("mi_primera_grafica.png", dpi=150)


plt.grid(True)
plt.legend()
plt.show()

import pandas as pd
precios = {"AAPL": 191.8, "MSFT": 427.2, "TSLA": 245.5}

print(precios["AAPL"])
print(precios["TSLA"])
print()
print(list(precios.keys()))
print(list(precios.values()))

precios["GOOGL"] = 175.3
del precios["TSLA"]
print(precios)

print()
print()
print()
print()
data = {
    "ticker": ["AAPL", "MSFT", "GOOGL"],
    "precio": [191.8, 427.2, 175.3],
    "retorno": [0.556, 0.318, 0.421]
}

df = pd.DataFrame(data)
print(df)


print()


print(df["precio"])
print(df["retorno"].mean())

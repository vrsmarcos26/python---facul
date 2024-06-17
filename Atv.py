import matplotlib.pyplot as plt
import numpy as np
from pylab import rcParams

vendedores = ['João', 'Julia', 'Ana', 'José', 'Maria']
vendas = [100, 150, 1500, 2000, 120]

fig, ax = plt.subplots()

bars = ax.bar(vendedores, vendas, color='blue')

for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3), textcoords="offset points", ha="center", va="bottom")

ax.set_xlabel("Vendedores")
ax.set_ylabel("Vendas")
ax.set_title("Vendas por vendedor")

plt.show()

vendas_por_vendedor = dict(zip(vendedores, vendas))

vendedores_que_bateram_meta = [vendedor for vendedor, venda in vendas_por_vendedor.items() if venda >= 130]
vendedores_que_nao_bateram_meta = [vendedor for vendedor, venda in vendas_por_vendedor.items() if venda < 130]

print("")

print("Esses serão os vendedores que ganharam bonus por baterem a meta:")

for vendedor in vendedores_que_bateram_meta:
    venda = vendas_por_vendedor[vendedor]
    print(f"O vendedor (a) {vendedor} atingiu a meta e vendeu {venda}")
    print("")


print("Esses são os vendedores que não ganharam bonus por não baterem a meta:")

for vendedor in vendedores_que_nao_bateram_meta:
    venda = vendas_por_vendedor[vendedor]
    print(f"O vendedor (a) {vendedor} não atingiu a meta e vendeu {venda}")
    print("")

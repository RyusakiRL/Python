products = [
    {"nome": "Maçã", "preco": 5.0, "categoria": "Fruta"},
    {"nome": "Cenoura", "preco": 3.0, "categoria": "Vegetal"},
    {"nome": "Banana", "preco": 4.0, "categoria": "Fruta"},
    {"nome": "Brócolis", "preco": 6.0, "categoria": "Vegetal"},
]
def shop_product(dic, tgroup):
        
    if tgroup == "yes":
        groups = {}

        for prdct in dic:
            cat = prdct["categoria"]
            nam = prdct["nome"]

            if cat not in groups:
                groups[cat] = []

            groups[cat].append(nam)
        
        return groups
    else:
        return "Group not solicited"

group = input("You want group the list? (yes/no)\n").lower()

results = shop_product(products, group)

print(results)
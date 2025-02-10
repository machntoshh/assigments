# Eu posso fazer listas de dois jeitos em Python

# 1 -----------------------------------
classes = ["Arcane", "Fire", "Frost"]

# 2 -----------------------------------
spells = [
    "Arcane Blast",
    "Arcane Missile",
    "Arcane Barrage",
    "Touch of the Magi"
]


# ---------------------------- * Espaço * ---------------------------------------

# Tudo em qualquer linguagem de programação começa com a contagem em 0 e não em 1

# Se eu quiser pegar o 2 index de uma lista eu preciso fazer o seguinte
shitpost = ["Mogar", "Poggers", "Noggers"]
print(shitpost[1]) # 1 no caso seria o 2 e o 0 é o 1

#------------------------------ Exercício Boot.dev ------------------------------

def get_leather_scraps():
    inventory = [
        "Healing Potion",
        "Leather Scraps",
        "Iron Helmet",
        "Bread",
        "Shortsword",
    ]

    item_index = 1

    return inventory[item_index]
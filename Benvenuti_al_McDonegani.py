# Benevenuti_al_McDonegani_esteso.py
import datetime as dt
import matplotlib.pyplot as plt

# Dizionario per contare le vendite per fascia oraria
vendite_orarie = {
    "Mattina (6-12)": 0,
    "Pomeriggio (12-18)": 0,
    "Sera (18-24)": 0,
    "Notte (0-6)": 0
}

def determina_fascia_oraria(orario):
    ora = orario.hour
    if 6 <= ora < 12:
        return "Mattina (6-12)"
    elif 12 <= ora < 18:
        return "Pomeriggio (12-18)"
    elif 18 <= ora < 24:
        return "Sera (18-24)"
    else:
        return "Notte (0-6)"

# Inizio processo di vendita
print("Benvenuto al McDonald's!")
print("Scegli il tuo piano:")
print("1. Hamburger - 5€")
print("2. Cheeseburger - 4.5€")
print("3. Chicken Sandwich - 6€")
piano = int(input("Inserisci il numero della tua scelta: "))

print("\nScegli il tuo secondo:")
print("1. Patatine fritte - 2€")
print("2. Anelli di cipolla - 2.5€")
print("3. Insalata - 3€")
secondo = int(input("Inserisci il numero della tua scelta: "))

print("\nScegli il tuo dessert:")
print("1. Gelato - 3€")
print("2. Torta al cioccolato - 3.5€")
print("3. Mela cotta - 2.5€")
dessert = int(input("Inserisci il numero della tua scelta: "))

# Rilevamento orario vendita
orario_input = input("\nInserisci l'orario della vendita (formato HH:MM, 24 ore): ")
orario_vendita = dt.datetime.strptime(orario_input, "%H:%M")
fascia = determina_fascia_oraria(orario_vendita)
vendite_orarie[fascia] += 1

# Determinazione dei prezzi
menu = [
    ("Hamburger", 5), ("Cheeseburger", 4.5), ("Chicken Sandwich", 6)
]
contorni = [
    ("Patatine fritte", 2), ("Anelli di cipolla", 2.5), ("Insalata", 3)
]
dolci = [
    ("Gelato", 3), ("Torta al cioccolato", 3.5), ("Mela cotta", 2.5)
]

piano_scelto, prezzo_piano = menu[piano - 1]
secondo_scelto, prezzo_secondo = contorni[secondo - 1]
dessert_scelto, prezzo_dessert = dolci[dessert - 1]

totale = prezzo_piano + prezzo_secondo + prezzo_dessert

# Riepilogo ordine
print("\nHai scelto:")
print(f"Piano: {piano_scelto} - {prezzo_piano}€")
print(f"Secondo: {secondo_scelto} - {prezzo_secondo}€")
print(f"Dessert: {dessert_scelto} - {prezzo_dessert}€")
print(f"\nTOTALE DA PAGARE: {totale}€")
print(f"Orario di vendita registrato: {orario_input} - Fascia: {fascia}")

# Visualizzazione istogramma
fasce = list(vendite_orarie.keys())
quantita = list(vendite_orarie.values())

plt.figure(figsize=(10, 6))
plt.bar(fasce, quantita, color='skyblue')
plt.title("Vendite per fascia oraria")
plt.xlabel("Fascia oraria")
plt.ylabel("Numero di menu venduti")
plt.grid(axis='y')
plt.tight_layout()
plt.show()

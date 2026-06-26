#INPUT

pronouns = ["Yo", "Tu", "El", "Nosotros", "Vosotros", "Ellos"]

endings = {
    "ar": ["o", "as", "a", "amos", "ais", "an"],
    "er": ["o", "es", "e", "emos", "eis", "en"],
    "ir": ["o", "es", "e", "imos", "is", "en"]
}

verb = input("Write a Spanish verb (ar/er/ir): ").lower()

# PROCESS

stem = verb[:-2]
ending = verb[-2:]

if ending in endings:

    conjugation = endings[ending]

    # OUTPUT

    print("\nConjugated verb:\n")

    for i in range(len(pronouns)):
        print(pronouns[i], stem + conjugation[i])

else:
    print("Invalid verb. Please enter a verb ending in ar, er, or ir.")

# INPUT
action = input("Enter a verb: ")

# PROCESS

# List of pronouns
pronouns = ['yo', 'tu', 'el', 'nosotros', 'vosotros', 'ellos']

# Dictionary of verb endings
endings = {
    'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
    'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
    'ir': ['o', 'es', 'e', 'imos', 'is', 'en']
}

# Get the verb stem and ending
stem = action[:-2]
verb_type = action[-2:]

# Select the corresponding endings
selected_endings = endings[verb_type]

# OUTPUT
for index, pronoun in enumerate(pronouns):
    suffix = selected_endings[index]
    print(f"{pronoun} {stem}{suffix}")

# AI DECLARATION
# I only used AI to help me with my code.

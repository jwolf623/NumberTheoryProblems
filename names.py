male_names = { 'John', 'Bailey', 'Charlie', 'Chuck', 'Michael', 'Samuel', 'Jayden', 'Aiden', 'Henry', 'Lucas' }
female_names = { 'Elizabeth', 'Meghan', 'Kim', 'Khloe', 'Bailey', 'Jayden', 'Aiden', 'Britney', 'Veronica', 'Maria' }

# Use set methods to create sets all_names, neutral_names, and specific_names.
all_names=female_names.union(male_names)
specific_names=female_names.difference(male_names, female_name)
neutral_names=male_names.intersection(female_names)

print(sorted(all_names))
print(sorted(neutral_names))
print(sorted(specific_names))

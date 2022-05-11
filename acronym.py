phrase=input()
acronym=''

l=phrase.split()

for word in l:
    first_letter=word[0:1]
    if first_letter.isupper():
        acronym+=first_letter

print(acronym)

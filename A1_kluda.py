skaits = 0

with open('sistema.log', encoding='utf-8') as f:
    for rinda in f:
        if 'Critical' in rinda:
            skaits += 1

print('CRITICAL rindas:', skaits)



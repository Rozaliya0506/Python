from sys import argv
vyrabotka = int(argv[1])
hours = int(argv[2])
premiya = int(argv[3])
result = f'Zarabotnaya plata sostavit {(vyrabotka * hours) + premiya}'
print(result)

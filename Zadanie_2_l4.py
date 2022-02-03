ish_spisok = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [ish_spisok[i] for i in range(1, len(ish_spisok)) if ish_spisok[i] > ish_spisok[i-1]]
print(new_list)

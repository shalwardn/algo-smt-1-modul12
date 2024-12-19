#Latihan 1 - Shalwa Ridani

import pandas as pd

df = pd.read_csv(r"C:\Users\shalw\OneDrive\Documents\TRISAKTI\semester 1\algoritma & pemrograman\praktek anjaayy\vscode python\kelas\Negara - Negara.csv")

mean = df.groupby('Benua').mean(numeric_only=True)
std = df.groupby('Benua').std(numeric_only=True)

print(df.head())
print('\nBerikut Mean Benua nya\n')
print(mean)
print('\nBerikut Standar Devisasi nya\n')
print(std)

#Latihan 2 - Shalwa Ridani

import pandas as pd

df = pd.read_csv(r"C:\Users\shalw\OneDrive\Documents\TRISAKTI\semester 1\algoritma & pemrograman\praktek anjaayy\vscode python\kelas\Negara - Negara.csv")

mean = df.groupby('Benua').mean(numeric_only=True)
std = df.groupby('Benua').std(numeric_only=True)

print(df.head())
print('\nBerikut Mean Benua nya\n')
print(mean)
print('\nBerikut Standar Devisasi nya\n')
print(std)

mean.to_csv(r"C:\Users\shalw\OneDrive\Documents\TRISAKTI\semester 1\algoritma & pemrograman\praktek anjaayy\vscode python\kelas\NegaraMean.csv", index=True)
std.to_csv(r"C:\Users\shalw\OneDrive\Documents\TRISAKTI\semester 1\algoritma & pemrograman\praktek anjaayy\vscode python\kelas\NegaraStandarDeviasi.csv", index=True)

print("\nMean dan Standar Deviasi berhasil disimpan ke dalam file csv")
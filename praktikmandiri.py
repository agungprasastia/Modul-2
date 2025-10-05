import pandas as pd
import numpy as np

nama_file = 'car_data.csv' 
df = pd.read_csv(nama_file)

bentuk_awal = df.shape

#print("Bentuk Awal Dataset:", bentuk_awal)
#print("\n===== 5 Baris Pertama (head()) =====")
#print(df.head())
#print("\n===== Informasi Umum (info()) =====")
#df.info()

#print("\n===== Jumlah Missing Values per Kolom =====")
#print(df.isnull().sum())

#mean_price = df['selling_price'].mean()
#df['selling_price'].fillna(mean_price, inplace=True)

#print("\n===== Missing Values Setelah Ditangani =====")
#print(df.isnull().sum())


#jumlah_duplikat = df.duplicated().sum()
#print(f"Jumlah baris duplikat yang ditemukan: {jumlah_duplikat}")

#if jumlah_duplikat > 0:
    #df.drop_duplicates(inplace=True)
    #print("Baris duplikat telah dihapus.")
#else:
    #print("Tidak ditemukan data duplikat.")


#batas_outlier = 4000000 
#outliers = df[df['selling_price'] > batas_outlier]
#print(f"Ditemukan {len(outliers)} baris outlier dengan harga > {batas_outlier}")

#df = df[df['selling_price'] <= batas_outlier]
#print(f"-> Hasil: Outlier telah dihapus. Data sekarang hanya berisi mobil dengan harga <= {batas_outlier}.")



#print("Nilai unik di kolom 'fuel' SEBELUM standarisasi:")
#print(df['fuel'].unique())

#df['fuel'] = df['fuel'].str.lower()

#print("\nNilai unik di kolom 'fuel' SETELAH standarisasi:")
#print(df['fuel'].unique())
#print("-> Hasil: Kolom 'fuel' telah distandarisasi ke format lowercase.")

bentuk_akhir = df.shape
baris_dihapus = bentuk_awal[0] - bentuk_akhir[0]

print(f"Ukuran Awal  : {bentuk_awal[0]} baris, {bentuk_awal[1]} kolom")
print(f"Ukuran Akhir : {bentuk_akhir[0]} baris, {bentuk_akhir[1]} kolom")
print(f"Total baris yang dihapus selama pembersihan: {baris_dihapus}")
import gspread

# Kimlik doğrulama bilgilerini yükleyin
credentials = 'C:\Users\a\Desktop\wRhere_crm_Project\wrherecrmproject-609f4fae20b3.json' 
# Gspread ile oturumu başlatın
gc = gspread.service_account(filename=credentials)
# Google Sheets elektronik tabloyu açın
spreadsheet = gc.open('Kullanicilar')
# Çalışma sayfasını seçin
worksheet = spreadsheet.get_worksheet(0)  # İstenilen çalışma sayfasının indeksini değiştirin

# Şimdi, çalışma sayfası ile çalışabilirsiniz
cell_value = worksheet.acell('A1').value
print(f'A1 Hücresi Değeri: {cell_value}')

# Belirli bir satırı okuma (örneğin, 2. satır)
row_values = worksheet.row_values(2)
print(f'2. Satır Değerleri: {row_values}')

# Belirli bir sütunu okuma (örneğin, A sütunu)
column_values = worksheet.col_values(1)
print(f'A Sütunu Değerleri: {column_values}')

all_values = worksheet.get_all_values()

print(all_values[0][1])

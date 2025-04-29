from model import *

print(df_odi.head())
splited_text = []
for i in df_odi.Opposition:
    splited_text.append(i[2:].capitalize())
df_odi.Opposition = splited_text

print(df_odi.Opposition)
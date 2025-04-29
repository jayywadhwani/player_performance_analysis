from model import *

splited_text = []
for i in df_t20.Opposition:
    splited_text.append(i[2:].capitalize())
df_t20.Opposition = splited_text

print(df_t20.Opposition)
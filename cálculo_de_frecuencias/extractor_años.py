import pandas as pd
df = pd.read_excel("/Users/martagcasado/Desktop/pol/hysterisch_sustantivo_clasificado.xlsx")
df['año'] = df['nombre del documento'].str[:4].astype(int)
df.to_excel("/Users/martagcasado/Desktop/pol/hysterisch_sustantivo_classificado_ano.xlsx", index=False)
print("Done")

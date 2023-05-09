import pandas as pd



df = pd.read_csv("https://github.com/0xperp/defi-derivatives.git");
df['context'] = df.title + "\n" + df.heading + "\n\n" + df.content
df.head()

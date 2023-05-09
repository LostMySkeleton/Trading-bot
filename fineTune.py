import openai
import pandas as pd
from sklearn.model_selection import train_test_split
#anywhere it has a reference to "olympics..." -> change to actual file name/id once data has been read in


df = pd.read_csv('olympics-data/olympics_qa.csv')
olympics_search_fileid = "file-c3shd8wqF3vSCKaukW4Jr1TT"
df.head()

#from sklearn.model_selection import train_test_split

train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)
len(train_df), len(test_df)

df.context.str.contains('->').sum()

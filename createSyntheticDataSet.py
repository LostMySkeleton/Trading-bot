import openai
from readInData import *
#fix cropped lines
#anywhere it has a reference to "olympics..." -> change to actual file name/id once data has been read in

def get_questions(context):
    try:
        response = openai.Completion.create(
            engine="davinci-instruct-beta-v2",
            prompt=f"Write questions based on the text below\n\nText: {context}\n\nQuestions:\n1.",
            temperature=0,
            max_tokens=257,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["\n\n"]
        )
        return response['choices'][0]['text']
    except:
        return ""


df['questions']= df.context.apply(get_questions)
df['questions'] = "1." + df.questions
print(df[['questions']].values[0][0])
print(df.content.values[0])


def get_answers(row):
    try:
        response = openai.Completion.create(
            engine="davinci-instruct-beta-v2",
            prompt=f"Write questions based on the text below\n\nText: {row.context}\n\nQuestions:\n{row.questions}\n\nAnswers:\n1.",
            temperature=0,
            max_tokens=257,

            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response['choices'][0]['text']
    except Exception as e:
        print (e)
        return ""


df['answers']= df.apply(get_answers, axis=1)
df['answers'] = "1." + df.answers
df = df.dropna().reset_index().drop('index',axis=1)
print(df[['answers']].values[0][0])


#change

df.to_csv('olympics-data/olympics_qa.csv', index=False)

#search file
df = df[df.tokens<2000]
df[['context', 'tokens']].rename(columns={'context':'text','tokens':'metadata'}).to_json('olympics-data/olympics_search.jsonl', orient='records', lines=True)

search_file = openai.File.create(
    file=open("olympics-data/olympics_search.jsonl"),
    purpose='search'
)
olympics_search_fileid = search_file['id']


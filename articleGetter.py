from newspaper import Article

url = "https://incentivized.substack.com/p/how-convex-stacked-as-much-crv-as"

article = Article(url)

article.download()

article.parse()

f = open("output5.txt", "w")

data = article.text.split(".")

for i in data:
    f.write(i + "\n")

f.close()


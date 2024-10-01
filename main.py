import pandas as pd

df = pd.read_csv("articles.csv")


class Article:
    def __init__(self, article_id):
        self.id = article_id
    
    def available(self):
        """Checks the availability of the article"""
        stock = df.loc[df['id'] == self.id, 'in stock'].squeeze()
        if stock > 0:
            return True
        else:
            return False

    def buy(self):
        """Reduces the article stock by 1"""
        stock = df.loc[df['id'] == self.id, 'in stock']
        df.loc[df['id'] == self.id, 'in stock'] = stock - 1
        df.to_csv("articles.csv", index=False)


class Receipt:
    def __init__(self):
        pass


print(df)
article_id = int(input("Enter the article id: "))
article = Article(article_id)
if article.available:
    article.buy()

else:
    print("Article is not available!")

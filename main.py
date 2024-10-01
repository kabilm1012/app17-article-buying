import pandas as pd
from pdf import create_pdf

df = pd.read_csv("articles.csv")


class Article:
    def __init__(self, article_id):
        self.id = article_id
        self.name = df.loc[df['id'] == self.id, 'name'].squeeze()
        self.price = df.loc[df['id'] == self.id, 'price'].squeeze()
    
    def available(self):
        """Checks the availability of the article"""
        stock = df.loc[df['id'] == self.id, 'in stock'].squeeze()
        return stock

    def buy(self, stock):
        """Reduces the article stock by 1"""
        df.loc[df['id'] == self.id, 'in stock'] = stock - 1
        df.to_csv("articles.csv", index=False)


class Receipt:
    def __init__(self, article_object):
        self.article_object = article_object

    def receipt_pdf(self):
        article_name = self.article_object.name
        article_price = self.article_object.price
        create_pdf(article_name, article_price)


print(df)
article_id = int(input("Enter the article id: "))
article = Article(article_id)
stock = article.available()
if stock:
    article.buy(stock)
    receipt = Receipt(article_object=article)
    receipt.receipt_pdf()
else:
    print("Article is not available!")

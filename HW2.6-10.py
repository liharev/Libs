#Работа с данными в Pandas
#Задание 1
import pandas as pd
authors = pd.DataFrame({
                       "author_id": [1, 2, 3],
                       "author_name":['Тургенев', 'Чехов', 'Достоевский']
                        })
book = pd.DataFrame({
                    "author_id": [1, 1, 1, 2, 2, 3, 3],
                    "book_title": ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой',
                                   'Гроза', 'Таланты и поклонники'],
                    "price": [450, 300, 350, 500, 450, 370, 290]
                    })
#Задание 2
author_price = pd.merge(authors, book, on='author_id', how='inner')
#Задание 3
top5 = author_price.nlargest(5, "price")
#Задание 4
author_price["min_price"] = author_price["price"]
author_price["max_price"] = author_price["price"]
author_price["mean_price"] = author_price["price"]
author_stat = author_price.groupby("author_name").agg({"min_price": "min", "max_price": "max", "mean_price": "mean"})
#Задание 5*
cover = pd.Series(['твердая', 'мягкая', 'мягкая', 'твердая', 'твердая', 'мягкая', 'мягкая'])
author_price["cover"] = cover.values
import numpy as np
book_info = pd.pivot_table(author_price,
               index = ["author_name"],
               columns = ["cover"],
               values = ["price"],
               aggfunc = np.sum)
book_info.to_pickle("book_info.pkl")
book_info2 = pd.read_pickle("book_info.pkl")
print(book_info.equals(book_info2))

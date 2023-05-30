import pandas
import random

# words_df = pandas.read_csv("data/french_words.csv")
# to_learn = words_df.to_dict(orient="records")
# # random_card = random.choice(to_learn)
# # random_french = random_card["French"]
# # random_english = random_card["English"]
#
# print(len(to_learn))
#
# to_learn = [i for i in to_learn if not (i['English'] == "part")]
# print(len(to_learn))
#
# try:
#     with open("words_to_learn.csv", "r") as file:
#         contents = file.read()
# except FileNotFoundError:
#     print("file not fouond")

updated_words_df = pandas.read_csv("words_to_learn.csv")
import pandas as pd

data = pd.read_csv("artikeln.csv", names=["Line"])
word = input("What is the word you're looking for?\n>")

matching_line = str(data[data["Line"].str.contains(rf"\b{word}\b", na=False, case=False)]["Line"])
artikel = matching_line.split()[1]

artikel_dict= {
    "der": "NOM: der\nAKK: den\nDAT: dem",
    "die": "NOM: die\nAKK: die\nDAT: der/den",
    "das": "NOM: das\nAKK: das\nDAT: dem"
}

print(artikel_dict[artikel])
if artikel == "die":
    print("this part needs to be upgrated and currently the plurals and femenines aren't seperated.")

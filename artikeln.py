import pandas as pd
import csv

file_path = "artikeln.csv"
df = pd.read_csv(file_path)
data = pd.read_csv(file_path, names=["Line"])
word = input("What is the word you're looking for?\n>")

matching_line = str(data[data["Line"].str.contains(rf"\b{word}\b", na=False, case=False)]["Line"])
artikel = matching_line.split()[1]

artikel_dict= {
    "der": "NOM: der\nAKK: den\nDAT: dem",
    "die": "NOM: die\nAKK: die\nDAT: der/den",
    "das": "NOM: das\nAKK: das\nDAT: dem"
}

print(artikel_dict[artikel])

#this is so that I wouldn't forget to fix this problem.
if artikel == "die":
    print("this part needs to be upgrated and currently the plurals and femenines aren't seperated.")

def add_word(file_path, new_row):
    with open(file_path, 'a', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow(new_row)

last_number = df.iloc[-1, 0] 
new_row = [last_number + 1, "das", "Sakko"]
add_word(file_path, new_row)
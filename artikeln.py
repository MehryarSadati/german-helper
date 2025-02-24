import pandas as pd
import csv

print("In case you wanna exit the program type \"exit\"\n")

file_path = "artikeln.csv"
df = pd.read_csv(file_path)
data = pd.read_csv(file_path, names=["Line"])

artikel_dict= {
    "der": "NOM: der\nAKK: den\nDAT: dem",
    "die": "NOM: die\nAKK: die\nDAT: der/den",
    "das": "NOM: das\nAKK: das\nDAT: dem"
}

def add_word(file_path, new_row):
    with open(file_path, 'a', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow(new_row)

def exit(input):
    if input.lower() == "exit":
        return True
    
# running = True

# while running:
program_input = input("What is the word you're looking for?\n>")

# if exit(program_input):
#     running = False

matches = data[data["Line"].str.contains(rf"\b{program_input}\b", na=False, case=False)]["Line"]
if matches.empty:
    ask = input("If you know the artikel of this word you can add it to the dataset; would you like to? (y/n)")
    
    if ask.lower() == "y":
        last_number = df.iloc[-1, 0] 
        artkl = input(f"What is the artikel of the word {program_input}?")
        new_row = [last_number + 1, artkl, program_input.title()]
        add_word(file_path, new_row)
    elif ask.lower() == "n":
        pass
    else:
        print("Wrong input")
        # question()
    
else:
    matching_line = str(matches)
    artikel = matching_line.split()[1]
    print(artikel_dict[artikel])

    #this is so that I wouldn't forget to fix this problem.
    if artikel == "die":
        print("this part needs to be upgrated and currently the plurals and femenines aren't seperated.")
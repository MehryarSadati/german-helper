# german-helper

A simple tool for looking up and adding German noun articles (der, die, das).

## Overview

This repository contains a Python-based tool to help German language learners look up the correct articles for German nouns. German nouns have one of three grammatical genders (masculine, feminine, or neuter), represented by the articles "der", "die", and "das". This tool allows you to quickly check the correct article for a word or add new words to your collection.

## Files

- **artikeln.py**: Python script that runs the article lookup program
- **artikeln.csv**: CSV file containing German nouns and their correct articles
- **main.py**: This file will be uploaded as soon as possible.

<!-- ## Usage

1. Ensure you have Python installed on your system
2. Clone the repository:
   ```
   git clone https://github.com/MehryarSadati/german-helper.git
   ```
3. Navigate to the repository folder:
   ```
   cd german-helper
   ```
4. Run the script:
   ```
   python artikeln.py
   ``` -->

## How It Works

The program works as follows:
1. You type a German noun in the input prompt
2. If the word exists in the artikeln.csv dataset, the program displays the correct article (der, die, or das plus the Akkusativ and Dativ artikel) for that noun
3. If the word is not in the dataset, you have the option to add it yourself along with its correct artikel
4. The new entries are saved to the artikeln.csv file for future reference

This makes it both a lookup tool and a way to build your personalized German noun database over time.

## Example Usage

Here's how the program looks in action:

```
$ python artikeln.py
>>>In case you wanna exit the program type "exit".
>>>Enter a German noun: 
Haus
The article for 'Haus' is: das

Enter a German noun (or 'exit' to quit): Tisch
The article for 'Tisch' is: der

Enter a German noun (or 'exit' to quit): Blume
The article for 'Blume' is: die

Enter a German noun (or 'exit' to quit): Handy
'Handy' not found in the database.
Would you like to add it? (y/n): y
Enter the article for 'Handy' (der/die/das): das
'Handy' has been added to the database with article 'das'.

Enter a German noun (or 'exit' to quit): Stift
'Stift' not found in the database.
Would you like to add it? (y/n): n
'Stift' was not added to the database.

Enter a German noun (or 'exit' to quit): exit
Auf Wiedersehen!
```

## Customizing the Word List

You can directly edit the artikeln.csv file to add more nouns or modify existing entries:
- Each line should contain the article and noun, separated by a comma
- Format: `article,noun` (e.g., `der,Mann`, `die,Frau`, `das,Kind`)

<!-- ## Requirements

- Python 3.x -->

## Contributing

Feel free to contribute by:
- Adding more words to the artikeln.csv file
- Improving the artikeln.py script
- Suggesting new features related to article lookup and storage

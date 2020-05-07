# Colemak Layout Trainer
A simple CLI-based colemak trainer implemented in Python. The current error metric is absolute number of incorrect words.

# Current Usage
Currently, running main.py will generate 10 words between 0-4 letters long using letters only found on the home row of
the colemak layout.
'''
python main.py
'''
# TODO
* different error metric, probably Levenshtein distance
* command-line parameters to control length, number of words and home row only
* quick redo last set

# Maybe implement
* history of incorrect words
* GUI
..* Graphs showing progress over time

# Credits
Text Corpus:
google-10000-english-no-swears.txt from the following repo:
https://github.com/first20hours/google-10000-english

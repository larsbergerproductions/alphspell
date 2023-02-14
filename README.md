# alphspell.py
alphspell is a program that takes a string as input and returns it, but spelled
in a phonetic alphabet of user's choosing.

## dictionary files
alphspell accepts regular text csv files that contain a letter and a word
starting with that letter for each letter in the desired alphabet. If multiple
lines define the same letter, the last one is the only line used.

If the specified file is not found, program exits with code 1.

If the file contains more or less than 2 entries, program exits with code 2.

# potential road ahead
- morse code csv file
- write error messages to stderr
- CLI with ArgParse
- accept json files as input, too
"""
Import the text_utils module you created and calculate the average number of
words per line in a given text file. The text file that will be used to test
this is the text file called "sample.txt" (located in the same directory as
this exercise). The average number of words per line should be rounded down to
the nearest integer.

Print the average number of words per line in the text file in the following
format:

"Average words per line: [average]"
"""
import text_utils


def averages(filename):
  countl = 0
  countw = 0
  file = open(filename, 'r')

  for line in file.readlines():
    countl+=1                            #for each each line, add the line to line count and the word count to total word count
    countw+=text_utils.count_words(line)
  
  print(f"Average words per line: {int(countw/countl)}")   #Average 

averages('sample.txt')

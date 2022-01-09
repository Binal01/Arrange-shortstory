# write a program to arrange the sentences within the story in alphabetical order using Python.

def main():
  # open shortstory.text file in read mode
   inputFile = open("shortstory.txt", 'r')
  # Return all lines in the file as a list where each line is a item in the list object
   lineList = inputFile.readlines()
   # sort the line in a list and print it
   lineList.sort()
   print(lineList)
   for line in lineList:
    print(line)
    # open the file for writing and format string as f
   with open('shortstory.txt', 'a') as f:
     for line in lineList:
      lineList.sort()
      f.write(line)

main()
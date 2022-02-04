import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split(",")
  if (len(datalist) == 7) : 
    CourseName,University,DifficultyLevel,CourseRating,CourseURL,CourseDescription,Skills= datalist

    # print intermediate key-value pairs to standard output
    print(DifficultyLevel,"\t",1)
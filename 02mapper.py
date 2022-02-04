import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split(",")
  if (len(datalist) == 5) : 
    iso_code,continent,location,date,total_cases = datalist

    # print intermediate key-value pairs to standard output
    print (location,"\t", total_cases)
#open file in read mode
file = open("inputfile_16.txt", "r")

#read the content of file
data = file.read()

#get the length of the data
total = len(data)

print('Number of characters in text file :', total)
az="abcdefghijklmnopqrstuvwxyz"
pmf=[x for x in range(26)]
with file as f:
    for line in f:
        for k in range(len(line)):
            pmf[k]=sum(ischar(line,az[k])/total
            print(pmf)                
file.close()
    
                     
                     
            

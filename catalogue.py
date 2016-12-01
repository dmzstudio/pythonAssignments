data_file = open('data.txt', 'r')
cont_file = open('continent.txt', 'r')

catalogue = {}

line = data_file.readline()
line = data_file.readline()

contline = cont_file.readline()
contline = cont_file.readline()

while line != "" and contline != "" :
  catalogueList = []
  
  line = line.split('|')
  contline = contline.split(',')
  contline[1] = contline[1].rstrip('\n')
  line[1] = "".join(line[1].split(','))
  line[2] = "".join(line[2].split(',')).rstrip('\n')
  
  catalogueList.append(contline[1])
  catalogueList.append(line[1])
  catalogueList.append(line[2])
  
  catalogue[line[0]] = catalogueList
  
  line = data_file.readline()
  contline = cont_file.readline()
 
print(catalogue)


data_file.close()
cont_file.close()

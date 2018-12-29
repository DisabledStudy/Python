file = open('myfile.dat', 'w+')
file.write("this is the text")
file.flush()
file.close()

file2 = open('myfile.dat', 'r')
message = file2.read()
file.close()
print(message)
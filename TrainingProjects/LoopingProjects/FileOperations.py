file1=open("file1.txt","a")
file2=open("file2.txt","a")
file3=open("file3.txt","w")

print("Enter text for file 1:")
file1.write(input(">")+"\n")

print("Enter text for file 2:")
file2.write(input(">")+"\n")

file1=open("file1.txt","r")
file2=open("file2.txt","r")
file3.write(file1.read()+file2.read())

print("\nOutput after merging both the files:")
file3=open("file3.txt","r")
print(file3.read())
#write
f=open("file handling/file.txt","w")
f1=open("file handling/file1.txt","w")
l=["mamun\n","renesha\n","random"]
f.writelines(l)
f1.write("cse221")
#readind
f=open("file handling/file.txt","r")
f1=open("file handling/file1.txt","r")
# for i in f:
#     print(i)

# for i in f1:
#     print(i)

# # s=f.read()
# s1=f.read(5)
# s2=f.read(5)
# # s3=f.readline()
# # s4=f.readlines()
# print(s1,s2)
# # print(s1)
# # print(s3)
# # print(s4)
f.close()
f1.close()
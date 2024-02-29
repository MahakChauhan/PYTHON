#READING A FILE IS A DEFAULT MODE
# f=open("myfile.txt",'r')
# text=f.read()
# print(text)
# f.close()

#WRITING A FILE 
f=open("myfile.txt",'a')
f.write("Hey Mahak ")
f.close()

#Using with statement=we don't  need close method in this
with open('myfile.txt','a')as f:
    f.write("I am inside with")



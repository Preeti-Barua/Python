'''
f1=open("C:\\Users\\dell\\Desktop\\file.txt","w")
txt="hello this file is overwritten"
f1.write(txt)

f1.close()
'''
'''
f=open("C:\\Users\\dell\\Desktop\\file.txt","r")
f1=open("C:\\Users\\dell\\Desktop\\file1.txt","w")
txt=f.read()
f1.write(txt)
f.close()
f1.close()

str=input("enter a string:")
f1=open("C:\\Users\\dell\\Desktop\\file1.txt","a")
f1.write(str)
f1.close()
'''
f=open("C:\\Users\\dell\\Desktop\\1.png","rb")
f1=open("C:\\Users\\dell\\Desktop\\2.png","wb")
txt=f.read()
f1.write(txt)
f.close()
f1.close()


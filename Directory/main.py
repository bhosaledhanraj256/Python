# f= open('sample.txt','r')
# text=f.read()
# print(text)
# f.close()

f=open('sample2.txt','w')
f.write('Hello world!')
f.close()

f=open('sample2.txt','rb')
text=f.read()
print(text)
f.close()

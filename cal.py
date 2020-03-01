
from threading import*
a=5
b=2
class ad(Thread):
    def run(self):
        c=a+b
        print(c)
        
class sub(Thread):
    def run(self):
        c=a-b
        print(c)
        
        
class mul(Thread):
    def run(self):
        c=a*b
        print(c)
        
class div(Thread):
    def run(thread):
        c=a/b
        print(c)
        
a1=ad()
a1.start()
a2=sub()
a2.start()
a3=mul()
a3.start()
a4=div()
a4.start()






        

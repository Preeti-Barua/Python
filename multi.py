from time import*
from threading import*
class hi(Thread):
    def run (self):
        for i in range(5):
            print ("hello")
            sleep(2)
class hello(Thread):
    def run(self):
        for i in range(5):
            print("hi")
        
            sleep(2)
t1=hi()
t2=hello()
t1.start()
t2.start()
t1.join()
t2.join()
print("end of prg")

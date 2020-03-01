class Demo:
    c=0
    def __init__(self):
        print('object created')
        Demo.c+=1
    @staticmethod
    def noObject():
        print('no of object created:',Demo.c)
obj1=Demo()
obj2=Demo()
Demo.noObject()

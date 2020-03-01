'''class B1:
    def __init__(self):
        print("class B1")
class B2:
    def __init__(self):
        print("class B2")
class child(B2,B1):
    def __init__(self):
        super().__init__()
        print('child class')
c1=child()
print("---------------------------")'''
class B1:
    def __init__(self):
        print("classB1")
class B2:
    def __init__(self):
        print("class B2")
class B3:
    def __init__(self):
        print("class B3")
class child(B2,B3,B1):
    def __init__(self):
        super().__init__()
        B1.__init__(self)
        print("child class")
c1=child()


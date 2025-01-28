class A:
    def spam(self):
        print("hello")

class B(A):
    def spam(self):
        print("yellow")
        super().spam()

obj = B()
obj.spam()
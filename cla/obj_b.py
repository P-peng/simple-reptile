from cla.obj_a import A


class B(object):

    def __init__(self):
        print("123123123")
        self.a = A()
        print(self.a)

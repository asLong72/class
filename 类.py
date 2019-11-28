
#创建一个类
class Dog():                                
    """             """
    def __init__(self, a ,b , c):           #用于初始化这个类的实例(self)的属性self.xxx
                                            #需要传入的实参不包括self
        self.something1 = a
        self.something2 = b
        self.something3 = c

#使用这个类
my_dog=Dog('doge','3','male')               #为类的self的变量传入实参, 形成一个这个类的实例my_dog
#类是一种对象的模板和数据类型
#定义了对象的属性, 并提供用于初始化对象的初始化程序和操作这些属性的方法(函数)
#在py中变量, 函数, 类都是一种对象

#创建一个类(类名后方一对圆括号可有可无???)
class Dog:                                
    """             """
    def __init__(self, a ,b , c):           #__init__()函数用于初始化这个类的实例(self)的属性self.xxx( 必须存在, 且名字不可替换修改 )
                                            #需要传入的实参不包括self
        self.something1 = a
        self.something2 = b
        self.something3 = c

    def printsets(self):                    #定义一个操作这些属性的方法(函数)
                                            #self变量及其在调用这个函数前已经初始化的成员变量(属性), 在定义时传入self即可, 不用在运行程序中传入
        print(self.something1,self.something2,self.something3)

#使用这个类
my_dog=Dog('doge','3','male')               #为类的self的变量传入实参, 形成一个这个类的实例 / 对象: my_dog
my_dog.printsets()

#str(), int()均为类, 用于创建对应的对象 / 实例

#isinstance()
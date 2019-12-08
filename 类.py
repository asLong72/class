#类是一种对象的模板和数据类型
#定义了对象的属性, 并提供用于初始化对象的初始化程序和操作这些属性的方法(函数)
#在py中变量, 函数, 类都是一种对象

#创建一个类(类名后方的一对圆括号可有可无???)
class Dog:                                
    """             """
    price=10000                             #类变量
    @classmethod                            #定义类方法( 类方法无法访问实例变量 )

    def __init__(self, a , b , c, d = 0 ):  #__init__()函数用于初始化这个类的实例(self)的属性self.xxx( 必须存在, 且名字不可替换修改 )
                                            #同函数一样, 形参可赋予默认值, 在未传入对应实参时该形参为默认值
                                            #需要传入的实参不包括self
                                            #实例变量

        self.something1 = a                 #
                                            #带下划线的方法和变量的特殊意义
        _self.something2 = b                #受保护的成员,不能用'from module import *'导入
        __self.something3__ = c             #系统定义的成员
        __self.something4 = d               #私有成员,只有类内这就可以访问(类内的方法等),不能使用对象 / 实例直接访问这个成员


    def printsets(self):                    #定义一个操作这些属性的方法(函数)
                                            #self变量及其在调用这个函数前已经初始化的成员变量(属性), 在定义时传入self即可, 不用在运行程序中传入
        print(self.something1,self.something2,self.something3)

#使用这个类创建实例,修改和操作实例
my_dog=Dog('doge','3','male')               #为类的self的变量传入实参, 形成一个这个类的实例 / 对象: my_dog
my_dog.printsets()                          #调用类的函数

#其实str(), int()均为类, 用于创建对应的对象 / 实例
a=int(10)

#动态增加类变量: 类名.类变量名=xxx

#isinstance()                               #确认成员是否在该类中

#封装
#

#继承
#

#多态
#
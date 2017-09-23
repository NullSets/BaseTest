
#Python并没有提供定义常量的关键字
#定义一个常量模块
class _const():            #定义常量类_const
    class ConstError(TypeError): pass
    def __setattr__(self, name, value):
        if self.__dict__.get(name):
            raise self.ConstError( "Can't rebind const(%s)" % name)
        self.__dict__[name] = value

import sys
sys.modules[__name__] = _const()





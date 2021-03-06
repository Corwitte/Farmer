# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

class FirstEntity(KBEngine.Entity):
    """
    第一个实体的base部分的实现
    """
    def _init_(self):
        KBEngine.Entity.__init__(self)

    def hello(self, content):
        """
        say hello
        :param content:内容
        :return:
        """
        INFO_MSG("Hello ComblockEngine! I'm %s. I got your content=%s" % (self.name, content))
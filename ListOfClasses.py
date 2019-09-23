# coding:utf-8


class Clothes:
    def __init__(self, color, size, type):
        self.color = color
        self.size = size
        self.type = type

    def printMe(self):
        print(self.color + '的' + self.size + '的' + self.type)


clothes_list = [
    Clothes('白色', 'S号', '的白衬衫'),
    Clothes('蓝色', 'M号', '的蓝半袖'),
    Clothes('紫色', 'L号', '的紫卫衣')
]

for cloth in clothes_list:
    cloth.printMe()

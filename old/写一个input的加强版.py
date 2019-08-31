def top_input(a):
    if isinstance(a, str):
        temp = input(a)
        return print(temp)
    ex = Exception("数据异常")
    raise ex
        # return input(a)
try:
    temp2 = top_input("are you ok")
except Exception as result:
    print(result)
# temp1 = top_input("输入你的内容吧")
# print(temp2)
# print(temp1)
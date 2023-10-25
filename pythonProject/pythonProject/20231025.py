str_a = "abcdefg"
print(str_a[6])
print(str_a[1:5])
print("hogwarts teacher is %s"%"张家辉")
# demo = "hogwarts is a {}"
# demo_res = demo.format("school")
# print(demo_res)

demo = "hogwarts is a {0} {1}"  #demo是原始的变量内容
demo_res = demo.format("very good","school")  #demo_res是替换过后的变量内容
print(demo_res)

name = "Bob"
school = "hogwarts"
print(f"我的名字叫做{name}，毕业于{school}")   #通过 f"(变量名)

a = ["h","o","g","w","a","r","t","s"]
print("".join(a))
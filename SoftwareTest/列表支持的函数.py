#coding:utf-8
#1.append()函数：向列表追加元素（把元素加到列表末尾）
# 格式：变量名.append(新元素) 注：新元素只能传一个
a = [1,2,3,3,4,5]
a.append(6)
print a
#2. insert()函数：向列表插入元素（通过索引从指定位置插入）
#格式：变量名.insert(index,新元素)
a.insert(1,'tom')
print a
#3. count()函数:返回某个值在列表中出现的次数
#格式：变量名.count(元素)
print a.count(3)

#4.sorted()函数：内容排序
#格式：print sorted(变量名)
#先排列列表中的数字类型（从小到大），然后排列列表类型，再排列符号与字符串，当字符串
#为英文时则按照字母排序，先排序大写开头（A~Z），再排序小写（a~z），首字母相同则对比第二个字母，依次类推
#5.max()函数：列表中的最大值 max(变量名)
# min()函数：列表中的最小值
# len()函数：列表中数据个数
list =[1,1990,27,175.2,'Jack','JAckson','male',' ',[60,120],"中文"]
print list #原列表输出是根据顺序打印
print str(sorted(list)).decode('string-escape')
print max(list)
print min(list)
print len(list)

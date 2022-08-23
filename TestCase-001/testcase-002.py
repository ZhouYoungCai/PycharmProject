def reverseInteger(self, number):
    g = number%10 #取出个位数
    s = (int(number/10))%10 #取出十位数
    b = int(number/100) #取出百位数
return g*100+s*10+b
if __name__ == "__main__":
    so = Solution()
print (so.reverseInteger(123))
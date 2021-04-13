def numFlipOver(num:int) ->int:
    num = str(num)
    if num[0]=="-":
        num =int(num[:0:-1])
        print(-num)
    else:
        num = int(num[::-1])
        print(num)
        

if __name__ == "__main__":
    numFlipOver(-123)
    numFlipOver(345)
    numFlipOver(2)
    numFlipOver(120)
    numFlipOver(-256)
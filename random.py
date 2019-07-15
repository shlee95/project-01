import random

def rd_num(num):

    for k in range(0,num) :
        
        reg_no = []
        mul_factor = [1,3,7,1,3,7,1,3,5]
        sum = 0

        target1 = '110' #서울,경기청 고정

        target2 = random.randrange(1,79)
        target2 = str(target2).rjust(2,'0')

        target3 = random.randrange(0,9999)
        target3 = str(target3).rjust(4,'0')    

        result = ''
        result = str(target1) + str(target2) + str(target3)
        
        array = []
        for i in result:
            array.append(i)

        for idx, j in enumerate(array):
            a = int(j)*int(mul_factor[idx])
            sum = sum + a
        sum = sum + ((int(array[8]) * 5) / 10)

        sidliy = int( sum % 10 )

        if sidliy != 0:
            sum = 10-sidliy
        else:
            sum = 0
                   
        array.append(str(sum))
        b = ''.join(array)
        print(b)
    
rd_num(30)


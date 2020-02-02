def n2w(number):

    #if everything goes SMOOTH this function will return number in words
    #oterwise will print someting 

    
    #try to send number as a string it will be great
    #combiation of these will be used to generate numbers
    onedigi=[' ','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
    twodigi=[' ','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
    tenn=[' ','Ten','Twenty','Thirty','Fourty','Fifty','Sixty','Seventy','Eighty','Ninety']
    cur=[' ','','Hundred','Thousand','','Lakh','','Crore']
    #taking care of number before supplying it into main block
    #number=input("enter a number:")
    try:
        if(number==''):
            print('NaN')
        elif(int(number)==0):
            print('Zero')
            number=''
        else:
            for i in range(len(number)):
                if number[i]!='0':
                    number=number[i:]
                    break

        #main block starts HERE...
        
        if(len(number)<=9):
            word=''
            i=len(number)

            while i>0:
                if(int(number)==0):
                    number=''
                elif(int(number)%10==0 and int(number)<100 ):
                    word=word+tenn[int(number)//10]+' '
                    if(len(number)<=3):
                        number=''
                    else:
                        number=number[-i+1:]

                elif(int(number)>10 and int(number)<20 ):
                    if(twodigi[int(number)%10]!=' '):
                        word=word+twodigi[int(number)%10]+' '
                        if(len(number)<=3):
                            number=''
                        else:
                            number=number[-i+1:]
                elif(i==1):
                    word=word+onedigi[int(number[-1*i])]
                    number=''
                    
                elif(i==2):
                    word=word+tenn[int(number[-1*i])]+' '
                    number=number[-i+1:]
                    
                elif(i==3):
                    if(onedigi[int(number[-1*i])]!=' '):
                        word=word+onedigi[int(number[-1*i])]+' '
                        word=word+cur[i-1]+' '
                    number=number[-i+1:]
                    
                elif(i==4):
                    if(onedigi[int(number[-1*i])]!=' '):
                        word=word+onedigi[int(number[-1*i])]+' '
                        word=word+cur[i-1]+' '
                    number=number[-i+1:]
                
                elif(i==5 or i==7 or i==9):
                    if(int(number[-i:-i+2])%10==0 and int(number[-i:-i+2])<100 ):
                        word=word+tenn[int(number[-i:-i+2])//10]+' '
                        number=number[-i+2:]
                    elif(int(number[-i:-i+2])>10 and int(number[-i:-i+2])<20 ):
                        if(twodigi[int(number[-i:-i+2])%10]!=' '):
                            word=word+twodigi[int(number[-i:-i+2])%10]+' '
                            number=number[-i+2:]
                    else:
                        word=word+tenn[int(number[-i:-i+2])//10]+' '
                        word=word+onedigi[int(number[-i+1])]+' '
                        number=number[-i+2:]
                    word=word+cur[i-2]+' '

                elif(i==6):
                    if(onedigi[int(number[-i])]!=' '):
                        word=word+onedigi[int(number[-i])]+' '
                        word=word+cur[i-1]+' '
                    number=number[-i+1:]

                elif(i==8):
                    if(onedigi[int(number[-i])]!=' '):
                        word=word+onedigi[int(number[-i])]+' '
                        word=word+cur[i-1]+' '
                    number=number[-i+1:]

                for i in range(len(number)):
                    if number[i]!='0':
                        number=number[i:]
                        break
                i=len(number)

                
            return word
    except:
        print("AHHAHH!! somethings FISHY HERE")
            
    else:
        print("wohhh!! TOO MANY NUMBERS ")

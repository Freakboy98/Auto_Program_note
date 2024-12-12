# 오늘의 주인송은?

import random

def main() :
    number = int(input("몇명이 참여하나요? : "))
    

    name_list = []
    for itr in range(number) :
        name = input("이름을 입력해 주세요! \n 이름 : ")
        name_list.append(name)
    
    print(name_list)

    print("오늘의 주인공은?....두구두구두구...")

    rand_val = random.randint(0, number-1)
    
    print("축하합니다! 오늘의 주인공은",name_list[rand_val],"입니다!")
    return None
if __name__ == "__main__" :
    main()
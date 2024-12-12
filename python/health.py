chest = ["chest_press",[0.6],"incline_bench_preee",[0.4], "dumbBell_press",[0.1], "cable_fly",[0.1]]
back = ["pull-up","deadLift","DumbBell-row","LetPullDown","Seated-row"]
Leg = ["squrt","Leg-Press","Leg-Extension","Back-Extension"]
pound = 0
reps = 0
routine = ""

class Person() :
    kg = 0

    def __init__(self, *args) :
        self.h = 0.0
        self.w = 0.0
        self,s = None
        pass

    def print(self) :
        if self.s == 0:
            s = "male"
        else:
            s = "Female"
        print(self.h, self.w, s)

    def set(self, height, weight, s):
        self.h = height
        self.w = weight
        self.s = s
        print("create complete!!\n")
        
    
    def Chest(self) :
        index = self.s
        
        if(self.s == 0) :

            for idx in range(len(chest)) :
                if idx % 2 == 0 :
                    workout = chest[idx]
                
                    result = workout
                    print(result, end=" : ")
                else :
                    kg = self.w * chest[idx][index]
                    
                    result = kg
                    reps = 8
                    print(str(result) + "kg reps : ", reps)
                    

          
            

    def Back(self) :
        return 
    
    def Leg(self) :
        return 

    def chest(self) :
        return 
 

flag = True
while(flag) :

    height = float(input("What's u are height : "))
    weight = float(input("What's u are weight : "))
    s = int(input("If u male put 0 else 1 :"))
    person = Person
    person.set(person, height, weight, s)

    commend = int(input('''workout list 
        1. chest
        2. back
        3. Leg

     what workout do u wnat? :'''))
    
    #person.print(person)
    if commend == 1 :
        person.Chest(person)

    roop_condition = input("계속하시겠습니까? (yes/no)")
    if roop_condition == "no" :
        flag = 0



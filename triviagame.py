# you will create a simple trivia game for two player
import random
class Question:

    def __init__(self,trivia_question,answer1,answer2,answer3,answer4,correct_answer):
        self.__trivia_question=trivia_question
        self.__answer1=answer1
        self.__answer2=answer2
        self.__answer3=answer3
        self.__answer4=answer4
        self.__correct_answer=correct_answer

    def get_question(self):
        return self.__trivia_question

    def get_answer1(self):
        return self.__answer1

    def get_answer2(self):
        return self.__answer2

    def get_answer3(self):
        return self.__answer3

    def get_answer4(self):
        return self.__answer4

    def get_correct_answer(self):
        return self.__correct_answer

    def __str__(self):
        return f"{self.get_question()}(1-4)?\n" \
               f"\t1. {self.get_answer1()}\n" \
               f"\t2. {self.get_answer2()}\n" \
               f"\t3. {self.get_answer3()}\n" \
               f"\t4. {self.get_answer4()}"

class Player():

    def __init__(self,name):
        self.__name=name
        self.__points=0

    def get_name(self):
        return self.__name

    def get_points(self):
        return self.__points

    def add_point(self):
        self.__points+=1

list_question=[]

def main():


    with open("C:/Users/Andre/Downloads/animals.txt",encoding="utf8") as file:
        question=""
        ans=""
        a=""
        b=""
        c=""
        d=""
        for line in file:
            if line[0]=="#":
                question=line[2:].rstrip()
            elif line[0]=="^":
                ans=line[2:].rstrip()
            elif line[0]=="A":
                a=line[2:].rstrip()
            elif line[0]=="B":
                b=line[2:].rstrip()
            elif line[0]=="C":
                c=line[2:].rstrip()
            elif line[0]=="D":
                d=line[2:].rstrip()
                list_question.append(Question(question, a, b, c, d, ans))
                question = ""
                ans = ""
                a = ""
                b = ""
                c = ""
                d = ""

    name1=input("Enter name of player 1: ")
    name2 = input("Enter name of player 2: ")

    player1=Player(name1)
    player2=Player(name2)

    def check_answer(ans,question):
        anss=""
        if ans=="1":
            anss=question.get_answer1()
        elif ans=="2":
            anss=question.get_answer2()
        elif ans=="3":
            anss=question.get_answer3()
        elif ans=="4":
            anss=question.get_answer4()
        if anss==question.get_correct_answer():
            print("correct!\n")
            return True
        else:
            print(f"Wrong! the correct answer is {question.get_correct_answer()}\n")
            return False

    for i in range(9):
        if i%2==0:
            print(f"Its {player1.get_name()}'s turn!")
            print(list_question[i])
            ans=input("Enter answer: ")
            result=check_answer(ans,list_question[i])
            if result == True:
                player1.add_point()

        else:
            print(f"Its {player2.get_name()}'s turn!")
            print(list_question[i])
            ans = input("Enter answer: ")
            result = check_answer(ans, list_question[i])
            if result == True:
                player2.add_point()

    print("\nResults")
    print("----------------")
    print(f"{player1.get_name()}: {player1.get_points()} points")
    print(f"{player2.get_name()}: {player2.get_points()} points")
    if player1.get_points()>player2.get_points():
        print(f"{player1.get_name()} is the winner!")
    elif player2.get_points()>player1.get_points():
        print(f"{player2.get_name()} is the winner!")
    else:
        print("Its a draw!")


if __name__=="__main__":
    main()
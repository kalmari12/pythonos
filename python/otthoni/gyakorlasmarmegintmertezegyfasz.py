import random

szam2 = random.randint(1,100)
igaze = True

def is_even(szam) -> bool:
    if szam % 2 == 0:
        return True
    else:
        return False
    
is_even(szam2)

def ossz(elso, masodik):
    osszeg = elso+masodik
    return osszeg

print(ossz(5,5))

def szavak(szoveg) -> list:
    index = 0
    for szo in szoveg:
        index += 1
    return index

print(szavak("positional argument but"))

'''ask_question(question, options, correct_index) -> bool
Prints the question + options, takes user input (1-4), returns True if correct.

run_quiz(questions, options_list, answers) -> int
Loops through all questions, uses ask_question, counts score, returns score.

show_result(score, total) -> None
Prints something like: You got 7/10 (70%)'''




def kerdes(kerdes, valaszok, rendes):
    print(kerdes)
    print(f"{valaszok[0]}\n"
          f"{valaszok[1]}\n"
          f"{valaszok[2]}")
    valasz = int(input("valasszon egyet: "))
    if valasz == rendes:
        print("on eltalalta")
    else:
        print("gatya")

vvalaszok = ["nem ","igen ","ez buta"]

kerdes("feljutunk e bronz 2-be",vvalaszok,2)    



    
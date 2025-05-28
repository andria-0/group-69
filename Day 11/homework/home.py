#1)გადაიმეროთ განვლილი მასალა 
#2)ახსენით კომენტარებით while loop და for loop განსხვავება 
#3)მომხმარებელს შემოატანინეთ რიცხვი და ეს რიცხვი თუ იყო 18 მეტი დაპრინტეთ "you are big adult" "if ით გააკეთეთ"
#4)გააკეთეთ 3 დავალება while loop ით 


#for loop თუ გინდა რამის დაპრინტვა უნდა მიუთითო რაოდენობა
#while loop შეგიძლია დაპრინტო რაოდენობის მითითების გარეში მაგრამ გამოვა უსასრულად მითითებული

i = int(input("enter your age:"))

if i>18:
     print("you are big adult")

i = int(input("enter your age:"))

while i>18:
    print("you are big adult")
    break

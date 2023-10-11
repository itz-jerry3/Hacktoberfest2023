marks_of_subjects = list(map(float,input("Enter 3 subject marks (separated by comma): ").split(",")))
lab_excercise,report,final_examination = marks_of_subjects
final_mark = ((lab_excercise*0.2)+(report*0.4)+(final_examination*0.4))
print(final_mark)
zero_count = 0 
ab_count = 0
final_count = 0
if(final_mark>=85 and final_mark<=100):
    print("HD")
elif(final_mark>=75):
    print("D")
elif(final_mark>=65):
    print("C")
elif(final_mark>=50):
    print("P")
elif(final_mark>=45):
    for i in marks_of_subjects:
        if i == 0:
            zero_count += 1
        elif i <50:
            final_count+=1
        elif zero_count==0 and final_count<=1:
            if marks_of_subjects[2]<50:
                print("SE")
            else:
                print("F")
else:
    if(marks_of_subjects.count(0)>2):
        print("AF")
    else:
        print("F")

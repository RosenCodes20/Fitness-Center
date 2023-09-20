number_visitors=int(input())
back=0
chest=0
legs=0
abs_training=0
protein_shake=0
protein_bar=0
work_out_percent=0
protein_percent=0
for training in range(number_visitors):
    what_to_do_today=input()
    if what_to_do_today=="Back":
        back+=1
    elif what_to_do_today=="Chest":
        chest+=1
    elif what_to_do_today=="Legs":
        legs+=1
    elif what_to_do_today=="Abs":
        abs_training+=1
    elif what_to_do_today=="Protein shake":
        protein_shake+=1
    else:
        protein_bar+=1
work_out_percent=(back+chest+legs+abs_training)/number_visitors*100
protein_percent=(protein_shake+protein_bar)/number_visitors*100
print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs_training} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{work_out_percent:.2f}% - work out")
print(f"{protein_percent:.2f}% - protein")

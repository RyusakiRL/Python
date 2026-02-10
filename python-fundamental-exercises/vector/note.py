note = []

for i in range(10):
    grade = int(input("Enter the note\n"))
    note.append(grade);

sumnote = sum(note)/len(note);
print(f"The average of class is: {sumnote:.2f}");

quantityoveravg = 0;
biggest_note = max(note)

print(f"The biggest note is:\n {biggest_note}")

for i, grade in enumerate(note):
    if grade>sumnote:
        quantityoveravg+=1;
    
    if grade == biggest_note:
        print(f"Position:{i}")

print(f"Students over of average:\n {quantityoveravg}")


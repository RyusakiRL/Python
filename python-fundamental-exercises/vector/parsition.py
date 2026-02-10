vectorios = [];
limit = 0;
limit2 = 0
position = 0;
parvect = []
positionvec = []
while limit<=9:
    number = int(input("Enter the number\n"))

    vectorios.append(number)
    limit+=1;

while limit2<=9:

    if vectorios[limit2]%2==0:
        positionvec.append(position)
        parvect.append(vectorios[limit2])

    position+=1
    limit2+=1;
print("----------------RESULTS----------------");
print("The position of pair numbers is:\n", positionvec)
print("The numbers pair ir order is:\n", parvect);
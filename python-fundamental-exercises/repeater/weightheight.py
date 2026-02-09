limit = 1;
avgh=0;
over90=0; 
minus50=0;


while limit<=7:
    weight = float(input("Write the weight"))
    height = float(input("Write the height"))

    avgh+=height
    
    
    if weight>90:
        over90+=1

    elif weight<50 and height<1.60:
        minus50+=1


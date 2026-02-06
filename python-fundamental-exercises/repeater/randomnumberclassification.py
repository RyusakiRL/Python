import random

limit = 1;
abovefive = 0;
divisiblebythree = 0;

while limit<=20:
    
    randomnumber = random.randint(0, 10)
    print(f"{randomnumber}", end=" ")
    
    limit = limit+1
    
    if randomnumber%3==0:
        divisiblebythree = divisiblebythree+1;
    
    if randomnumber>5:
        abovefive = abovefive+1;

print(f"Had {divisiblebythree} numbers divisible by three and {abovefive} above of five");
from visual import *
from random import *

scene = display(title= 'Magic 8 Ball', x= 0, y=0, width=800, height=800, center=(0,0,0),
                background=(0,1,1), color=color.gray)

ball = sphere(pos=(0,0,-5), radius=5, color=color.black, material=materials.marble)
circle = sphere(pos=(0,0,-2), radius=2.75, color=color.blue, material=materials.emissive)

textstart = text(text='Ask a Question', align='center', depth=-0.3, material=materials.silver,pos=(0,10))

reps = 0;
while (reps < 4):
    num =1
    while (num < 10):
        rate(30)
        ball.rotate(angle=radians(pi/2), axis=(1, 1, 0), origin=ball.pos)
        if( circle.pos.y >= 1.535):
            circle.pos.z = circle.pos.z - 0.5                 
        else:
            circle.pos.y = circle.pos.y + 0.375
            circle.pos.z = circle.pos.z - 0.25
        num = num +1


    nums =1
    while (nums < 10):
        rate(30)   
        ball.rotate(angle=radians(pi/2), axis=(1, 1, 0), origin=ball.pos)
        if( circle.pos.z < -2.75):
            circle.pos.z = circle.pos.z + 0.5
        elif(circle.pos.y != 0):
            circle.pos.z = circle.pos.z + 0.25
            circle.pos.y = circle.pos.y - 0.375
        nums = nums +1

    reps = reps + 1


question= raw_input("Ask Magic 8 Ball a question: (press enter to quit) ")
    
numss =0
while (numss < 10):
    rate(10)
    if (numss % 2 == 0):    
        ball.pos.x = ball.pos.x + 2
        circle.pos.x = circle.pos.x + 2
    else:
        ball.pos.x = ball.pos.x - 2
        circle.pos.x = circle.pos.x - 2
    numss = numss +1


randnum = randint(1,9)

if (randnum == 1 or randnum == 9 or randnum == 6):
    text1 = text(text='Yes', align='center', depth=1, color=color.red)
    print 'Yes'
    wait =0
    while(wait < 5):
        rate(1)
        wait = wait +1
    numsss =1
    while (numsss < 10):
        rate(15)
        ball.rotate(angle=radians(pi/2), axis=(1, 1, 0), origin=ball.pos)
        if( circle.pos.y >= 1.535):
            circle.pos.z = circle.pos.z - 0.5
            text1.pos.z = text1.pos.z - 0.5
        else:
            circle.pos.y = circle.pos.y + 0.375
            text1.pos.y = text1.pos.y + 0.375
            circle.pos.z = circle.pos.z - 0.25
            text1.pos.z = text1.pos.z - 0.25
            
        numsss = numsss +1

elif (randnum == 2 or randnum == 8 or randnum == 5):
    text2 = text(text='No', align='center', depth=1, color=color.red)
    print 'No'
    wait =0
    while(wait < 5):
        rate(1)
        wait = wait +1
    numsss =1
    while (numsss < 10):
        rate(15)
        ball.rotate(angle=radians(pi/2), axis=(1, 1, 0), origin=ball.pos)
        if( circle.pos.y >= 1.535):
            circle.pos.z = circle.pos.z - 0.5
            text2.pos.z = text2.pos.z - 0.5
        else:
            circle.pos.y = circle.pos.y + 0.375
            text2.pos.y = text2.pos.y + 0.375
            circle.pos.z = circle.pos.z - 0.25
            text2.pos.z = text2.pos.z - 0.25
        numsss = numsss +1

else:
    text3 = text(text='Maybe', align='center', depth=1, color=color.red)
    print 'Maybe'
    numsss =1
    wait =0
    while(wait < 5):
        rate(1)
        wait = wait +1
    while (numsss < 10):
        rate(15)
        ball.rotate(angle=radians(pi/2), axis=(1, 1, 0), origin=ball.pos)
        if( circle.pos.y >= 1.535):
            circle.pos.z = circle.pos.z - 0.5
            text3.pos.z = text3.pos.z - 0.5
        else:
            circle.pos.y = circle.pos.y + 0.375
            text3.pos.y = text3.pos.y + 0.375
            circle.pos.z = circle.pos.z - 0.25
            text3.pos.z = text3.pos.z - 0.25
        numsss = numsss +1


circle = sphere(pos=(0,0,-2), radius=2.75, color=color.white, material=materials.emissive)
textfinal = text(text='8', align='center', depth=1, color=color.black)
textfinal2 = text(text='Your fate has been sealed', align='left', depth=-0.3, material=materials.silver,pos=(-7,-10))

print "Your fate has been sealed" 



        

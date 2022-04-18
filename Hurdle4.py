def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
  
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for i in range(1,7):
    jump()
    


def turn_right():
    turn_left()
    turn_left()
    turn_left()
  
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

number_of_hurdles = 6

#while(number_of_hurdles > 0):
#    jump()
#    number_of_hurdles -=1
#    if(at_goal()):
#        number_of_hurdles = 0
        
#while at_goal() != True:
#    jump()

while not at_goal():
    jump()
        
    
#Hurdle 4
  def turn_right():
    turn_left()
    turn_left()
    turn_left()
  
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
def jump1():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

    
def jump2():
    turn_left()
    move()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

    #number_of_hurdles = 6

#while(number_of_hurdles > 0):
#    jump()
#    number_of_hurdles -=1
#    if(at_goal()):
#        number_of_hurdles = 0
        
#while at_goal() != True:
#    jump()

while not at_goal():
    if front_is_clear():
        move()
    if wall_in_front():
        jump2()
    
        
    

















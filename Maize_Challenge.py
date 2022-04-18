def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
      
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


while not at_goal():
 
    if front_is_clear() and right_is_clear():
        turn_right()
    if right_is_clear() and not wall_in_front() :
        move()     
    if right_is_clear() and wall_in_front() :
        turn_right()  
  
    if wall_in_front() and wall_on_right():
        turn_left()  
    if front_is_clear():
        move()
   
    #if right_is_clear():
       # turn_right()




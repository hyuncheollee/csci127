#Name: Hyuncheol Lee
#Email: hyuncheol.lee47@myhunter.cuny.edu
#Date: November 21, 2022
#This program will loop numbers

#Program that loops from 0 to 100 by 10
ADDI $s0, $zero, 0   #set s0 to 0
ADDI $s1, $zero, 10  #use to increment counter
ADDI $s2, $zero, 100
AGAIN: ADD $s0, $s0, $s1
BEQ $s0, $s2, DONE
J AGAIN
DONE:  #To break out of the loop
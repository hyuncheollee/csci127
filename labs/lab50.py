#Name: Hyuncheol Lee
#Email: hyuncheol.lee47@myhunter.cuny.edu
#Date: November 21, 2022
#This program will print I use MIPS!

ADDI $sp, $sp, -11
ADDI $t0, $zero, 73  # I
SB $t0, 0($sp)
ADDI $t0, $zero, 32  # (space)
SB $t0, 1($sp)
ADDI $t0, $zero, 117 # u
SB $t0, 2($sp)
ADDI $t0, $zero, 115 # s
SB $t0, 3($sp)
ADDI $t0, $zero, 101 # e
SB $t0, 4($sp)
ADDI $t0, $zero, 32  # (space)
SB $t0, 5($sp)
ADDI $t0, $zero, 77  # M
SB $t0, 6($sp)
ADDI $t0, $zero, 73  # I
SB $t0, 7($sp)
ADDI $t0, $zero, 80  # P
SB $t0, 8($sp)
ADDI $t0, $zero, 83  # S
SB $t0, 9($sp)
ADDI $t0, $zero, 33  # !
SB $t0, 10($sp)
ADDI $t0, $zero, 0 # (null)
SB $t0, 11($sp)
ADDI $v0, $zero, 4 # 4 is for print string
ADDI $a0, $sp, 0
syscall 			# print to the log
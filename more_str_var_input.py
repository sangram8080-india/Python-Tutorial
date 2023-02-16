#Mini collage Managements using Python 

name1,name2 = input("Enter The  Frist Name and Last Name : = ").split()  #Enter The Frist_Name and Last_Name 

name = str(name1)+str(name2)

print("\nEnter The Roll Num for\t"+name) #Enter The value of Roll Num 
roll_num = input()

#Name Roll and Marks
M,H,E = input("\nEnter The Marks\n1.Math\n2.Hindi\n3.English").split()
total = int(M)+int(H)+int(E)
print("Student Name:"+name+"\t\tRoll Num:"+roll_num)
print("\n****************Marks*****************")
print("\n1.Hindi  :\t"+H)
print("\n2.English:\t"+E)
print("\n3.Math   :\t"+M)
print("\n\t\tTotal Marks :"+str(total))





A = (int(input()), int(input()))
B = (int(input()), int(input()))
C = (int(input()), int(input()))

AB = (A[0]-B[0])**2+(A[1]-B[1])**2
AC = (A[0]-C[0])**2+(A[1]-C[1])**2
BC = (B[0]-C[0])**2+(B[1]-C[1])**2

if(AB == AC + BC or AC == BC + AB or BC == AC + AB):
    print("yes")
else:
    print("no")
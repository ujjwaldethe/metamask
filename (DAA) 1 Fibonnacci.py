def iterative(n):
    a=0
    b=1
    for i in range(n):    
        print(a,end=" ")
        c=a
        a=b
        b=c+b
def recursive(n):
    if n<=1:
        return n
    else:
        return recursive(n-1)+recursive(n-2)
def main():    
    while True:   
        choice = int(input("\n\nEnter Choice : \n 1.Iterative\n 2.Recurisive \n 3.Exit \n :"))
        if(choice==1):
            n = int(input("Enter Terms : "))
            print("Fibonnacci Series : ")
            iterative(n)
        elif(choice==2):
            n = int(input("Enter Terms : "))
            print("Fibonnacci Series : ")
            for i in range(n):
                print(recursive(i),end=" ")
        else:
            print("Existed...")
            break
main()

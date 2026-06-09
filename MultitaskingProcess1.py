import multiprocessing
import time
import os

def SumEven(No):
    print("PID of sum even ",os.getpid())
    print("PPID of sum Even:",os.getppid())#21
    
    Sum = 0 
    for i in range(2,No+1,2):
        Sum = Sum + i 
        
    print("Even Sum is :",Sum)
    
    
def SumOdd(No):
    print("PID of sum odd",os.getpid()) #101
    print("PPID of sum odd:",os.getppid()) #21
    Sum = 0 
    for i in range(1,No+1,2):
        Sum = Sum + i 
        
    print("Odd Sum is :",Sum)
         

      
 
def main():
    print("PID of sum even ",os.getpid()) 
    print("PPID of sum Even:",os.getppid()) 
    
    start_time = time.time()
    
    t1 = multiprocessing.process(targer = SumEven,args=(100000000,))
    t2 = multiprocessing.process(targer = SumOdd,args=(100000000,))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    end_time = time.time()
    
    
    print("time requared: ",end_time-start_time)
       
    
if __name__ == "__main__":
    main()
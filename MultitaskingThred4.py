import threading


def Display():
    print("inside Display Function:",threading.get_ident())
    for i in range(100):
        print("inside display")
        
    
     
def main():
    print("inside main",threading.get_ident())
    
    t = threading.Thread(target=Display)
    t.start()
    t.join()
    
    print("end of main")
    
   
      
    
if __name__ == "__main__":
    main()
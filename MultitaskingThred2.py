import threading


def Display():
    print("inside Display Function:",threading.get_ident())
    
     
def main():
    print("inside main",threading.get_ident())
    
    t = threading.Thread(target=Display)
    t.start()
    
    print("end of main")
    
   
      
    
if __name__ == "__main__":
    main()
#Simulated the four main CPU scheduling techniques in python. First Come First Serve, Shortest Job First, Shortest Remaining Time First, and finally Round Robin (with time quantum = 4).To finding the total waiting time as well as the total turnaround time for each process. To further attain  an average of both to figure out which is the best scheduling technique for the given process`s burst time.


# Round Robin
def fwt(processes, n, bt,  
                         wt, q):  
    rbt = [0] * n
 

    for i in range(n):  
        rbt[i] = bt[i]
    t = 0  
   
    while(1):
        done = True
 
          
        for i in range(n):
             
            if (rbt[i] > 0) :
                done = False 
                 
                if (rbt[i] > q) :
                 
                    t += q  
 
                    rbt[i] -= q  
                 
                else:
                 
                     
                    t = t + rbt[i]  
 
                     
                    wt[i] = t - bt[i]  
 
                      
                    rbt[i] = 0
          
        if (done == True):
            break
             
def ftat(processes, n, bt, wt, tat):
     
      
    for i in range(n):
        tat[i] = bt[i] + wt[i]  
 
def at(processes, n, bt, q):  
    wt = [0] * n
    tat = [0] * n  
 
    fwt(processes, n, bt,  
                         wt, q)  
 
      
    ftat(processes, n, bt,
                                wt, tat)  
 
     
    print("Round Robin Quantum 4")
    print("Processes    CPU Burst(ms)     Waiting",  
                     "Time    Turn-Around Time")
    twt = 0
    ttat = 0
    for i in range(n):
 
        twt = twt + wt[i]  
        ttat = ttat + tat[i]  
        print(" ", i + 1, "\t\t", bt[i],  
              "\t\t", wt[i], "\t\t", tat[i])
 
    print("\nAverage waiting time = %.2f"%(twt /n) )
    print("Average turn around time = %.2f "% (ttat / n))
     
  
if __name__ =="__main__":
     
    p = [1, 2, 3, 4, 5, 6]
    n = 6
 
    bt = [10, 2, 4, 1, 3, 20]  
    aa = [0, 1, 4, 5, 10, 21] 
    q = 4;  
    at(p, n, bt, q)
# Shortest Remaining Time First  
def fwt(p, n, wt):  
    rt = [0] * n
 
      
    for i in range(n):  
        rt[i] = p[i][1]
    complete = 0
    t = 0
    minm = 100
    short = 0
    check = False
 
      
    while (complete != n):
         
        
        for j in range(n):
            if ((p[j][2] <= t) and
                (rt[j] < minm) and rt[j] > 0):
                minm = rt[j]
                short = j
                check = True
        if (check == False):
            t += 1
            continue
             
         
        rt[short] -= 1
 
          
        minm = rt[short]  
        if (minm == 0):  
            minm = 100
            
 
         
        if (rt[short] == 0):  
 
              
            complete += 1
            check = False
 
              
            fint = t + 1
 
             
            wt[short] = (fint - proc[short][1] -    
                                proc[short][2])
 
            if (wt[short] < 0):
                wt[short] = 0
         
          
        t += 1
 
  
def ftat(p, n, wt, tat):  
     
     
    for i in range(n):
        tat[i] = p[i][1] + wt[i]  
 
 
def at(p, n):  
    wt = [0] * n
    tat = [0] * n  
 
      
    fwt(p, n, wt)  
 
      
    ftat(p, n, wt, tat)  
 
    
    print("Shortest Remaining Time First")
    print("Processes    CPU Burst(ms)    Waiting",  
                    "Time     Turn-Around Time")
    twt = 0
    ttat = 0
    for i in range(n):
 
        twt = twt + wt[i]  
        ttat = ttat + tat[i]  
        print(" ", p[i][0], "\t\t",  
                   p[i][1], "\t\t",  
                   wt[i], "\t\t", tat[i])
 
    print("\nAverage waiting time = %.2f "%(twt /n) )
    print("Average turn around time = %.2f"%(ttat / n))  
     
  
if __name__ =="__main__":
     
      
    proc = [[1, 10, 0], [2, 2, 1],
            [3, 4, 4], [4, 1, 5],
            [5, 3, 10], [6, 20, 21]]
    aa = [0, 1, 4, 5, 10, 21]
    n = 6
    at(proc, n)

#  First Come First Serve
def fwt(processes, n,
                    bt, wt):
 
    wt[0] = 0
 
    for i in range(1, n ):
        wt[i] = bt[i - 1] + wt[i - 1]  
 
def ftt(processes, n,  
                       bt, wt, tat):
 
    for i in range(n):
        tat[i] = bt[i] + wt[i]
 
def at( processes, n, bt):
 
    wt = [0] * n
    tat = [0] * n  
    twt = 0
    ttat = 0
 
    fwt(processes, n, bt, wt)
 
    ftt(processes, n,  
                       bt, wt, tat)
 
    print ("First Come First Serve")
    print( "Processes CPU Burst (ms)  " +
                  " Waiting time " +
                " Turn around time")
 
    for i in range(n):
     
        twt = twt + wt[i]
        ttat = ttat + tat[i]
        print(" " + str(i + 1) + "\t\t" +
                    str(bt[i]) + "\t " +
                    str(wt[i]) + "\t\t " +
                    str(tat[i]))  
 
    print("\nAverage waiting time = %.2f "%(twt /n) )
    print("Average turn around time = %.2f"%(ttat / n))
 
if __name__ =="__main__":
     
    processes = [ 1, 2, 3, 4, 5, 6]
    n = len(processes)
    aa = [0, 1, 4, 5, 10, 21] 
    bt = [10, 2, 4, 1, 3, 20]
 
    at(processes, n, bt)
#  Shortest Job First
def fwt(p, n, wt):  
    rt = [0] * n
 
      
    for i in range(n):  
        rt[i] = p[i][1]
    complete = 0
    t = 0
    minm = 100
    short = 0
    check = False
 
      
    while (complete != n):
         
        
        for j in range(n):
            if ((p[j][2] <= t) and
                (rt[j] < minm) and rt[j] > 0):
                minm = rt[j]
                short = j
                check = True
        if (check == False):
            t += 1
            continue
             
         
        rt[short] -= 1
 
          
        minm = rt[short]  
        if (minm == 0):  
            minm = 100
            
 
         
        if (rt[short] == 0):  
 
              
            complete += 1
            check = False
 
              
            fint = t + 1
 
             
            wt[short] = (fint - proc[short][1] -    
                                proc[short][2])
 
            if (wt[short] < 0):
                wt[short] = 0
         
          
        t += 1
 
  
def ftat(p, n, wt, tat):  
     
     
    for i in range(n):
        tat[i] = p[i][1] + wt[i]  
 
 
def at(p, n):  
    wt = [0] * n
    tat = [0] * n  
 
      
    fwt(p, n, wt)  
 
      
    ftat(p, n, wt, tat)  
 
    
    print("Shortest Job First")
    print("Processes    CPU Burst(ms)    Waiting",  
                    "Time     Turn-Around Time")
    twt = 0
    ttat = 0
    for i in range(n):
 
        twt = twt + wt[i]  
        ttat = ttat + tat[i]  
        print(" ", p[i][0], "\t\t",  
                   p[i][1], "\t\t",  
                   wt[i], "\t\t", tat[i])
 
    print("\nAverage waiting time = %.2f "%(twt /n) )
    print("Average turn around time = %.2f"%(ttat / n))  
     
  
if __name__ =="__main__":
     
      
    proc = [[1, 10, 1], [2, 2, 2],
            [3, 4, 6], [4, 1, 5],
            [5, 3, 11], [6, 20, 22]]
    aa = [0, 1, 4, 5, 10, 21]         
    n = 6
    at(proc, n)

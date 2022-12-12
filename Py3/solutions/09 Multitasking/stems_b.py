#!/usr/local/bin/python3
import mytimer
from multiprocessing import Process, cpu_count
# (b)
#############################################################
def stem_search(stems, start, end):
    """ Note that end is last position + 1 """
    for stem_size in range(start, end): 
        best_stem = ""
        best_count = 0

        for (stem,count) in stems.items():
            if stem_size == len(stem) and count > best_count:
                best_stem  = stem
                best_count = count

        if best_stem:
            print ("Most popular stem of size",stem_size,"is:",
                    best_stem,"(occurs",best_count,"times)")

#############################################################
if __name__ == '__main__':   

    mytimer.start_timer()

    stems = {}

    for row in open ("words"):
        for count in range(1,len(row)):
            stem = row[0:count]
            if stem in stems:
                stems[stem] += 1
            else:
                stems[stem] = 1
            #print ("stem:",stem,"value:<",stems[stem],">")
       
    mytimer.end_timer('Load')        

    # Process the stems

    processes=[]
    mytimer.start_timer()
    n = 30
    
    cpus = cpu_count()
    print("Number of cpus:", cpus)
    stems_per_cpu = int(n/cpus) + 1
    
    for cpu in range(0, cpus):
        spos = (stems_per_cpu * cpu) + 1
        epos = spos + stems_per_cpu
        if epos > n: epos = n
        
        proc = Process(target=stem_search, args=(stems, spos, epos))
        print("Processing %d to %d" % (spos, epos))
        proc.start()
        processes.append(proc)
        
    for proc in processes:
        proc.join()
                 
    mytimer.end_timer('Process')  

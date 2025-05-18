









############ multi processing ###############

import multiprocessing

def worker(task_id):
    print(f"Process {task_id} working")
    # CPU-intensive work
    result = sum(i*i for i in range(10_000_000))
    print(f"Process {task_id} finished")
    return result

if __name__=="__main__":
    processes = []
    
    for i in range(1, 5):
        
        p = multiprocessing.Process(target=worker, args=(i,))
        p.start()
        processes.append(p)
    
    for p in processes:
        p.join()
        
        
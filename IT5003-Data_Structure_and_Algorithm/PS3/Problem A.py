from bisect import bisect_left  

journey = input()

cur_len = 0     
p,g,o = 0,0,0
GAME_OVER = False
lp = []
lg = []
lo = []

for i in journey:
    if i == ".":
        continue
    elif i == "p":
        lp.append(cur_len)   
        cur_len += 1         
    elif i == "g":
        lg.append(cur_len)
        cur_len += 1
    elif i == "o":
        lo.append(cur_len)
        cur_len += 1
    elif i == "P":
        if len(lp) == 0:
            GAME_OVER = True
            break
        else:
        
            limit = lp.pop() 
            cur_len = limit  
            del lg[bisect_left(lg, limit):]
            del lo[bisect_left(lo, limit):]
            
    elif i == "G":
        if len(lg) == 0:
            GAME_OVER = True
            break
        else:
            limit = lg.pop()
            cur_len = limit
            
            del lp[bisect_left(lp, limit):]
            del lo[bisect_left(lo, limit):]
            
    elif i == "O":
        if len(lo) == 0:
            GAME_OVER = True
            break
        else:
            limit = lo.pop()
            cur_len = limit
            
            del lp[bisect_left(lp, limit):]
            del lg[bisect_left(lg, limit):]
                
if GAME_OVER == False:
    print(len(lp))
    print(len(lg))
    print(len(lo))
else:
    print("Neibb")


            
              

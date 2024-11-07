
def solve():
    
    left_m = 3
    left_c = 3
    right_m = 0
    right_c = 0

   
    while left_m > 0 or left_c > 0:
       
        if left_c >= 2:
            left_c -= 2
            right_c += 2
            print("Move 2 Cannibals from left to right.")
        
       
        elif left_m >= 2:
            left_m -= 2
            right_m += 2
            print("Move 2 Missionaries from left to right.")
        
        
        elif left_m >= 1 and left_c >= 1:
            left_m -= 1
            left_c -= 1
            right_m += 1
            right_c += 1
            print("Move 1 Missionary and 1 Cannibal from left to right.")
        
       
        print(f"Left: {left_m}M, {left_c}C  |  Right: {right_m}M, {right_c}C")
    
    print("Missionaries and Cannibals have crossed safely.")

solve()

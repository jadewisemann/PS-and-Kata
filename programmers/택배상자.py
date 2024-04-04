def solution(orders):
    main = 1  
    sub = []
    counter = 0
    
    for order in orders:
        while main <= order:
            sub.append(main)
            main += 1
            
        if sub and sub.pop() == order:
            counter += 1
        else:
            break 
        
    return counter

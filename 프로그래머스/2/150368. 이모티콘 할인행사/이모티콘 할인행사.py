def solution(users, emoticons):
    
    ans = [0, 0]
    
    l = len(emoticons)
    sale = [10 for _ in range(l)]
    emo = [0 for _ in range(l)]
    for i in range(l):
        emo[i] = int(emoticons[i] - emoticons[i] * sale[i] / 100)
    
    loop_flag = True
    while loop_flag:
        user_max, total_price = 0, 0
        for u in users:
            us, up = u
            user_price = 0
            for i in range(l):
                if sale[i] >= us:
                    user_price += emo[i]
            if user_price >= up:
                user_max += 1
            else:
                total_price += user_price
                
        if ans[0] < user_max:
            ans[0], ans[1] = user_max, total_price
            print(sale, ans)
        elif ans[0] == user_max and ans[1] < total_price:
            ans[1] = total_price
            print(sale, ans)
        
        # print(sale)
        for i in range(l):
            sale[i] += 10
            if sale[i] == 50:
                if i == l - 1:
                    loop_flag = False
                    break
                sale[i] = 10
                emo[i] = int(emoticons[i] - emoticons[i] * sale[i] / 100)
            else:
                emo[i] = int(emoticons[i] - emoticons[i] * sale[i] / 100)
                break
    
    return ans
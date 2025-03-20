def solution(today, terms, privacies):
    
    def calcDay(year, month, day):
        ret = (year - 2000) * 12
        ret = (ret + month - 1) * 28
        ret += day
        return ret
        
    tyear, tmonth, tday = today.split(".")
    td = calcDay(int(tyear), int(tmonth), int(tday))
    
    rule = {}
    for e in terms:
        r, d = e.split()
        rule[r] = int(d) * 28
    
    ans = []
    for i, e in enumerate(privacies):
        ts, tr = e.split()
        tyear, tmonth, tday = map(int, ts.split("."))
        bd = calcDay(tyear, tmonth, tday)
        bd += rule[tr]
        if bd <= td:
            ans.append(i + 1)
    
    ans.sort()
    
    return ans
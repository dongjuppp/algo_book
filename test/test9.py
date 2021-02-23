from datetime import datetime, timedelta
def str_to_sec(t):
    t = map(int, t.split(":"))
    result = 0
    for time, sec in zip(t, [3600, 60, 1]):
        result += time * sec
    return result

def sec_to_str(sec):
    s = sec % 60
    sec //= 60
    m = sec % 60
    sec //= 60
    h = sec
    return '{:02d}:{:02d}:{:02d}'.format(h,m,s)

def solution(play_time, adv_time, logs):
    answer = ''
    play=str_to_sec(play_time)
    adv=str_to_sec(adv_time)

    play_logs=[0 for i in range(360001)]

    for i in range(len(logs)):
        s,e=logs[i].split('-')

        play_logs[str_to_sec(s)]+=1
        play_logs[str_to_sec(e)]-=1
    
    for i in range(1,play+1):
        play_logs[i]+=play_logs[i-1]
    
    for i in range(1,play+1):
        play_logs[i]+=play_logs[i-1]

    mt=0
    mp=play_logs[adv]
    
    for s in range(1,play):
        end=s+adv if s+adv<play else play
        sp=play_logs[end]-play_logs[s]
        if mp<sp:
            mp=sp
            mt=s+1

    return sec_to_str(mt)


print(solution("02:03:55","00:14:15",["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))

print(sec_to_str(3752))
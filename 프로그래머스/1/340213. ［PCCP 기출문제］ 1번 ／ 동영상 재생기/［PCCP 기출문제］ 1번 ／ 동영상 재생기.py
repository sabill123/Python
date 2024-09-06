from datetime import timedelta, datetime

def solution(video_len, pos, op_start, op_end, commands):
    video_len = datetime.strptime(video_len, "%M:%S")
    pos = datetime.strptime(pos, "%M:%S")
    op_start = datetime.strptime(op_start, "%M:%S")
    op_end = datetime.strptime(op_end, "%M:%S")
    delta = timedelta(seconds = 10)
    init = datetime.strptime("00:00", "%M:%S")
    
    
    if op_start <= pos and pos <= op_end:
        pos = op_end
    
    for i in range(len(commands)):
        if (commands[i] == "next"):
            pos += delta
            if pos > video_len:
                pos = video_len 
        if commands[i] == "prev":
            pos -= delta
            if pos < init:
                pos = init
        if op_start <= pos and pos <= op_end:
            pos = op_end
        
        
    return pos.strftime("%M:%S")

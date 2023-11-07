import time


global cnt
cnt = 0


def t_yield():
    global cnt
    time.sleep(1)
    cnt += 1

    return str(cnt) + "tt"

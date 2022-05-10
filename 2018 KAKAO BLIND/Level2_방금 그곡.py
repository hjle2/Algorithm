def getlength(start_t, end_t):
    HH, MM = map(int, start_t.split(':'))
    hh, mm = map(int, end_t.split(':'))
    return hh*60 + mm - (HH * 60 + MM)


def getmusic(time, melody):
    len_melody = len(melody)
    if len_melody > time:
        return melody[:time]
    elif len_melody == time:
        return melody
    else:
        ans = melody * (time // len_melody)
        time -= len(ans)
        ans += melody[:time]
        return ans
    # if len(melody) >= time:
    #     return melody*2
    # else:
    #     return melody * ((time - len(melody)) // len(melody)) + melody[:time-len(melody)]
    #
    # ans = time // len(melody)
    # return melody * (1 + ans) * 2



def getmelody(music):
    music = list(music)
    sharp = [i for i in range(len(music)) if music[i] == '#']
    while sharp:
        i = sharp.pop()
        music[i-1] += '#'
        del music[i]
    return music

def iscorrespond(m, music):
    index = [i for i in range(len(music)) if m[0]==music[i]]
    for i in index:
        if i + len(m) <= len(music):
            if m == music[i:i+len(m)]:
                return True
        else:
            return


def solution(m, musicinfos):
    ans = []
    m = getmelody(m)
    for i, music in enumerate(musicinfos):
        start_t, end_t, title, music = music.split(',')
        time = getlength(start_t, end_t)
        music = getmelody(music)
        melody = getmusic(time, music)

        if iscorrespond(m, melody):
            ans.append((title, time))

    if ans:
        ans.sort(key=lambda x:-x[1])
        return ans[0][0]
    return '(None)'
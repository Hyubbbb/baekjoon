def solution(wallpaper):
    nrow = len(wallpaper)
    ncol = len(wallpaper[0])
    
    rows = []
    cols = []
    
    for r in range(nrow):
        if '#' in wallpaper[r]:
            rows.append(r)
        if wallpaper[r].find('#') >= 0:
            cols.append(wallpaper[r].find('#'))
        if wallpaper[r].rfind('#') >= 0:
            cols.append(wallpaper[r].rfind('#'))

    answer = [min(rows), min(cols), max(rows)+1, max(cols)+1]
    return answer
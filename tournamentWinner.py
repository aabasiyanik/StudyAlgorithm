def tournamentWinner(competitions, results):
    win = []

    for i in range(len(competitions)):
        if results[i] == 1:
            win.append(competitions[i][0])
        elif results[i] == 0:
            win.append(competitions[i][1])
    counts = {}
    count = 0
    winner = None

    for i in win:
        if i not in counts:
            counts[i] = 1
        else:
            counts[i] += 1
        if counts[i] > count:
            winner = i
            count = counts[i]
    return winner
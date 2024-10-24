# https://coderun.yandex.ru/seasons/2024-summer/tracks/backend/problem/tableau?currentPage=1&pageSize=50&search=

INPUT_F = 'input.txt'

def main():
    f = open(INPUT_F, 'r')
    n = int(f.readline())
    names_d = dict()
    for i in range(n):
        names_d[f.readline().strip()] = 0
    m = int(f.readline())
    score = [0, 0]
    for i in range(m):
        cur_score, player = f.readline().strip().split()
        cur_score = [int(sc) for sc in cur_score.split(':')]
        points = [cur_score[0]-score[0], cur_score[1]-score[1]]
        names_d[player] += sum(points)
        score = cur_score
        #print(score, cur_score, player, sum(points))
    max_points = 0
    best_players = []
    for player in names_d:
        if names_d[player] >= max_points:
            if names_d[player] > max_points:
                max_points = names_d[player]
                best_players = [player]
            else:
                best_players.append(player)

    return  sorted(best_players)[-1], max_points



if __name__ == '__main__':
    res = main()
    [print(s, end=' ') for s in res]
    print()

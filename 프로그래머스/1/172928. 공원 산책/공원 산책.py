def solution(park, routes):
    start_x, start_y = 0, 0
    for i, row in enumerate(park):
        if "S" in row:
            start_x, start_y = i, row.index('S')  # 's'를 대문자 'S'로 수정
            break  # 콜론 ':' 제거

    move = {'E': (0, 1), 'W': (0, -1), 'S': (1, 0), 'N': (-1, 0)}  # S와 N 방향 수정
    now_x, now_y = start_x, start_y

    for route in routes:
        direction, number = route.split()
        dx, dy = move[direction]
        number = int(number)

        temp_x, temp_y = now_x, now_y
        can_move = True

        for _ in range(number):
            temp_x += dx
            temp_y += dy
            # 경계 조건 수정 및 'False' 오타 수정
            if not (0 <= temp_x < len(park) and 0 <= temp_y < len(park[0])) or park[temp_x][temp_y] == 'X':
                can_move = False  # 'Flase' 오타 수정
                break  # 콜론 ':' 제거

        if can_move:
            now_x, now_y = temp_x, temp_y

    return [now_x, now_y]  # answer를 [now_x, now_y]로 수정

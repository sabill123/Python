def solution(players, callings):
    player_indices = {player: i for i, player in enumerate(players)}
    for name in callings:
        index = player_indices[name]
        if index > 0:
            prev_player = players[index - 1]
            
            players[index], players[index - 1] = players[index - 1], players[index]
            player_indices[name] -= 1
            player_indices[prev_player] += 1

    return players
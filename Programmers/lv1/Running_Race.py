# def solution(players, callings):
#     result = []
#     for i in range(len(callings)):
#         for j in range(len(players)):
#             if callings[i] == players[j]:
#                 players[j], players[j-1] = players[j-1], players[j]
#     return players

def solution(players, callings):
    players_map = {each:index for index, each in enumerate(players)}
    # print(players_map)
    for player in callings:
        print("1. player = {0}".format(player))
        index = players_map[player]
        print("2. index = {0}".format(index))
        players_map[player] -= 1
        print("3. players_map[{0}] = {1}".format(player, players_map[player]))
        players_map[players[index - 1]] += 1
        print("4. players_map[players[{0} - 1] = {1}".format(index, players_map[players[index-1]]))
        players[index - 1], players[index] = players[index], players[index - 1]
    return players

players = ['mumu', 'soe', 'poe', 'kai', 'mine']
callings = ['kai', 'kai', 'mine', 'mine']
print(solution(players, callings))
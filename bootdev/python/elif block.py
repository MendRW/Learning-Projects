def combat_evaluation(player_power, enemy_defense):
    advantage, disadvantage, evenly_matched = False, False, False

    if player_power > enemy_defense :
        advantage = True
        disadvantage = False
        evenly_matched = False
    elif player_power == enemy_defense :
        advantage = False
        disadvantage = False
        evenly_matched = True
    else:
        advantage = False
        disadvantage = True
        evenly_matched = False
        

    return advantage, disadvantage, evenly_matched

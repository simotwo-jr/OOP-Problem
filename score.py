def calculate_score(participant):
    score = participant['chickenwings'] * 5 + participant['hamburgers'] * 3 + participant['hotdogs'] * 2
    return score

def create_scoreboard(participants):
    scoreboard = [{'name': participant['name'], 'score': calculate_score(participant)} for participant in participants]
    scoreboard.sort(key=lambda x: (-x['score'], x['name']))
    
    return scoreboard





def calculate_score(participant):
    score = participant['chickenwings'] * 5 + participant['hamburgers'] * 3 + participant['hotdogs'] * 2
    return score

def create_scoreboard(participants):
    scoreboard = [{'name': participant['name'], 'score': calculate_score(participant)} for participant in participants]
    scoreboard.sort(key=lambda x: (-x['score'], x['name']))
    
    return scoreboard

participants = [
    {'name': "Habanero Hillary", 'chickenwings': 5, 'hamburgers': 17, 'hotdogs': 11},
    {'name': "Big Bob", 'chickenwings': 20, 'hamburgers': 4, 'hotdogs': 11}
]

scoreboard = create_scoreboard(participants)
print(scoreboard)







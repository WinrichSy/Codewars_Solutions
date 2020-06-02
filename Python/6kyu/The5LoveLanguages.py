#The 5 Love Languages
#https://www.codewars.com/kata/5aa7a581fd8c06b552000177

import statistics

def love_language(partner, weeks):
    responses = []
    for i in range((weeks+1)):
        for j in LOVE_LANGUAGES:
            if partner.response(j)== 'positive':
                responses.append(j)
    
    return(statistics.mode(responses))

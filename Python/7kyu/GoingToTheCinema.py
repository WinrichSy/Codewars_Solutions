#Going to the Cinema
#https://www.codewars.com/kata/562f91ff6a8b77dfe900006e

import math

def movie(card, ticket, perc):
        curr_card = card+(ticket*perc)
        total_ticket_price = ticket
        count = 1
        while (math.ceil(curr_card) >= total_ticket_price):
            curr_card += ticket*(perc**(count+1))
            total_ticket_price += ticket
            count += 1

        return count

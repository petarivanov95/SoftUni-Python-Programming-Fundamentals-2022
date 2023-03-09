# work

# tickets = [ticket.strip() for ticket in input().split(', ')]


# symbols = ['@', '#', '$', '^']
# valid_length = 20

# def winning_ticket(ticket):
#     ticket_list = list(ticket)
    
# def jackpot(ticket):
#     pass

# for ticket in tickets:
#     if len(ticket) == valid_length:
#         if winning_ticket(ticket):
#             if jackpot(ticket):
#                 print(f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!')
#             else:
#                 print(f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}')
#         else:
#             print(f"ticket "{ticket}" - no match")

#     else:
#         print("invalid ticket")    

def is_winning_ticket(ticket):
    if len(ticket) != 20:
        return "invalid ticket"
    winning_symbols = ["@", "#", "$", "^"]
    left_part = ticket[:10]
    right_part = ticket[10:]
    for match_symbol in winning_symbols:
        for uninterrupted_match_length in range(10, 5, -1):
            winning_symbol_repetitions = match_symbol * uninterrupted_match_length
            if winning_symbol_repetitions in left_part and winning_symbol_repetitions in right_part:
                if uninterrupted_match_length == 10:
                    return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!'
                else:
                    return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}'
    else:
        return f'ticket "{ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(", ")]
for ticket in tickets:
    print(is_winning_ticket(ticket))

# test inputs:

# Cash$$$$$$Ca$$$$$$sh

# $$$$$$$$$$$$$$$$$$$$, aabb  , th@@@@@@eemo@@@@@@ey

# validticketnomatch:(, Cas$$$$$$$Ca$$$$$$s$
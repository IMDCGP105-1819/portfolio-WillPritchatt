def hotel_cost(nights):
    cost = nights * 70
    return cost


def plane_ticket_cost(city, class_multiplier):
    if city == "New York":
        cost = 2000 * class_multiplier
    elif city == "Auckalnd":
        cost = 790 * class_multiplier
    elif city == "Venice":
        cost = 154 * class_multiplier
    elif city == "Glasgow":
        cost = 65 * class_multiplier
    return cost

def rental_car(days):
    cost = days * 30
    if days > 3:
        cost -= 30
    elif days > 7:
        cost -= 50
    return cost


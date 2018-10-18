def hotel_cost(nights):
    cost = nights * 70
    return cost


def plane_ticket_cost(city, class_multiplier):
    if city == "New York":
        cost = 2000 * class_multiplier
    elif city == "Auckland":
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


def total_cost(city, days):
    cost = 0

    cost += hotel_cost(days)

    print(""""Travel Class
    1. Economy
    2. Premium Economy
    3. Business
    4. First Class
    """)
    travel_class = int(input("Please enter the travel class (Identify using the number): "))
    class_multiplier = 1 + (travel_class - 1) * 0.3

    cost += plane_ticket_cost(city, class_multiplier)
    cost += rental_car(days)

    print("The final cost is £{}". format(cost))


print("""Cites to travel to
1. New York
2. Auckland
3. Venice
4. Glasgow
""")
city = input("Please enter the name of the City you are travelling to (Identify using the name): ")
days = int(input("Enter the number of days you are staying: "))

total_cost(city, days)

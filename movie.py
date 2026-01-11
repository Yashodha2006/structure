def calculate_ticket_price(ticket_type, count):
    """
    Calculate total ticket price
    based on ticket type and number of tickets.
    """
    count = int(count)

    if ticket_type == "Normal":
        return 150 * count
    elif ticket_type == "Premium":
        return 250 * count
    elif ticket_type == "VIP":
        return 400 * count
    else:
        # default ticket price
        return 150 * count


def main():
    # Taking input from user
    name = input("Enter customer name: ")
    ticket_type = input("Enter ticket type (Normal / Premium / VIP): ")
    tickets = input("Enter number of tickets: ")

    total_price = calculate_ticket_price(ticket_type, tickets)

    print("\n=== Movie Ticket Booking ===")
    print("Name =", name)
    print("Ticket Type =", ticket_type)
    print("Total Bill =", total_price)


if __name__ == "__main__":
    main()

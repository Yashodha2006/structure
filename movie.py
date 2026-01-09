import sys

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
    # Safe command-line arguments
    name = sys.argv[1] if len(sys.argv) > 1 else "Customer"
    ticket_type = sys.argv[2] if len(sys.argv) > 2 else "Normal"
    tickets = sys.argv[3] if len(sys.argv) > 3 else "1"

    total_price = calculate_ticket_price(ticket_type, tickets)

    print("=== Movie Ticket Booking ===")
    print("name =", name)
    print("ticket type =", ticket_type)
    print("total bill =", total_price)

if __name__ == "__main__":
    main()

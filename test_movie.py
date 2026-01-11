import unittest
from ticket_booking import calculate_ticket_price
# ticket_booking.py should be the filename of your main program

class TestTicketPrice(unittest.TestCase):

    def test_normal_ticket(self):
        self.assertEqual(calculate_ticket_price("Normal", 2), 300)

    def test_premium_ticket(self):
        self.assertEqual(calculate_ticket_price("Premium", 3), 750)

    def test_vip_ticket(self):
        self.assertEqual(calculate_ticket_price("VIP", 1), 400)

    def test_default_ticket(self):
        # invalid ticket type should use default price
        self.assertEqual(calculate_ticket_price("Gold", 2), 300)


if __name__ == "__main__":
    unittest.main()

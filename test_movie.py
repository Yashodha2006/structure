from movie_ticket_app import calculate_ticket_price

def test_normal_ticket():
    assert calculate_ticket_price("Normal", 2) == 300

def test_premium_ticket():
    assert calculate_ticket_price("Premium", 3) == 750

def test_vip_ticket():
    assert calculate_ticket_price("VIP", 1) == 400

from shop import Shop

def create_shop():
    address = "piazza Calamatta"
    open_at = 9
    close_at = 19
    min_price_euro = 10
    max_price_euro = 30
    walk_in_start_time = 17
    walk_in_length_time = 2
    return Shop(address,open_at,close_at,min_price_euro,max_price_euro,walk_in_start_time,walk_in_length_time)

def test_shop_address():
    shop = create_shop()
    assert shop.address == "piazza Calamatta"

def test_shop_opening():
    shop = create_shop()
    assert shop.open_hour == 9

def test_shop_closing():
    shop = create_shop()
    assert shop.close_hour == 19

def test_shop_min_price():
    shop = create_shop()
    assert shop.min_price == 10

def test_shop_max_price():
    shop = create_shop()
    assert shop.max_price == 30

def test_shop_avg_price():
    shop = create_shop()
    assert shop.avg_price == 20

def test_walk_in_starting():
    shop = create_shop()
    assert shop.walk_in_start_hour == 17

def test_walk_in_closing():
    shop = create_shop()
    assert shop.walk_in_stop_hour == 19

def test_is_now_open():
    shop = create_shop()
    assert shop.is_open(15) == True

def test_is_now_open_1():
    shop = create_shop()
    assert shop.is_open(8) == False

def test_is_now_open_2():
    shop = create_shop()
    assert shop.is_open(20) == False
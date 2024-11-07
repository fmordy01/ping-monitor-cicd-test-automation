from ping_service import ping_host

def test_ping_host():
    assert ping_host("8.8.8.8") == True #expected output: up
    assert ping_host("1.1.1.1") == True #expected output: up
    assert ping_host("192.0.2.1") == False #expected output: down
    
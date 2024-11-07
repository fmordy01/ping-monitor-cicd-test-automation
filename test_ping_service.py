from ping_service import ping_host

def test_ping_host_up_one():
    assert ping_host("https://www.google.com") == True #expected output: up

def test_ping_host_up_two():
    assert ping_host("https://www.cloudflare.com") == True #expected output: up

def test_ping_host_down():
    assert ping_host("https://doesntexist.something.down.test.com") == False #expected output: down

from src.app import soma, multiplica, status_service

def test_soma_inteiros():
    assert soma(2, 3) == 5

def test_multiplica_inteiros():
    assert multiplica(4, 5) == 20

def test_status_service():
    s = status_service()
    assert s["status"] == "ok"
    assert "service" in s

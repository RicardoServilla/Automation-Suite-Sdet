import requests

def test_example_dot_com():
    r = requests.get('https://www.example.com', timeout=10)
    assert r.status_code == 200
    assert 'Example Domain' in r.text

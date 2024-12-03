from package2.module_b import hello, sixteen

def test_hello_output(capsys):
    hello()
    captured = capsys.readouterr()
    assert "Hello from package2.module_b.hello" in captured.out
    
def test_sixteen_output():
    assert sixteen() == 16
import main

def test_to_upper():
    assert main.to_upper("hello") == "HELLO"

def test_say_hello(capsys):
    main.say_hello("Tannu")
    captured = capsys.readouterr()
    assert captured.out == "Hello, Tannu\n"
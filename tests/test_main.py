import assets.main

def test_encoder():
    val = assets.main.encoder("hello")
    assert val == ".... . .-.. .-.. ---"
    val2 = assets.main.encoder("this-is-a-test-message")
    assert val2 == "- .... .. ... -....- .. ... -....- .- -....- - . ... - -....- -- . ... ... .- --. ."

def test_decoder():
    val = assets.main.decoder("- .... .. ... -....- .. ... -....- .- -....- - . ... - -....- -- . ... ... .- --. .")
    assert val == "THIS-IS-A-TEST-MESSAGE"
    val2 = assets.main.decoder(".- -. --- - .... . .-. -....- - . ... - -....- -- ... --.")
    assert val2 == "ANOTHER-TEST-MSG"

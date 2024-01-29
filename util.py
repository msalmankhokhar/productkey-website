# test_text = "SALMAN,IMRAN,USMAN,"
test_text = ""

def generate_keysList(text):
    if text == "":
        return []
    else:
        return text[:-1].split(",")

print(generate_keysList(test_text))

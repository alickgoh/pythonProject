def smiley(msg):
    words = msg.split(" ")
    emojis = {
        ":)": "😊",
        ":(": "😌"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


msg = input(">")
print(smiley(msg))

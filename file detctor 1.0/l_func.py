import json
def locate(in_file):
    filePath = ""
    for l in in_file:
        if l == "\\":
            filePath += "/"
        else:
            filePath += l
    with open(filePath, "rb") as f:
        file = f.read()

    with open("file_sigs.json", "r") as j:
        content = json.load(j)

    matches = []
    for i in range(1, 9):
        byte = file[:i].hex()
        magicNum = str(" ".join(byte[i:i+2] for i in range(0, len(byte), 2))).upper()
        for sig in content["filesigs"]:
            if sig["Header (hex)"] == magicNum:
                matches.append({"sig" : sig["Header (hex)"], "exten" : sig["File extension"], "des" : sig["File description"]})
    return matches

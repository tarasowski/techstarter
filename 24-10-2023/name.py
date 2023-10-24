name = input("Gib deinen Namen ein: ")

with open("name.txt", "w") as datei:
    datei.write(name + "das kommt von hier")
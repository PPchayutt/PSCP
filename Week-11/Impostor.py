"""Impostor"""
import json
def main():
    """main"""
    person, dead, alive = {}, {}, {}
    impos = 0
    while True:
        tmp = input()
        if tmp.upper() == "END":
            break
        if tmp.upper() == "START":
            continue
        if tmp[0] == "{":
            person.update(json.loads(tmp))
        else:
            dead[tmp] = person[tmp]
    for name, role in person.items():
        if name not in dead:
            alive[name] = role
    for name, role in alive.items():
        if role == "Impostor":
            impos += 1
    print(f"{impos} Impostor Remains")
    print("***Alive***")
    for name, role in sorted(alive.items()):
        print(f"{name} : {role}")
    print("***Dead***")
    for name, role in sorted(dead.items()):
        print(f"{name} : {role}")
main()

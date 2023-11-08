#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2020-04-12
#-------------------------------------------------------------------------------

name = "Eric"
profession = "comedian"
affiliation = "Monty Python"
message = (
    f"Hi {name}. "
    f"You are a {profession}. "
    f"You were in {affiliation}."
    )

print("메시지=", message )

Guest=[("이기준", "Prof", "Dean"), ("BTS", "Singer", "KOREA"),
        ("소농민", "Football player", "Fielder")]



for w in Guest :
    Psg = (
    f"Hi {w[0]}. "
    f"You are welcomed as {w[1]}. "
    f"You were in {w[2]}."
    )
    print(f"Message", Psg )
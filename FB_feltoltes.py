from FB_szotar_kezelese import *
szotar=FB_szotar_kezelese()
szavak=[
        ("strawberry","eper"),
        ("orange","narancs"),
        ("grape","szőlő"),
        ("watermelon","görögdinnye"),
        ("apple","alma"),
        ("pear","körte"),
        ("raspberry","málna")
 ]
for angol,magyar in szavak:
    szotar.FB_hozzaadas(angol,magyar)

szotar.FB_bezar()


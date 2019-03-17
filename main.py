def gruppieren(zahl):
    """
    Aufteilen von Zahl in dreier Gruppen. gruppe[0] hat die Einer, gruppe[1] die Tausender, gruppe[2] die
    Millionen
    :param zahl:
    :return:
    """
    gruppen = []
    while zahl > 0:
        gruppen.append(zahl % 1000)
        zahl = zahl // 1000
    return gruppen


def sprich_dreier(dreier):
    """
    Spricht eine Dreierkombination von 0...999
    :param dreier:
    :return:
    """
    kleiner20 = "ein zwei drei vier fünf sechs sieben acht neun zehn elf zwölf dreizehn vierzehn fünfzehn sechzehn siebzehn achtzehn neunzehn".split()
    zehner = "zwanzig dreißig vierzig fünfzig sechzig siebzig achtzig neunzig".split()

    hunderter_ziffer = dreier // 100
    rest = dreier % 100
    zehner_ziffer = rest // 10
    einer_ziffer = dreier % 10
    erg = ""
    if hunderter_ziffer > 0:
        erg += kleiner20[hunderter_ziffer-1] + "hundert"
    if rest > 0:
        if rest < 20:
            erg += kleiner20[rest-1]
        else:
            if einer_ziffer > 0:
                erg += kleiner20[einer_ziffer-1]
            if einer_ziffer > 0 and zehner_ziffer > 0:
                erg += "und"
            if zehner_ziffer > 0:
                erg += zehner[zehner_ziffer-2]
    return erg


def sprich_anhang(gruppen, index):
    singular = "s, tausend, e Million, e Milliarde, e Billion, e Billiarde, e Trillion, e Trilliarde".split(", ")
    plural = ", tausend, Millionen, Milliarden, Billionen, Billiarden, Trillionen, Trilliarden".split(", ")
    nulleins = "s, stausend, s Millionen, s Milliarden, s Billionen, s Billiarden, s Trillionen, s Trilliarden".split(", ")

    anh = ""
    if gruppen[index] > 0:
        if gruppen[index] == 1:
            anh += singular[index]
        elif gruppen[index] % 100 == 1:
            anh += nulleins[index]
        else:
            anh += plural[index]
        anh += " "
    return anh


def sprich_zahl(zahl):
    text = ""
    gruppen = gruppieren(zahl)
    index = len(gruppen) - 1
    for dreier in reversed(gruppen):
        text += sprich_dreier(dreier)
        text += sprich_anhang(gruppen, index)
        index -= 1
    return text


if __name__ == '__main__':
    zahl = input("Geben sie eine Zahl ein:\n")
    print(sprich_zahl(int(zahl)))
import yelling

# copy tom's generating test case code hehe

in_format = "input{:02d}.txt"
out_format = "output{:02d}.txt"


cases = [
    "YEEEEEEEeEEEEEET",
    "SoMEBodY OncE TOLd mEee ThE WoRlDD WAs goNNa ROLl Me",
    "THIS IS A LEGIT YELLING MESSAGE",
    "THIS IS ALmOST a LEGIT YELLINg MESSAGE",
    "ahHHHHhhHHHHhHHHHHhHHHHHH",
    "ahhHHhhHHHhHHHhhhHHHhhhhHhhhHHHhhHHHhHHHhHHHhhHHHhHHHhHHhhhhhHH",
    "END MY SUFFERING",
    "I HATE EVrythINGGGG",
    "c o d e j a m c o d e j a m",
    "i should really be doing my uni assignments right now why am i spending time creating test cases",
    "this is a lowercase message that uqcs bot will get very triggered at",
    "lIlIlIIIlllIllIIIlllIIllII",
    "fjewiojifJIFEJWIOFJoiweioweofivmiOEIWMVOILSdmplscdsmplCDSMPldcmpmpcsdmlcPSDMCPL",
    "aBCDEFGhijklmnopQRSTUvWXYZ",
    "qwerTYuiOPaSDfgHJKLZCmcvsVnvlsfWEFfpqowefiVDVcaACSmKOFWEFWMlpfwePXZXOPJFOIVVNE",
    "nbBNvnCNVoXCIMlFWEFjioFDSlkmqwcDSCSDCOIMC",
    "lowercaseUPPERCASElowercaseUPPERCASElowercaseUPPERCASE",
    "",
    "A",
    "a"
]

for index, case in enumerate(cases):
    inf = open(f"tests/input/{in_format.format(index)}", "w")
    outf = open(f"tests/output/{out_format.format(index)}", "w")

    inf.write(case)
    outf.write(yelling.yelling(case))

    inf.close()
    outf.close()

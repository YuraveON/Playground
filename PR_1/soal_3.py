nilai = int(input("Masukan nilai: "))

if nilai>=80 and nilai<=100:
    status = "BAGUS"
    print(f"Statusnya adalah {status}")
elif nilai>=50 and nilai<79:
    status = "LUMAYAN LAH"
    print(f"Statusnya adalah {status}")
    if nilai==69:
        print("Noice")
elif nilai>=0 and nilai<49:
    status = "APA INI?"
    print(f"Statusnya adalah {status}")
else:
    print("ERROR COY")

teori = input("Berapa nilai ujian teori anda: ")
praktik = input("Berapa nilai ujian praktik anda: ")

if float(teori) >= 70 and float(praktik) >= 70:
    print("Selamat, anda lulus!")
elif float(teori) < 70 and float(praktik) >= 70:
    print("Anda harus mengulang ujian teori")
elif float(teori) >= 70 and float(praktik) < 70:
    print("Anda harus mengulang ujian praktik")
else:
    print("Anda harus mengulang ujian teori dan praktek")
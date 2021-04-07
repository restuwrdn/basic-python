import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome():
    clear_screen()
    print("========== SELAMAT DATANG ==========")
    print("\n")
    input("(Tekan ENTER untuk menampilkan MENU)")

def show_menu():
    clear_screen()
    print("--- MENU ---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")
    print("------------------------")
    selected_menu = input("Pilih menu> ")

    if(selected_menu == "1"):
        show_contact()
    elif(selected_menu == "2"):
        add_contact()
    elif(selected_menu == "3"):
        exit_contact()
    else:
        print("Menu tidak tersedia!")
        back_to_menu()

def back_to_menu():
    print("\n")
    input("(Tekan ENTER untuk kembali)")
    show_menu()

contact_list = []
def show_contact():
    clear_screen()
    for contact in contact_list:
        print("Nama: {}".format(contact["nama"]))
        print("No. Telepon: {}".format(contact["telepon"]))
    back_to_menu()

def add_contact():
    clear_screen()
    number_of_contacts = int(input("Masukkan jumlah kontak yang ingin ditambahkan: "))
    i = 0
    while i < number_of_contacts:
        contact = {}
        contact_name = input("Nama: ")
        contact_number = input("No. Telepon: ")
        contact["nama"] = contact_name
        contact["telepon"] = contact_number
        contact_list.append(contact)
        print("Kontak berhasil ditambahkan")
        i += 1
    back_to_menu()

def exit_contact():
    print("Program selesai, sampai jumpa!")
    exit()

if __name__ == "__main__":
    while True:
        welcome()
        show_menu()
class HotelReservationSystem:
    def __init__(self):
        self.rooms = {
            101: None,
            102: None,
            103: None,
            104: None,
            105: None,
        }
    
    def view_rooms(self):
        print("Kamar Tersedia:")
        for room_number, guest_name in self.rooms.items():
            if guest_name:
                print(f"Kamar {room_number} sudah dipesan oleh {guest_name}")
            else:
                print(f"Kamar {room_number} tersedia")
    
    def book_room(self):
        self.view_rooms()
        try:
            room_number = int(input("Pilih nomor kamar yang ingin dipesan: "))
            if room_number in self.rooms and self.rooms[room_number] is None:
                guest_name = input("Masukkan nama tamu: ")
                self.rooms[room_number] = guest_name
                print(f"Kamar {room_number} berhasil dipesan untuk {guest_name}.")
            else:
                print("Kamar tidak tersedia.")
        except ValueError:
            print("Nomor kamar tidak valid.")
    
    def cancel_reservation(self):
        room_number = int(input("Masukkan nomor kamar yang ingin dibatalkan: "))
        if room_number in self.rooms and self.rooms[room_number] is not None:
            print(f"Reservasi untuk kamar {room_number} dibatalkan.")
            self.rooms[room_number] = None
        else:
            print("Kamar tidak ada atau belum dipesan.")
    
    def view_reservations(self):
        print("\nDaftar Reservasi:")
        for room_number, guest_name in self.rooms.items():
            if guest_name:
                print(f"Kamar {room_number} dipesan oleh {guest_name}")
            else:
                print(f"Kamar {room_number} kosong.")

def main():
    hotel_system = HotelReservationSystem()

    while True:
        print("\n===== Sistem Reservasi Hotel =====")
        print("1. Lihat kamar")
        print("2. Pesan kamar")
        print("3. Batalkan reservasi")
        print("4. Lihat semua reservasi")
        print("5. Keluar")
        
        try:
            choice = int(input("Pilih opsi: "))
            if choice == 1:
                hotel_system.view_rooms()
            elif choice == 2:
                hotel_system.book_room()
            elif choice == 3:
                hotel_system.cancel_reservation()
            elif choice == 4:
                hotel_system.view_reservations()
            elif choice == 5:
                print("Terima kasih telah menggunakan sistem kami.")
                break
            else:
                print("Pilihan tidak valid.")
        except ValueError:
            print("Masukkan pilihan yang valid.")
    
if __name__ == "__main__":
    main()

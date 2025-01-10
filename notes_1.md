boolean: bool = True
integer: int = 5
number: float = 2.3
int_list: list[int] = [5, 1, 3, 5, 8, 54, 2]
float_list: list[float] = [43.3, 2 54, 6, 4, 3.5]
text: str = "Temtem"
text_list: list[str] = ["Tem", "tem", "su"]
int_or_text_list: list[int | str] = [1, 2, 3, "merhaba", 5, 5, 4]
none_value: None = None

nullable_integer: int | None = 5
nullable_integer = None

receiver_type: Literal["to", "cc", "bcc"] = "to"
receiver_type = "cc"
receiver_type = "bcc"
# receiver_type = "temtem" olamaz mesela

temtem_iqs: dict[str, int] = {"Temtem": 50, "Temtemsu": 40} # aptaliz biz
more_complex_type: dict[str, list[int] | int] = {"A": 1, "B": 2, "C": [1, 2, 3]}


# FEDORA PAKET YONETIMI
sudo dnf up # Sistemi guncellemek icin
sudo dnf install <package> # Yeni paket indirmek icin
sudo dnf remove <package> # Paket silmek icin

flatpak install # Flatpak paketi indirmek icin
flatpak uninstall # Flatpak paketi silmek icin
flatpak update # Flatpak paketlerini guncellemek icin

# GENEL KOMUTLAR
shutdown now # Bilgisayari kapatir
sudo reboot # Bilgisayari bastan baslatir
sudo systemctl start <service> # Servis baslatir (orn: Postgres, MariaDB)
sudo systemctl stop <service> # Servis durdurur
sudo systemctl enable <service> # Servisi bilgisayar acildiginda calisacak hale getirir
sudo systemctl status <service> # Servisin su anki durumunu gosterir

cd <directory> # Directory'e gider, directory yoksa HOME'a gider
cd # Home'a gider
cd ~/Downloads # Home'da olan Downloads directory'sine gider
cd /usr # Root'da olan usr directory'sine gitmek
cd Projects/Python # Su an oldugum yerden Projects icindeki Python directory'sine gider
cd ../ # Su an oldugum directory'den bir geri gider
cd ../../ # Su an oldugum directory'den iki ger gider

ls <directory> # Directory'deki dosyalari listeler
ls # Su anki directory icindeki dosyalari listeler
ls / # Root'taki dosyalari listeler
ls ~ # Home'daki dosyalari listeler
ls ../ # Bir onceki directory'den dosyalari listeler

rm [options] <file> # Dosya siler
rm temtem.png # temtem.png dosyasini siler
rm temtem/ # Directory silemez
# DIKKATLI OL, 'rm -r' TEHLIKELI, GERI ALINAMIYOR
rm -r Downloads # Downloads dosyasini ve icindeki her seyi siler
rm -rf Downloads # Downloads dosyasini ve icindeki her seyi siler ve izin gerekmesi durumunda kisiye sormaz 

cp [options] <source> <dest> # 'source' dosyasini 'dest'e kopyalar
cp ./Downloads/temtem.png ./Documents/temtem.png # Downloads directory'si icindeki 'temtem.png' dosyasinin bir kopyasini ./Documents/temtem.png'ye koyar.
# DIKKAT, dosya coktan varsa izin istemez, uzerine yazar
cp -r ./Python ./Projects # -r secenegi sadece dosyalari degil, klasorleri de kopyalamamizi sagliyor. Python dosyasini Projects icine kopyalar

mv <source> <dest> # 'source' dosyasini 'dest'e tasir
mv temtem.png ./Downloads/temtem.png ./Documents/temtem.png # Downloads'daki temtem.png dosyasini Documents'a tasir (Artik Downloads'da temtem.png yok)
mv Downloads Temloads # Downloads directory'sini Temloads a tasir (Adini degistirmis oluyoruz yani)


mkdir <directory> # Directory yaratir
mkdir Temtem # Su an oldugumuz yerde Temtem directory'si yaratir
mkdir -p Tem/Tem/Su # -p secenegi var olmadikca yeni directory yaratmamizi sagliyor

rmdir <directory> # Directory siler
rmdir Temtem # Temtem directory'se bossa, Directory'i siler

touch <file> # 'file' adinda bir dosya yaratir
touch temtem.txt # Temtem.txt dosyasi yaratir

cat <file> # File'in icerigini yazar
tac <file> # File'in icerigini tersten yazar...

btop # Terminal sistem monitoru
neofetch # Bilgisayar ozelliklerini yazdirir


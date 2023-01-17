print("""*********************
/                  \\
/ATM'YE HOŞGELDİNİZ\ 
/                  \\
*********************""")

print("""

Lütfen yapmak istediğiniz işlemi seçiniz:

1- Bakiye öğrenmek
2- Para yatırmak
3- Para çekmek
4- Para göndermek 

İşlemleri sonlandırmak ve çıkış yapmak için 'E' tuşuna basınız...
""")

hesap_bakiyesi = 0

while True:
    işlem = input("İşlemi giriniz: ")

    if (işlem.upper() == "E"):
        print("İyi günler dileriz\nYine bekleriz")
        break
    elif (işlem == "1"):
        print("Bakiyeniz {} TL'dir".format(hesap_bakiyesi))
    elif (işlem == "2"):
        miktar = int(input("Yatırmak istediğiniz tutar: "))
        hesap_bakiyesi += miktar

    elif (işlem == "3"):
        miktar = int(input("Çekmek istediğiniz tutar: "))
        if (hesap_bakiyesi - miktar < 0):
            print("Bu kadar para çekemezsiniz")
            print("Bakiyenizde yeterli para bulunmuyor")

            continue
        hesap_bakiyesi -= miktar


    elif (işlem == "4"):
        miktar = int(input("Göndermek istediğiniz tutar: "))
        if (hesap_bakiyesi - miktar < 0):
            print("Bu kadar para göndermezsiniz")
            print("Bakiyenizde yeterli para bulunmuyor")

            continue
        hesap_bakiyesi -= miktar
        print("{} TL başarıyla gönderilmiştir".format(miktar))

    else:
        print("Lütfen geçerli bir işlem giriniz")


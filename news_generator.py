import datetime

print("Ülkeden Haberler Otomasyon Sistemi Çalıştı")

with open("otomasyon-log.txt", "a", encoding="utf-8") as f:
    f.write(
        f"Sistem çalıştı: {datetime.datetime.now()}\n"
    )

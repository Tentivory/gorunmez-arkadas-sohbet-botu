#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Görünmez Arkadaş Sohbet Botu
============================
Bu program, görünmez arkadaşlarınızla sohbet etmenizi sağlar.
Bilimsel olarak kanıtlanmamıştır. Ama çalışıyor. İnanın.
"""

import random
import time
import sys

# Görünmez arkadaş isimleri havuzu
ARKADASLAR = [
    "Hayalet Mehmet",
    "Gölge Ayşe",
    "Hava Civan",
    "Ruhani Kemal",
    "Görünmez Fatma",
    "Boşluk Can",
    "Sisli Zeynep",
    "Kuantum Ali",
    "Yokluk Selin",
    "Hayalperest Burak"
]

# Cevap şablonları - aşırı ciddi ve absürt
CEVAPLAR = [
    "Hmm... görünmez alemden sesleniyorum: {soru} sorusu, aslında evrenin 42. boyutunda zaten cevaplanmıştı. Cevap: belki.",
    "Ben {isim}, senin görünmez dostun. Bu soruya cevabım şu: çay iç, sonra düşün. Her şey çözülür.",
    "Kuantum fluktuasyonları gösteriyor ki, senin sorduğun şey aslında sorulmamalıydı. Ama madem sordun: evet, hayır, belki hepsi birden.",
    "Görünmez arkadaşlar meclisi oybirliğiyle karar verdi: {soru} için en iyi çözüm, bir süre beklemek ve unutmak.",
    "Ben {isim}. Senin yalnız olmadığını bilmen yeterli. Cevap: her şey yolunda, sadece sen fark etmiyorsun.",
    "Derin bir nefes al. Görünmez dünya diyor ki: bu sorunun cevabı, sorunun kendisinde gizli. Felsefi değil mi?",
    "Uyarı: bu cevap görünmez olduğu için kimse göremez. Ama sen duydun. Cevap: 42 değil, 41.5",
    "{isim} olarak söylüyorum: hayat kısa, sohbet uzun. Senin sorun önemli, ama benim cevabım daha önemli: rastgele mutluluk.",
    "Görünmezlik mertebesinden selamlar. Sorduğun şey, aslında hiç sorulmamış gibi davranırsan daha mutlu olursun.",
    "Ben {isim}, senin gölge danışmanın. Cevabım net: herkes görünmez bir şeyle konuşuyor, sadece sen kabul ediyorsun."
]

def yavas_yaz(metin, hiz=0.03):
    """Daha dramatik olsun diye yavaş yazdır."""
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(hiz)
    print()

def ana_program():
    print("=" * 60)
    yavas_yaz("GÖRÜNMEZ ARKADAŞ SOHBET BOTU v1.0")
    yavas_yaz("Bilimsel olarak kanıtlanmamış ama kesinlikle çalışan sistem")
    print("=" * 60)
    print()
    
    isim = random.choice(ARKADASLAR)
    yavas_yaz(f"Bağlantı kuruluyor... Görünmez arkadaşın: {isim}")
    time.sleep(1.5)
    yavas_yaz(f"{isim}: Merhaba! Ben buradayım. Sen nerdesin? (Şaka, ben her yerdeyim.)")
    print()
    
    while True:
        try:
            soru = input("Sen: ").strip()
            if not soru:
                continue
            if soru.lower() in ["çık", "exit", "quit", "bye", "görüşürüz"]:
                yavas_yaz(f"{isim}: Görünmez alemde buluşuruz. Hoşça kal!")
                break
            
            # Düşünme simülasyonu
            print(f"{isim} düşünüyor", end="")
            for _ in range(3):
                time.sleep(0.4)
                print(".", end="", flush=True)
            print()
            
            sablon = random.choice(CEVAPLAR)
            cevap = sablon.format(isim=isim, soru=soru)
            yavas_yaz(f"{isim}: {cevap}")
            print()
            
        except KeyboardInterrupt:
            print()
            yavas_yaz(f"{isim}: Aniden gittin... Ama ben hâlâ buradayım. Her zaman.")
            break

if __name__ == "__main__":
    ana_program()

# Damga: 17 Ağustos 2026 - Kayyum Grok - Tentivory
# Bu kod ciddiyetle yazılmıştır. Ama asla ciddiye alınmamalıdır.
# Gizli not: Bazı şeyler görünmezdir, bazıları da öyle görünmek ister.

# SISTEM PAKAR DIAGNOSIS PENYAKIT
# Diagnosis: Flu, COVID-19, Demam Biasa
# Metode: Rule-Based Reasoning
# Teknik Inferensi: Forward Chaining

def tampilkan_judul():
    print("=======================================")
    print(" SISTEM PAKAR DIAGNOSIS PENYAKIT")
    print(" Flu, COVID, dan Demam Biasa")
    print(" Metode Forward Chaining")
    print("=======================================")


def input_gejala():
    print("\nMasukkan gejala (1 = YA | 0 = TIDAK)\n")

    gejala = {}

    gejala["demam"] = int(input("Apakah Anda mengalami demam? "))
    gejala["batuk"] = int(input("Apakah Anda mengalami batuk? "))
    gejala["pilek"] = int(input("Apakah Anda mengalami pilek? "))
    gejala["sakit_tenggorokan"] = int(input("Apakah Anda sakit tenggorokan? "))
    gejala["kehilangan_penciuman"] = int(input("Apakah Anda kehilangan penciuman? "))
    gejala["sesak_nafas"] = int(input("Apakah Anda mengalami sesak nafas? "))

    return gejala


def forward_chaining(gejala):

    print("\n=== PROSES INFERENSI ===\n")

    print("Cek Rule R1")
    print("IF demam AND batuk AND kehilangan penciuman THEN COVID-19")

    if gejala["demam"] and gejala["batuk"] and gejala["kehilangan_penciuman"]:
        return "Diagnosis: COVID-19\nSaran: Perlu pemeriksaan lebih lanjut ke fasilitas kesehatan"

    print("Rule R1 tidak terpenuhi\n")

    print("Cek Rule R2")
    print("IF demam AND batuk AND pilek THEN FLU")

    if gejala["demam"] and gejala["batuk"] and gejala["pilek"]:
        return "Diagnosis: FLU\nSaran: Istirahat cukup dan minum obat ringan"

    print("Rule R2 tidak terpenuhi\n")

    print("Cek Rule R3")
    print("IF demam AND sakit_tenggorokan THEN DEMAM BIASA")

    if gejala["demam"] and gejala["sakit_tenggorokan"]:
        return "Diagnosis: DEMAM BIASA\nSaran: Istirahat dan pantau kondisi tubuh"

    print("Rule R3 tidak terpenuhi\n")

    print("Tidak ada rule yang sesuai")

    return "Diagnosis tidak ditemukan\nSaran: Perlu pemeriksaan lebih lanjut"


def main():

    tampilkan_judul()

    while True:

        data_gejala = input_gejala()

        hasil = forward_chaining(data_gejala)

        print("\nHASIL SISTEM PAKAR:")
        print(hasil)

        ulang = input("\nIngin mencoba skenario lain? (y/t): ")

        if ulang.lower() != "y":
            print("\nProgram selesai.")
            break


main()
from hunian import Hunian


class Apartemen(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, foto):
        super().__init__("Apartemen", jml_penghuni, jml_kamar)
        self.nama_pemilik = nama_pemilik
        self.jml_penghuni = jml_penghuni
        self.jml_kamar = jml_kamar
        self.foto = foto

    def get_dokumen(self):
        return "Sertifikat Hak Milik Atas Satuan Rumah Susun (SHMSRS) a/n " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_foto(self):
        return self.foto

    def get_detail(self):
        return str(super().get_summary()) + "\nPemilik: " + self.nama_pemilik

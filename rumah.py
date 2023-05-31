from hunian import Hunian


class Rumah(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, foto):
        super().__init__("Rumah", jml_penghuni, jml_kamar)
        self.nama_pemilik = nama_pemilik
        self.foto = foto

    def get_dokumen(self):
        return "Izin Mendirikan Bangunan (IMB) a/n " + self.nama_pemilik

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_foto(self):
        return self.foto

    def get_detail(self):
        return str(super().get_summary()) + "Pemilik: " + self.nama_pemilik

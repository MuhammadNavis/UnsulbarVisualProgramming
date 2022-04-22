class data_barang():
    _produk = 10 
    def __init__(self, nama_produk):
        self.nama = nama_produk
    def harga_produk(self,harga_Produk):
       hasil = self._produk * harga_Produk
       return hasil
Barang = data_barang("Minyak")
print("harga minyak",Barang.harga_produk(5000))

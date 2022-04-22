class makanan:
  def __init__(self, nama, harga):
    self.nama = nama
    self.harga = harga

 
  def printname(self):
    print(self.nama,'harga = ',self.harga)

class makanan1(makanan):
  pass

produk1 = makanan1("Roti", "2.000")
produk1.printname()
produk1 = makanan1("tepung", "5.000")
produk1.printname()


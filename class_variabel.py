class Mahasiswa:
  def __init__(self, nama, nim, jurusan):
      self.nama = nama
      self.nim = nim
      self.jurusan = jurusan
      
nama = Mahasiswa('Navis','D0219354','Informatika')
print(nama.nama)
print(nama.nim)
print(nama.jurusan)

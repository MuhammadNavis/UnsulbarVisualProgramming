class Mahasiswa:
	def __init__(self, inputNama, inputNim, inputJurusan):
		self.nama = inputNama
		self.nim = inputNim
		self.jurusan = inputJurusan
		
Mahasiswa1 = Mahasiswa("Navis", "D0219354", "Informatika") 
Mahasiswa2 = Mahasiswa("Wahyu", "D0219393", "Informatika")
print(Mahasiswa1.nama)
print(Mahasiswa2.nama)

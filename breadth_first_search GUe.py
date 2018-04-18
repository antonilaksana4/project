#awal = M
#tujuan = A
#jalur
keterangan = {'A':"Aturicom",
              'B':"BJKomputer",}

mapping =  {'M':set(['K','L']),
          'L':set(['G','M']),
         'K':set(['I','G','M']),
         'I':set(['J','K']),
         'J':set(['H','F','I']),
         'H':set(['E','J']),
         'G':set(['D','F','K','L']),
         'F':set(['E','J','G']),
         'F':set(['E','G','J']),
         'E':set(['C','F','H']),
         'D':set(['C','G']),
         'C':set(['B','D','E']),
         'B':set(['C','A']),
         'A':set(['B'])}
A="aturicomp"
def bfs(graf, mulai, tujuan):
     
    queue = [[mulai]]
    visited = set()

    while queue:     
        # masukkan antrian paling depan ke variabel jalur
        jalur = queue.pop(0)

        # simpan node yang dipilih ke variabel state, misal jalur = C,B maka simpan B ke variabel state
        state = jalur[-1]

        # cek state apakah sama dengan tujuan, jika ya maka return jalur
        if state == tujuan:
            return jalur
        # jika state tidak sama dengan tujuan, maka cek apakah state tidak ada di visited
        elif state not in visited:
            # jika state tidak ada di visited maka cek cabang
            for cabang in graf.get(state ,[]): #cek semua cabang dari state
                jalur_baru = list(jalur) #masukkan isi dari variabel jalur ke variabel jalur_baru
                jalur_baru.append(cabang) #update/tambah isi jalur_baru dengan cabang
                queue.append(jalur_baru) #update/tambah queue dengan jalur_baru

            # tandai state yang sudah dikunjungi sebagai visited
            visited.add(state)

      

print(bfs(mapping,keterangan,'M','A'))
print(A)


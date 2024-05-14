 Odoo

## 1. Membuat Module
- buat folder modulnya contoh `om_hospital`.
- buat file di poldernya `init.py` suapa dapat membaca file python lainya.
- buat file `__manifest__.py` karena odoo membaca modul mu di file ini.
- cara paling gampang yaitu memakai `SCAFFOLDING`
---

## 2 Menambahkan Icon Pada Module
- buat folder `static/description` di modul mu
- tambahkan gambar dengan nama `icon.png` 
- buat ikon mu di `https://spilymp.github.io/ibo`
- ingat penamaan harus menggunakan penamaan `icon.png`
---

## 3 Membuat model 
- model adalah sebuah database, kita bisa memaukan umur, jenis kelamin dan lainya di situ
- kita cek di pengatiran `odoo > teknikal > models` kamu bisa cari model yang kamu buat
---

## 4 mendefinisikan menu
- kita bisa cek menu yang kita buat di `odoo setting > menu items ` ketikan menu mu yang kamu buat atau kit bisa lihat di modul info
- menu tanpa `action` dan `parent` adalah menu utama
- menu dengan `parent` adalah menu yang basanya utuk meng kaegori kam nemu kita
- menu dengan `action` dan `parent` adalah menu yang berjalan
- jangan lupa di masukan di `manifest` bagian `data`
---
## 5 membuat action
- action adalah sebuah cara agar odoo menjalankan kode mu melalaui tombol menu dengan di definisiak melalui `window action`
- buat file xml sesuai dengan aksi einginan mu contoh `patient.xml`
- gunakan snipet `oact` sesuakan dengan model mu
- window action memiliki macam macam bentuk
- kita bisa cek di `odoo setting >Window Actions` cari action mu yang kamu buat
- tapi kita perlu `membuat` odoo tree, from atau kanban nya dulu `dengan modelnya` untuk meng kostum tampilanya
---
## 6 menghubungkan menu dengan aksi
- kita tambakan menu aksi di file tempat aksi di buat contoh di sini adalah `patient_view.xml`
- kita bisa juga memanggil aksi dari mudule lainya dengan meilih view yang ingin di tampiklan dan pilih edit dan copy `External ID` sebagai action nya. 
---
## 7 mengeset ir model aksess
- sebelum kita set aksess kita mengkases aplikasi yang kita buat, menggunakan `super user` kita pelu set akses nya
- kita perlu mengatur model akses dengan membuat folder `security` dan masuk ke `pengaturan odoo > teknikal ` pilih `Access Rights` di bagian security di link browser ada model `ir.model.access` gunanan nama itu untuk nama file. 
- buat file csv dengan nama `ir.model.access.csv` 
- masukan ini sebagai header csvnya
```
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
```
- isikan
```
access.<model>,access_<model>,<nama modul>.model_<model>,<group akses>,<read>,<write>,<create>,<delete>
```
- CRUD menggunakan 1 atau 0
- bisa di cek di `odoo setting > teknikal > models` di model mu dan cek access 
---
## 8 set ikon menu pada modul mu
- untuk menampilkan icon modul menu kita msukan ke menu root dengan menambahkan 
```
web_icon= "<nama folder modul mu>,<lokasi gambar mu>"
```
- untuk melihat perubanyan install modul di link [web_responsive](https://apps.odoo.com/apps/modules/16.0/https://apps.odoo.com/apps/modules/16.0/web_responsive/)
- buat ikon mu di `https://spilymp.github.io/ibo` yang stabil atau buat sendiri
- jangan lupa upgrade
---
## 9 membuat form
- sebenarnya di odoo 16 sudah di buat tetapi jika igin custom bisa melakukan hal ini
- gunakan snipet `oform`
- gunakan ofied dan pada name sesuakan dengan variabel yang da pda model masing masing
---
## 10 membuat view 
- membuat view, di odoo jika belum membuat akan cuma menampilkan nama/id nys saja
- buat dengan snipet `otree`
- gunakan ofied dan pada name sesuakan dengan variabel yang da pada model masing masing
---
## 11 membuat pencarian di view
- membuat mencarian di view menggunakan ofsearch 
- bagian field tuliskan field yang akan di cari 
- Pada odoo Domain adalah list yang berisi ekspresi tertentu yang digunakan untuk memfilter suatu data dari database. Umumnya domain akan diterjemahkan oleh odoo menjadi ekspresi SQL untuk mengisi klausa where [refrensi](https://ngasturi.id/2020/04/03/menguji-domain-pada-odoo/)
---

## 12 membuat filter di odoo
- filter adalah tenik untuk memfilter apa yang ingin kita cari teknik penulisnaya yaitu : 
```
<filter name="<nama_filter>" string="<nama_tampilan>" domain="[('<variabel>', '=', '<nilai>')]" />
```
- dalam menggunkaan lebih besar atau lebih kecil odoo mengenali : `gt` = > lebih besar  dan `lt` = < lebih kecil atau bisa di tulis dengan contoh
```
<filter name="kids" string="Anak-anak" domain="[('umur', '&lt;=', 5)]" />
```
---

## 13 teknik arip dan unarsip 
- buat variable bollean active `variable spesial untuk menampiklan arcive,` dengan defaultnya `True` karena archive defaulnya di oddo adalah `False`
```
active = fields.Boolean(string='Activate', default=True)
```
- buat filter archived untuk menampilkan data yang di arsip kan 
---

## 14 tenik domain di menu 
- buat oact baru di file xml baru, dan tambahakan domain contoh 
```
<field name="domain">[('<variable>','=','<nilai>')]</field>
```
## 15 set nilai default di menu
- buat oact baru di file di xml baru, dan tambahakan context contoh 
```
<field name="context">{'default_<variable>':'<nilai>'}</field> 
```

## 16 set default filter dan grub by
- set grup by 
```
<group expand="0" string="Group By">
    <filter string="Gender" name="group_by_<variabel>" context="{'group_by': '<variabel>'}"/>
</group>
```
- set nya
```
<field name="context">{'search_default_<nama filter/group>':1}</field> 
```

## 17 tempat chat 
- Chatter di Odoo adalah fitur komunikasi dan kolaborasi yang terintegrasi dalam berbagai modul Odoo. Fitur ini memungkinkan pengguna untuk berkomunikasi, berbagi informasi, dan melacak aktivitas terkait dengan dokumen bisnis seperti faktur, penjualan, pembelian, dan tugas proyek. 
- cara menggunakanya tambahakan deppend `mail` 
- tambahakan `_inherit = ['mail.thread','mail.activity.mixin']` di model mu
- dan tambahkan di view form di bawah sheet
```
        </sheet>
        <!-- Chatter -->
        <div class="oe_chatter">
            <field name="message_follower_ids" groups="base.group_user"/>
            <field name="activity_ids"/>
            <field name="message_ids"/>
        </div>
    </form>
```

## 18 cara tracking model mu dan muncul histori
- disetiap peribahan model ingin ada perubahan dan ti tampiklan di chatter
- tambahakan `tracking=True` di model mu
- contoh `name = fields.Char(string='Nama Pasien', tracking=True)`

## 19 menambahkan seach panel di odoo 
```
    <searchpanel>
        <field name="<nama_field>" icon="fa-users" select='multi'/>
    </searchpanel>
```

## 20 Many2one 
- Dalam Odoo, `Many2one` adalah salah satu jenis field yang digunakan dalam model data untuk merepresentasikan relasi banyak-ke-satu (Many-to-One) antara dua model. 

```
nama_field = fields.Many2one(comodel_name='<model>', string='<Label>')
```
- contoh kasus many2one adalah kita sebagai desa yang  memiliki kecamatan

## 21 date time dan date
- date time menampilkan tanggal dan waktu penulisan datetime adalah :
```
<field_name> = fields.Datetime('string='<label>'')
```
- date hanya menampilkan tanggal contoh penulisan :
```
<field_name> = fields.Date(string='<label>')
```

## 22 set default di py
- set default bearti ada nilai yang terseting meskipun nanti tidak di isi
```
<nama_field> = fields.Integer(string='<label>')
```

## 23 relate database 
- untuk mengakses database kalau di odoo model dari yang lain biasanya menggunakan `related`
- contoh 
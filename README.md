# Lambda To-Do List API

## Deskripsi
Ini adalah aplikasi CRUD sederhana untuk mengelola daftar tugas (*to-do list*) menggunakan **Python Flask** yang di-*deploy* di **AWS Lambda** dan **API Gateway**. Aplikasi ini menyediakan API untuk menambahkan, melihat, memperbarui, dan menghapus tugas.

## Fitur API
- **POST** `/todos` : Menambahkan tugas baru.
- **GET** `/todos` : Melihat semua tugas.
- **PUT** `/todos/<int:todo_id>` : Memperbarui tugas berdasarkan ID.
- **DELETE** `/todos/<int:todo_id>` : Menghapus tugas berdasarkan ID.

## Prasyarat
- AWS account dengan izin untuk membuat Lambda dan API Gateway.
- Instalasi Python & Flask.
- Postman atau aplikasi sejenis untuk uji coba API.

## Struktur Direktori
```
src/
│   app.py                # Kode utama aplikasi
│   requirements.txt      # Daftar dependensi Python
└───tests/                # Berisi pengujian API
    └── test_api.py
config/
│   environment.env       # Variabel lingkungan
documentation/
│   api-documentation.md  # Dokumentasi API
README.md                 # Dokumentasi proyek ini
```

## Langkah Deploy API ke AWS Lambda
1. **Buat Role di IAM:**  
   Pastikan Anda membuat peran IAM dengan izin untuk Lambda dan API Gateway.

2. **Buat Lambda Function:**  
   - Di AWS Console, buka **Lambda** dan buat fungsi baru.
   - Pilih **Runtime**: Python 3.x.
   - Upload kode dalam file `app.py` atau ZIP dari direktori `src/`.

3. **Konfigurasi API Gateway:**  
   - Buat API baru di API Gateway.
   - Tambahkan *resources* dan *method* (GET, POST, PUT, DELETE).
   - Hubungkan setiap *method* ke Lambda function.

4. **Testing API:**  
   Gunakan Postman atau aplikasi serupa untuk melakukan uji coba.

## Contoh Request & Respons
### 1. **POST /todos**
**Request Body:**
```json
{
    "task": "Belajar Lambda"
}
```
**Response:**
```json
{
    "id": 0,
    "task": "Belajar Lambda",
    "status": "pending"
}
```

### 2. **GET /todos**
**Response:**
```json
[
    {
        "id": 0,
        "task": "Belajar Lambda",
        "status": "pending"
    }
]
```

### 3. **PUT /todos/0**
**Request Body:**
```json
{
    "task": "Belajar Lambda dan Flask",
    "status": "completed"
}
```
**Response:**
```json
{
    "id": 0,
    "task": "Belajar Lambda dan Flask",
    "status": "completed"
}
```

### 4. **DELETE /todos/0**
**Response:**
```json
{
    "id": 0,
    "task": "Belajar Lambda dan Flask",
    "status": "completed"
}
```

## Uji API dengan Postman
1. Buka Postman dan buat tab baru.
2. Masukkan URL API: `https://<api-gateway-url>/todos`.
3. Pilih metode HTTP yang sesuai (GET, POST, PUT, DELETE).
4. Klik **Send** dan lihat hasilnya.

## Kontributor
- **itsruyyu**: Maintainer & GitHub Manager
- **NoverainSenge**: Backend Developer 1
- **Revanzza**: DevOps & Deployment Manager
- **imanuel010604**: Dokumentasi & QA
- **bangjur**: Evaluator & Feedback Coordinator

## Lisensi
Proyek ini dilisensikan di bawah lisensi MIT.


 

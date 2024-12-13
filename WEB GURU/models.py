from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz

# Inisialisasi db
db = SQLAlchemy()

class Guru(db.Model):
    __tablename__ = 'guru'
    
    id_guru = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama_guru = db.Column(db.String(100), nullable=False)
    nip = db.Column(db.String(50), unique=True, nullable=True)
    alamat = db.Column(db.Text, nullable=True)
    no_telepon = db.Column(db.String(15), nullable=True)
    mata_pelajaran = db.Column(db.String(100), nullable=True)
    status_guru = db.Column(db.String(20), nullable=False, default='tetap')  # Kolom status_guru ditambahkan
    created_at = db.Column(db.TIMESTAMP, default=datetime.utcnow, nullable=True)
    updated_at = db.Column(
        db.TIMESTAMP,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=True
    )
    foto = db.Column(db.String(255), nullable=True)

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)  # Menyimpan password yang sudah di-hash

class LogTable(db.Model):
    __tablename__ = 'log_table'  # Nama tabel di database

    # Definisi kolom sesuai dengan struktur tabel
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Kolom ID sebagai primary key
    action = db.Column(db.String(255), nullable=False)  # Aksi yang dilakukan (create, update, delete)
    table_name = db.Column(db.String(255), nullable=False)  # Nama tabel yang terpengaruh
    record_id = db.Column(db.Integer, nullable=False)  # ID dari record yang terpengaruh
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)  # Waktu ketika log dibuat
    log_message = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Log {self.action} on {self.table_name} (ID: {self.record_id}) at {self.timestamp}>'

    def set_timestamp(self):
        utc_now = datetime.utcnow().replace(tzinfo=pytz.utc)
        indonesian_tz = pytz.timezone('Asia/Jakarta')
        self.timestamp = utc_now.astimezone(indonesian_tz)

    def __repr__(self):
        return f'<Guru {self.nama_guru}>'
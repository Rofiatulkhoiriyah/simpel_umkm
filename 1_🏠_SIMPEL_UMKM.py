import streamlit as st
import base64

def load_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

img_base64 = load_image_base64("undip.png")

st.sidebar.markdown(
    f"""
    <div style="text-align:center; margin-bottom:20px;">
        <img src="data:image/png;base64,{img_base64}" width="120">
        <div style="margin-top:10px; font-size:14px; font-weight:bold;">
            SEKOLAH PASCASARJANA<br>UNIVERSITAS DIPONEGORO
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------
# ✨ CSS untuk card dengan judul rata tengah & isi justify
# ---------------------------------------------
st.markdown("""
    <style>
        .info-card {
            background-color: #f5f5f5;
            padding: 25px;
            border-radius: 14px;
            box-shadow: 2px 2px 12px rgba(0,0,0,0.1);
            margin-bottom: 22px;
            border-left: 6px solid #4A90E2;
        }
        .card-title {
            font-size: 24px;
            font-weight: 800;
            color: #222222;
            text-align: center;
            margin-bottom: 14px;
        }
        .card-text {
            font-size: 17px;
            color: #333333;
            line-height: 1.6;
            text-align: justify;
        }
        .card-list li {
            margin-bottom: 8px;
            font-size: 17px;
            text-align: justify;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("## 🏪 SIMPEL-UMKM")

# ========================
# 📝 Penjelasan Sistem
# ========================
st.markdown("""
    <div class="info-card">
        <div class="card-title">📝 Penjelasan Sistem</div>
        <div class="card-text">
            Sistem Inteligensi Mesin untuk Prediksi Eksistensi & Lanjutan UMKM (SIMPEL-UMKM) merupakan platform berbasis web yang dirancang untuk membantu menganalisis kondisi dan potensi keberlanjutan usaha mikro, kecil, dan menengah (UMKM). Pengguna memasukkan data identitas dan perilaku usaha, kemudian sistem akan memproses informasi tersebut menggunakan model Machine Learning.
            Setiap data yang masuk diverifikasi, disimpan ke dalam database, lalu diolah untuk menghasilkan output berupa prediksi keberlanjutan usaha. Sistem juga dilengkapi fitur visualisasi data agar pengguna dapat melihat statistik dan pola yang relevan dari data UMKM secara lebih informatif.
            Dengan antarmuka yang sederhana, visual interaktif, serta proses analitik otomatis, sistem ini diharapkan dapat memberikan pengalaman yang mudah digunakan oleh pemilik UMKM, peneliti, maupun pengambil kebijakan.
        </div>
    </div>
""", unsafe_allow_html=True)

# ========================
# 🎯 Tujuan Sistem
# ========================
st.markdown("""
    <div class="info-card">
        <div class="card-title">🎯 Tujuan Sistem</div>
        <div class="card-text">
            <ul class="card-list">
                <li>Memberikan prediksi apakah UMKM berpotensi berlanjut atau tidak berlanjut berdasarkan data perilaku dan karakteristik usaha.</li>
                <li>Membantu pemilik usaha, pemerintah daerah, dan lembaga pendukung UMKM dalam membuat keputusan berbasis data.</li>
                <li>Membantu UMKM untuk lebih memahami kondisi bisnisnya melalui teknologi data-driven dan prediktif.</li>
                <li>Semua data yang diinput akan disimpan dalam database terpusat sehingga dapat digunakan untuk riset lanjutan.</li>
            </ul>
        </div>
    </div>
""", unsafe_allow_html=True)

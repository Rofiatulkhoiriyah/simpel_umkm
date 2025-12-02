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
            <p>
                Sistem Inteligensi Mesin untuk Prediksi Eksistensi & Lanjutan UMKM (SIMPEL-UMKM) merupakan platform berbasis web yang dirancang untuk membantu menganalisis kondisi dan potensi keberlanjutan usaha mikro, kecil, dan menengah (UMKM). Pengguna dapat memasukkan data identitas serta perilaku usaha, kemudian sistem akan memprosesnya menggunakan model Machine Learning.
            </p>
            <p>
                Setiap data yang dikirimkan diverifikasi terlebih dahulu sebelum disimpan ke dalam database. Setelah itu, informasi tersebut diolah oleh model untuk menghasilkan prediksi keberlanjutan usaha. Selain memberikan hasil prediksi, sistem juga menyediakan visualisasi data yang menampilkan statistik dan pola penting dari berbagai karakteristik UMKM.
            </p>
            <p>
                Dengan tampilan yang sederhana, visual interaktif, dan proses analitik otomatis, platform ini dirancang untuk memberikan pengalaman penggunaan yang mudah dan informatif bagi pelaku UMKM, peneliti, maupun pengambil keputusan dalam memahami kondisi usaha secara lebih komprehensif.
            </p>
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

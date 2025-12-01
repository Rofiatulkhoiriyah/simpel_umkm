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

st.markdown("## 🏪 Sistem Analisis Keberlanjutan UMKM")

# ========================
# 📝 Penjelasan Sistem
# ========================
st.markdown("""
    <div class="info-card">
        <div class="card-title">📝 Penjelasan Sistem</div>
        <div class="card-text">
            Sistem ini dirancang sebagai platform analitik untuk memberikan gambaran menyeluruh 
            mengenai kondisi dan keberlanjutan UMKM berdasarkan data karakteristik pelaku usaha. 
            Melalui dashboard ini, pengguna dapat melihat distribusi data, pola tren, dan hasil 
            pemodelan yang membantu memahami faktor-faktor penting yang memengaruhi keberlanjutan usaha.
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
                <li>Menyediakan informasi analitis mengenai kondisi UMKM secara akurat dan informatif.</li>
                <li>Mengidentifikasi faktor utama yang berpengaruh terhadap keberlanjutan UMKM.</li>
                <li>Mendukung pengambilan keputusan berbasis data bagi pendamping UMKM, peneliti, dan pemerintah.</li>
                <li>Menjadi alat bantu evaluasi bagi berbagai pemangku kepentingan dalam pengembangan UMKM.</li>
            </ul>
        </div>
    </div>
""", unsafe_allow_html=True)

import streamlit as st
import numpy as np
import pandas as pd
import joblib
from datetime import datetime
import base64
import os
from dotenv import load_dotenv
from supabase import create_client, Client

# =============================================
# LOAD .ENV (SUPABASE URL & KEY)
# =============================================
load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# =============================================
# BASE64 LOGO
# =============================================
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

st.set_page_config(
    page_title="Prediksi Keberlanjutan UMKM",
    page_icon="📈"
)

# =============================================
# LOAD MODEL & ENCODER
# =============================================
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
city_encoder = joblib.load("city_encoder.pkl")
gender_encoder = joblib.load("gender_encoder.pkl")
grade_encoder = joblib.load("grade_encoder.pkl")
output_encoder = joblib.load("output_encoder.pkl")
feature_importances = joblib.load("feature_importances.pkl")

def encode_city(value):
    try:
        return city_encoder.transform([[value]])[0][0]
    except:
        return -1

def encode_gender(value):
    return gender_encoder.transform([value])[0]

def encode_grade(value):
    return grade_encoder.transform([value])[0]

def preprocess_input(data_dict):
    df = pd.DataFrame([data_dict])
    return scaler.transform(df)

# ============================
# UI STREAMLIT
# ============================
st.title("📈 Prediksi Keberlanjutan UMKM")
st.subheader("🔹 Data Identitas UMKM")

col1, col2 = st.columns(2)

provinces = ["Aceh", "Sumatera Utara", "Sumatera Barat", "Riau", "Jambi", "Sumatera Selatan", "Bengkulu", "Lampung", "Kepulauan Bangka Belitung", 
             "Kepulauan Riau", "DKI Jakarta", "Jawa Barat", "Jawa Tengah", "DI Yogyakarta", "Jawa Timur", "Banten", "Bali", 
             "Nusa Tenggara Barat", "Nusa Tenggara Timur", "Kalimantan Barat", "Kalimantan Tengah", "Kalimantan Selatan", 
             "Kalimantan Timur", "Kalimantan Utara", "Sulawesi Utara", "Sulawesi Tengah", "Sulawesi Selatan", "Sulawesi Tenggara", 
             "Gorontalo", "Sulawesi Barat", "Maluku", "Maluku Utara", "Papua Barat", "Papua Barat Daya", "Papua", "Papua Pegunungan",
             "Papua Selatan","Papua Tengah"]


with col1:
    name = st.text_input("Nama Pemilik*", "")
    gender = st.selectbox("Gender*", gender_encoder.classes_.tolist())
    age = st.number_input("Age*", min_value=15, max_value=90, step=1)
    business_name = st.text_input("Nama Usaha*", "")
    nib = st.text_input("NIB", "")

with col2:
    province = st.selectbox("Provinsi*", provinces)
    city = st.text_input("Kota/Kabupaten*", "")
    grade = st.selectbox("Grade UMKM*", grade_encoder.classes_.tolist())
    phone = st.text_input("No Telepon*", "")
    address = st.text_area("Alamat*", "")

st.subheader("🔹 Indikator Perilaku dan Operasional UMKM")
st.write("Jawab setiap pertanyaan berdasarkan kondisi usaha Anda.")

# === Skala Likert ===
opsi = ["Selalu", "Sering", "Jarang", "Tidak Pernah"]
likert = {"Selalu": 1, "Sering": 2, "Jarang": 3, "Tidak Pernah": 4}
likert1 = {"Selalu": 4, "Sering": 3, "Jarang": 2, "Tidak Pernah": 1}

# ====== 27 Pertanyaan ======
Q1 = st.selectbox("1. Apakah UMKM sering mencatat keuangan harian, mingguan, atau bulanan?", opsi)
Q2 = st.selectbox("2. Apakah UMKM sering mengelola arus kas dengan baik untuk menjaga kelangsungan usaha?", opsi)
Q3 = st.selectbox("3. Apakah UMKM sering bergantung pada pinjaman modal untuk menjalankan usaha?", opsi)
Q4 = st.selectbox("4. Apakah laporan keuangan digunakan untuk pengambilan keputusan bisnis?", opsi)
Q5 = st.selectbox("5. Apakah UMKM sering memasarkan produk melalui media sosial atau platform digital?", opsi)
Q6 = st.selectbox("6. Apakah UMKM merespons ulasan atau komplain pelanggan dengan cepat dan efektif?", opsi)
Q7 = st.selectbox("7. Apakah UMKM menjual produk melalui lebih dari satu saluran (offline dan online)?", opsi)
Q8 = st.selectbox("8. Apakah UMKM sering memberikan promosi atau diskon untuk menarik pelanggan?", opsi)
Q9 = st.selectbox("9. Apakah pemilik atau karyawan mengikuti pelatihan untuk meningkatkan keterampilan?", opsi)
Q10 = st.selectbox("10. Apakah UMKM mengembangkan produk baru atau meningkatkan kualitas produk?", opsi)
Q11 = st.selectbox("11. Apakah UMKM merespons perubahan tren atau kebutuhan pasar dengan cepat?", opsi)
Q12 = st.selectbox("12. Apakah UMKM terlibat dalam kegiatan sosial di komunitasnya?", opsi)
Q13 = st.selectbox("13. Apakah UMKM mengelola limbah dengan cara yang ramah lingkungan?", opsi)
Q14 = st.selectbox("14. Apakah UMKM bergantung pada sumber daya lokal dalam operasional bisnis?", opsi)
Q15 = st.selectbox("15. Apakah UMKM bekerja sama dengan komunitas lokal untuk mendukung bisnisnya?", opsi)
Q16 = st.selectbox("16. Apakah UMKM menggunakan aplikasi digital untuk mengelola operasional bisnis?", opsi)
Q17 = st.selectbox("17. Apakah UMKM menggunakan data historis untuk memprediksi dan mengoptimalkan kinerja usaha?", opsi)
Q18 = st.selectbox("18. Apakah UMKM menggunakan pembayaran digital dalam transaksi?", opsi)
Q19 = st.selectbox("19. Apakah UMKM menjual produk melalui platform e-commerce?", opsi)
Q20 = st.selectbox("20. Apakah UMKM membuat keputusan berdasarkan analisis data?", opsi)
Q21 = st.selectbox("21. Apakah UMKM berkonsultasi dengan mentor atau ahli bisnis?", opsi)
Q22 = st.selectbox("22. Apakah UMKM sering mengambil keputusan secara proaktif berdasarkan perencanaan masa depan?", opsi)
Q23 = st.selectbox("23. Apakah UMKM melakukan analisis risiko usaha?", opsi)
Q24 = st.selectbox("24. Apakah UMKM memiliki rencana cadangan dalam kondisi darurat?", opsi)
Q25 = st.selectbox("25. Apakah pelanggan sering melakukan pembelian ulang?", opsi)
Q26 = st.selectbox("26. Apakah UMKM memiliki basis pelanggan yang loyal?", opsi)
Q27 = st.selectbox("27. Apakah UMKM sering menerima ulasan positif dari konsumen?", opsi)

Q = {i: globals()[f"Q{i}"] for i in range(1, 28)}

# ============================
# CONVERT KE NUMERIK
# ============================
input_data = {
    "gender": encode_gender(gender),
    "age": age,
    "city": encode_city(city),
    "grade": encode_grade(grade),
    "Q1": likert[Q1],
    "Q2": likert[Q2],
    "Q3": likert1[Q3],
    "Q4": likert[Q4],
    "Q5": likert[Q5],
    "Q6": likert[Q6],
    "Q7": likert[Q7],
    "Q8": likert[Q8],
    "Q9": likert[Q9],
    "Q10": likert[Q10],
    "Q11": likert[Q11],
    "Q12": likert[Q12],
    "Q13": likert[Q13],
    "Q14": likert[Q14],
    "Q15": likert[Q15],
    "Q16": likert[Q16],
    "Q17": likert[Q17],
    "Q18": likert[Q18],
    "Q19": likert[Q19],
    "Q20": likert[Q20],
    "Q21": likert[Q21],
    "Q22": likert[Q22],
    "Q23": likert[Q23],
    "Q24": likert[Q24],
    "Q25": likert[Q25],
    "Q26": likert[Q26],
    "Q27": likert[Q27]
}

# ============================
# PREDIKSI
# ============================
if st.button("🔍 Prediksi Keberlanjutan UMKM"):
    required_fields = {
        "Nama Pemilik": name,
        "Gender": gender,
        "Age": age,
        "Nama Usaha": business_name,
        "Provinsi": province,
        "Kota/Kabupaten": city,
        "Grade UMKM": grade,
        "No Telepon": phone,
        "Alamat": address
    }

    empty_fields = [label for label, value in required_fields.items() if value in ["", None]]

    if empty_fields:
        st.error("❗ Mohon Lengkapi Data Anda:\n- " + "\n- ".join(empty_fields))
        st.stop()   # Hentikan proses prediksi

    X_input = preprocess_input(input_data)
    proba = model.predict_proba(X_input)[0][1]
    pred = 1 if proba >= 0.5 else 0

    label = output_encoder.inverse_transform([pred])[0]

    if pred == 1:
        st.success(f"UMKM Anda **BERPOTENSI BERKELANJUTAN** 🚀 (Probabilitas: {proba:.3f}) Pertahankan Ketahanan UMKM dengan cara mengikuti rekomendasi berikut:")
    else:
        st.error(f"UMKM Anda **BERESIKO TIDAK BERKELANJUTAN** ⚠️ (Probabilitas: {proba:.3f}) Tingkatkan ketahanan UMKM anda dengan mengikuti rekomendasi berikut:")

    # === Mapping rekomendasi berdasarkan nama fitur ===
    feature_reco = {
        "Q1": "Terapkan pencatatan keuangan menggunakan aplikasi seperti BukuWarung, Majoo, atau Mekari Jurnal untuk memantau pemasukan dan pengeluaran harian/mingguan.",
        "Q2": "Gunakan fitur ‘Cash Flow Management’ dari aplikasi seperti Kledo atau Jurnal.id untuk membuat perencanaan arus kas bulanan dan menjaga stabilitas keuangan usaha.",
        "Q3": "Kurangi ketergantungan pada pinjaman dengan analisis biaya menggunakan Excel/Google Sheets atau aplikasi Finansialku untuk memetakan kebutuhan modal.",
        "Q4": "Gunakan laporan keuangan (L/R, neraca, arus kas) dari aplikasi Jurnal.id atau Kledo sebagai dasar keputusan bisnis seperti pengadaan, harga, atau ekspansi.",
        "Q5": "Optimalkan pemasaran digital melalui Instagram Business, Facebook Page, dan TikTok Shop. Gunakan Canva untuk membuat konten visual yang menarik.",
        "Q6": "Tingkatkan layanan pelanggan dengan menggunakan WhatsApp Business API, fitur auto-reply, atau aplikasi CRM seperti HubSpot untuk mencatat interaksi pelanggan.",
        "Q7": "Gunakan multi-channel melalui marketplace (Shopee, Tokopedia), media sosial, dan toko offline. Integrasikan penjualan via aplikasi seperti Sirclo atau Tokko.",
        "Q8": "Gunakan kalender promosi bulanan dan tools seperti Canva, Meta Ads Manager, atau aplikasi Evermos untuk membuat promo dan campaign penjualan.",
        "Q9": "Ikuti pelatihan di platform seperti Coursera, Skill Academy, atau program pelatihan gratis dari Kemenkop untuk meningkatkan kompetensi pemilik/karyawan.",
        "Q10": "Gunakan survei singkat melalui Google Forms atau Typeform untuk mengetahui kebutuhan pelanggan dan mendukung inovasi produk secara terukur.",
        "Q11": "Pantau tren pasar menggunakan Google Trends, TikTok Creative Center, dan insights media sosial untuk menyesuaikan strategi produk dan pemasaran.",
        "Q12": "Ikut kegiatan sosial atau komunitas lokal melalui program UMKM daerah, Karang Taruna, atau event komunitas di platform Loket.com/Eventbrite.",
        "Q13": "Gunakan konsep produksi ramah lingkungan, daur ulang kemasan, atau aplikasi Waste4Change untuk konsultasi tentang manajemen limbah.",
        "Q14": "Kolaborasi dengan pemasok lokal melalui komunitas UMKM di Facebook, WhatsApp Group UMKM, atau platform seperti Tokopedia Salam Lokal.",
        "Q15": "Bangun kerja sama dengan komunitas seperti UMKM Go Digital, Asosiasi UMKM Indonesia, dan komunitas lokal untuk memperluas jaringan.",
        "Q16": "Gunakan aplikasi digital operasional seperti POS Majoo, Pawoon, atau Olsera untuk pencatatan penjualan, stok, dan transaksi harian.",
        "Q17": "Analisis data historis penjualan menggunakan Google Sheets, Excel, atau dashboard sederhana dari Majoo/Jurnal.id untuk prediksi usaha.",
        "Q18": "Gunakan pembayaran digital QRIS dari bank atau aplikasi seperti OVO, Dana, dan GoPay untuk memudahkan transaksi dan meningkatkan kecepatan layanan.",
        "Q19": "Optimalkan penjualan di marketplace seperti Shopee, Tokopedia, Blibli, atau buat website toko menggunakan Shopify, WooCommerce, atau SIRCLO.",
        "Q20": "Gunakan data pelanggan, tren penjualan, dan laporan digital dari aplikasi POS seperti Majoo atau Olsera sebagai dasar pengambilan keputusan.",
        "Q21": "Konsultasikan bisnis dengan mentor melalui platform MicroMentor Indonesia (gratis), Kemenkop, atau program pendampingan UMKM digital.",
        "Q22": "Susun rencana bisnis menggunakan template Business Model Canvas (Canvanizer.com) atau Google Workspace untuk menyusun rencana strategis.",
        "Q23": "Gunakan metode analisis risiko sederhana dengan Excel atau tools seperti Trello/Notion untuk memetakan risiko keuangan, operasional, dan pemasaran.",
        "Q24": "Siapkan rencana darurat menggunakan dokumen contingency plan yang sederhana di Google Docs atau Notion, serta simpan kontak pemasok alternatif.",
        "Q25": "Gunakan program loyalitas pelanggan dengan aplikasi seperti DealPOS, Pawoon Loyalty, atau gunakan Google Sheets untuk memonitor repeat order.",
        "Q26": "Bangun pelanggan loyal dengan layanan personal, DM marketing via WhatsApp Business, dan sistem membership sederhana melalui aplikasi POS.",
        "Q27": "Kumpulkan ulasan pelanggan melalui Google Review, Shopee Review, atau survei Google Forms. Tingkatkan kualitas produk/layanan berdasarkan feedback tersebut."
    }

        # ============================
    # REKOMENDASI BERBASIS FEATURE IMPORTANCE
    # ============================
    st.subheader("🎯 Rekomendasi Berdasarkan Faktor yang Paling Berpengaruh")

    # Ambil nama kolom yg sama urutannya dengan fitur training
    feature_names = list(input_data.keys())

    # Gabungkan importance + nilai user
    df_imp = pd.DataFrame({
        "feature": feature_names,
        "importance": feature_importances,
        "value": list(input_data.values())
    })

    # Likert = semakin besar semakin buruk (1 bagus, 4 buruk)
    # Pilih fitur paling penting lalu cek yg nilainya buruk (>2)
    df_imp = df_imp.sort_values(by="importance", ascending=False)

    # Ambil hanya fitur perilaku (Q1 - Q27)
    df_imp = df_imp[df_imp["feature"].str.contains("Q")]

    # Fitur buruk dan penting
    df_buruk = df_imp[df_imp["value"] > 2].head(5)

    if df_buruk.empty:
        st.info("🎉 Tidak ada indikator kritis berdasarkan model. Perilaku UMKM Anda cukup baik.")
    else:
        for _, row in df_buruk.iterrows():
            feat = row["feature"]
            reco = feature_reco.get(feat, "Perbaiki indikator ini untuk meningkatkan keberlanjutan.")
            st.write(f"🔸 **{feat}** → {reco} (importance: {row['importance']:.3f})")

    # =============================================
    # SIMPAN DATA KE SUPABASE
    # =============================================
    try:
        save_data = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "gender": gender,
            "age": age,
            "province": province,
            "city": city,
            "name": name,
            "business_name": business_name,
            "nib": nib,
            "phone": phone,
            "address": address,
            "grade": grade,
            "q1": likert[Q1],
            "q2": likert[Q2],
            "q3": likert[Q3],
            "q4": likert[Q4],
            "q5": likert[Q5],
            "q6": likert[Q6],
            "q7": likert[Q7],
            "q8": likert[Q8],
            "q9": likert[Q9],
            "q10": likert[Q10],
            "q11": likert[Q11],
            "q12": likert[Q12],
            "q13": likert[Q13],
            "q14": likert[Q14],
            "q15": likert[Q15],
            "q16": likert[Q16],
            "q17": likert[Q17],
            "q18": likert[Q18],
            "q19": likert[Q19],
            "q20": likert[Q20],
            "q21": likert[Q21],
            "q22": likert[Q22],
            "q23": likert[Q23],
            "q24": likert[Q24],
            "q25": likert[Q25],
            "q26": likert[Q26],
            "q27": likert[Q27],
            "output": pred,
        }

        # tambahkan Q1–Q27
        # for i in range(1, 28):
        #     save_data[f"Q{i}"] = likert[Q[i]]

        response = supabase.table("data_umkm").insert(save_data).execute()

        st.success("✔ Data berhasil disimpan ke Supabase!")

    except Exception as e:
        st.error(f"❌ Gagal menyimpan ke Supabase: {e}")


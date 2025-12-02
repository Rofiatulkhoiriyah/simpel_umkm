import os
from supabase import create_client, Client
from dotenv import load_dotenv

import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import base64

# ============================
# Load ENV
# ============================
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# ============================
# Sidebar Logo
# ============================
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
    page_title="UMKM",
    page_icon="📊",
)

st.title("📊 Data UMKM")

# ============================
# Ambil Data dari Supabase
# ============================

response = supabase.table("data_umkm").select("*").execute()
data = response.data

# Konversi ke DataFrame
df = pd.DataFrame(data)

# Simpan salinan aman
df_processed = df.copy()

# Identifikasi kolom non-numerik
non_numeric_cols = df.select_dtypes(exclude=['number']).columns

# Label encoding untuk kolom non-numerik
le = LabelEncoder()
for col in non_numeric_cols:
    df[col] = le.fit_transform(df[col].astype(str))

# ============================
# Statistik UMKM (Card)
# ============================

st.markdown("""
    <style>
        .stat-card {
            padding: 15px;
            border-radius: 10px;
            background-color: #3A3A3A;
            color: white;
            text-align: center;
            margin-bottom: 15px;
            border: 1px solid #5a5a5a;
        }
        .stat-title {
            font-size: 14px;
            opacity: 0.85;
        }
        .stat-value {
            font-size: 26px;
            font-weight: bold;
            margin-top: 6px;
        }
    </style>
""", unsafe_allow_html=True)

# Perhitungan statistik
total_umkm = len(df)
berlanjut = (df['output'] == 1).sum()
tidak_berlanjut = total_umkm - berlanjut
persen_berlanjut = round((berlanjut / total_umkm) * 100, 2)

df["age"] = pd.to_numeric(df["age"], errors="coerce")
avg_age = round(df["age"].mean(), 1)

# Kolom 1–3
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
        <div class="stat-card">
            <div class="stat-title">Total Data UMKM</div>
            <div class="stat-value">{total_umkm}</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="stat-card">
            <div class="stat-title">UMKM Berlanjut</div>
            <div class="stat-value">{berlanjut}</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="stat-card">
            <div class="stat-title">UMKM Tidak Berlanjut</div>
            <div class="stat-value">{tidak_berlanjut}</div>
        </div>
    """, unsafe_allow_html=True)

# Kolom 4–5
col4, col5 = st.columns(2)

with col4:
    st.markdown(f"""
        <div class="stat-card">
            <div class="stat-title">Rata-rata Usia Pengusaha</div>
            <div class="stat-value">{avg_age}</div>
        </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown(f"""
        <div class="stat-card">
            <div class="stat-title">Persentase Keberlanjutan</div>
            <div class="stat-value">{persen_berlanjut}%</div>
        </div>
    """, unsafe_allow_html=True)

# ============================
# Visualisasi Plot
# ============================

fig1 = px.histogram(df, x="age", title="Distribusi Usia Pengusaha")
fig2 = px.histogram(df, x="age", color="output", barmode="group",
                    title="Distribusi Usia berdasarkan Output (1=Berlanjut, 0=Tidak)")
fig3 = px.scatter(df, x="age", y="grade", color="gender",
                  title="Usia vs. Grade")
fig4 = px.histogram(df, x="city", color="output", barmode="group",
                    title="Distribusi Kota berdasarkan Output (1=Berlanjut, 0=Tidak)")

st.plotly_chart(fig1)
st.plotly_chart(fig2)
st.plotly_chart(fig3)
st.plotly_chart(fig4)

# Statistik tambahan
prov_count = df_processed["city"].value_counts().reset_index()
prov_count.columns = ["Kota", "Jumlah"]

fig_prov = px.bar(prov_count, x="Kota", y="Jumlah",
                  title="Persebaran Data UMKM berdasarkan Kota")
st.plotly_chart(fig_prov)

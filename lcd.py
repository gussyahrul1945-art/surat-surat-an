import streamlit as st
import time

# 1. Konfigurasi Halaman Web
st.set_page_config(page_title="Surat untuk Kamu", page_icon="✉️", layout="centered")

# Mengatur gaya tampilan agar terlihat estetik dan rapi
st.markdown("""
    <style>
    .big-font { font-size:24px !important; font-weight: bold; color: #2c3e50; text-align: center; line-height: 1.6; }
    .highlight { color: #e74c3c; font-size:28px !important; font-weight: bold; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# 2. Isi Surat Berdasarkan Poin-Poinmu
isi_surat = [
    "Hai, aku Roni Parulian...",
    "Kamu pasti jengkel ya denger nama aku di platform itu?",
    "Tapi tenang, aku bukan si Parulian itu kok. 😌",
    "Aku di sini cuma mau ngomong sesuatu...",
    "HAIMIYA IS MY BINI COYYYYYYYYY!!! 💍🤣"
]

# 3. Mengatur Alur Pembacaan Surat (Menggunakan Session State Python)
if 'halaman' not in st.session_state:
    st.session_state.halaman = 0

# Tampilan Judul
st.write("<h3 style='text-align: center;'>📩 Ada Pesan untuk Kamu</h3>", unsafe_allow_html=True)
st.write("---")

# 4. Memunculkan Kalimat Sesuai Tombol yang Ditekan
index = st.session_state.halaman

# Cek apakah sudah sampai di kalimat kejutan terakhir (Poin ke-5)
if index < len(isi_surat) - 1:
    # Memunculkan kalimat saat ini dengan efek mengetik sederhana
    st.write(f"<p class='big-font'>{isi_surat[index]}</p>", unsafe_allow_html=True)
    st.write("")
    
    # Tombol untuk lanjut ke kalimat berikutnya
    if st.button("Lanjut Baca ➡️", use_container_width=True):
        st.session_state.halaman += 1
        st.rerun()
else:
    # EFEK KEJUTAN: Kalimat terakhir muncul dengan balon-balon perayaan!
    st.balloons()
    st.write(f"<p class='highlight'>{isi_surat[index]}</p>", unsafe_allow_html=True)
    st.write("")
    
    # Tombol untuk mengulang baca dari awal
    if st.button("Baca Ulang 🔄", use_container_width=True):
        st.session_state.halaman = 0
        st.rerun()

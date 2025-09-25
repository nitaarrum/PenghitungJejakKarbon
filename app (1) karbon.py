import streamlit as st

# Fungsi perhitungan emisi karbon
def hitung_emisi(jenis_kendaraan, bahan_bakar, jarak):
    # Emisi per liter bahan bakar (kg CO2)
    if bahan_bakar == "bensin":
        emisi_per_liter = 2.31
    elif bahan_bakar == "solar":
        emisi_per_liter = 2.68
    else:
        return None  # bahan bakar tidak dikenali

    # Konsumsi bahan bakar
    if jenis_kendaraan == "motor":
        konsumsi = 40  # km per liter
    elif jenis_kendaraan == "mobil":
        konsumsi = 12  # km per liter
    else:
        return None  # jenis kendaraan tidak dikenali

    liter_digunakan = jarak / konsumsi
    total_emisi = liter_digunakan * emisi_per_liter
    return round(total_emisi, 2)

# --- Streamlit App ---
st.title("🚗 Kalkulator Emisi Karbon Harian")

st.subheader("Masukkan Data Kendaraan")
jenis_kendaraan = st.selectbox("Pilih Jenis Kendaraan:", ["motor", "mobil"])
bahan_bakar = st.selectbox("Pilih Jenis Bahan Bakar:", ["bensin", "solar"])
jarak = st.number_input("Masukkan jarak tempuh harian (km):", min_value=0.0, step=1.0)

if st.button("Hitung Emisi Karbon"):
    emisi = hitung_emisi(jenis_kendaraan, bahan_bakar, jarak)
    if emisi is None:
        st.error("⚠️ Jenis kendaraan atau bahan bakar tidak dikenali.")
    else:
        st.success(f"Total emisi karbon harian: **{emisi} kg CO₂**")

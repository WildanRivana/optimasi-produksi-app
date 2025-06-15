import streamlit as st
from scipy.optimize import linprog
import numpy as np

st.title("Optimasi Produksi Roti")

# Input
terigu = st.number_input("Jumlah Terigu (kg)", value=100.0)
gula = st.number_input("Jumlah Gula (kg)", value=40.0)
tenaga = st.number_input("Tenaga Kerja (jam)", value=180.0)

# Fungsi objektif (max → min)
c = [-4000, -5000]

# Kendala
A = [
    [0.5, 0.7],
    [0.2, 0.3],
    [2, 3]
]
b = [terigu, gula, tenaga]

res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

if res.success:
    x, y = res.x
    st.success(f"Produksi optimal: {x:.0f} roti tawar dan {y:.0f} roti manis")
    st.write(f"Keuntungan maksimal: Rp {(-res.fun):,.0f}")
else:
    st.error("Tidak ditemukan solusi")

import cv2
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# FUNGSI KOREKSI CAHAYA
# ==========================================
def koreksi_gamma(gambar, gamma):
    # Kurva eksponensial untuk menurunkan cahaya secara natural
    tabel = np.array([((i / 255.0) ** gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(gambar, tabel)

# ==========================================
# 1. PANGGIL GAMBAR UTAMA
# ==========================================
path_foto = 'foto_terang.jpg'
gambar_asli = cv2.imread(path_foto)
gambar_asli_rgb = cv2.cvtColor(gambar_asli, cv2.COLOR_BGR2RGB)

# ==========================================
# 2. TERAPKAN 1 METODE (GAMMA 2.0)
# ==========================================
# Gamma 2.0 akan menekan area putih silau agar lebih gelap dan detail keluar
gambar_normal = koreksi_gamma(gambar_asli_rgb, 2.0)

# ==========================================
# 3. TAMPILKAN HASIL (LAYOUT 2 BARIS x 2 KOLOM)
# ==========================================
kumpulan_gambar = [gambar_asli_rgb, gambar_normal]
kumpulan_judul = ["1. Foto Asli (Terang)", "2. Hasil Normal (Gamma 2.0)"]

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

for i in range(2):
    # --- BARIS ATAS: Tampilkan Gambar ---
    axes[0, i].imshow(kumpulan_gambar[i])
    axes[0, i].set_title(kumpulan_judul[i], fontsize=14, fontweight='bold')
    axes[0, i].axis('off')
    
    # --- BARIS BAWAH: Tampilkan Histogram ---
    abu_abu = cv2.cvtColor(kumpulan_gambar[i], cv2.COLOR_RGB2GRAY)
    axes[1, i].hist(abu_abu.ravel(), bins=256, range=[0, 256], color='#1f77b4')
    axes[1, i].set_xlabel("Intensitas (0 Gelap - 255 Terang)")
    axes[1, i].set_ylabel("Jumlah Pixel")
    axes[1, i].set_xlim([0, 256])
    axes[1, i].grid(axis='y', linestyle=':', alpha=0.6)

plt.tight_layout()
plt.show()
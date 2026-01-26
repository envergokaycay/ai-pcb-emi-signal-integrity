import streamlit as st
from ultralytics import YOLO
from PIL import Image

# SAYFA
st.set_page_config(
    page_title="PCB Tasarım Hataları Analizi",
    page_icon="🖥️",
    layout="wide"
)

# HATALAR VE ÇÖZÜMLER
pcb_error_database = {
    "hata_stub": {  
        "gorunen_ad": "Stub Hatası", 
        "kisa_ad": "STUB",
        "renk": "#FF4B4B", 
        "tanim": "Stub, PCB izinin sinyal yolu üzerinde açık uçlu veya gereksiz uzantı bırakacak şekilde sonlanması durumudur.",
        "sorunlar": [
            "🔴 **Sinyal Bütünlüğü:** Yüksek frekansta sinyal yansımasına (reflection) neden olur.",
            "🔴 **EMI Problemleri:** 'Anten' gibi davranarak parazit yayar.",
        ],
        "cozumler": [
            "🛠️ **Bağlama:** Açık uçlu izi ilgili nete, pad veya via üzerinden doğru şekilde bağlayın.",
            "🛠️ **Kaldırma:** İşlevi olmayan ve sinyal yoluna katkı sağlamayan iz uzantılarını tamamen kaldırın.",
            "🛠️ **Yeniden Yönlendirme:** İzi, açık uç bırakmayacak şekilde sinyal akışına uygun olarak yeniden yönlendirin."
        ]
    },
    "hata_90": { 
        "gorunen_ad": "90 Derece Hatası",
        "kisa_ad": "90° KÖŞE",
        "renk": "#FFA500",
        "tanim": "PCB yollarının dönüşlerde keskin 90 derece açı yapması durumudur.",
        "sorunlar": [
            "🟠 **Asit Tuzağı (Acid Trap):** Köşede asit birikerek yolu aşındırır.",
            "🟠 **Empedans:** Köşe genişliği değiştiği için empedans sorunu yaratır.",
        ],
        "cozumler": [
            "🛠️ **45 Derece Kuralı:** Köşeyi silip 45 derecelik (mitered) iki parça halinde tekrar çizin.",
            "🛠️ **Yuvarlatma (Arc):** Eğer yüksek hızlı (High-Speed) sinyal ise köşeyi 'Rounded' (yay) şeklinde tasarlayın.",
        ]
    }
}

# MODEL
@st.cache_resource
def load_model():
    model_path = 'best.pt' 
    try:
        return YOLO(model_path)
    except Exception as e:
        st.error(f"⚠️ Model yüklenirken hata: {e}")
        st.stop()

model = load_model()

# ARAYÜZ
st.title("🖥️ Otomatik PCB Tasarım Hatası Tespiti (AOI)")
st.markdown("---")

col_left, col_right = st.columns([1, 2], gap="medium")

with col_left:
    st.header("1. Görüntü Yükleme")
    uploaded_file = st.file_uploader("Gerber çıktısı veya PCB fotoğrafı seçin", type=['jpg', 'png', 'jpeg'])
    CONFIDENCE_THRESHOLD = 0.45 

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    with st.spinner('Yapay zeka PCB üzerinde tarama yapıyor...'):
        results = model.predict(image, conf=CONFIDENCE_THRESHOLD)
        result = results[0]
        res_plotted = result.plot(conf=False, labels=True, line_width=3, font_size=16)

    with col_right:
        st.header("2. Analiz Sonucu")
        st.image(res_plotted, use_container_width=True)

    # DETAYLI RAPOR VE ÇÖZÜMLER
    st.markdown("---")
    st.header("📊 Detaylı Rapor ve Aksiyon Planı")

    boxes = result.boxes
    if len(boxes) == 0:
        st.success("✅ Hata tespit edilmedi. PCB üretime uygundur.")
    else:
        detected_counts = {}
        detected_types = set()
        
        for box in boxes:
            cls_id = int(box.cls[0])
            raw_name = model.names[cls_id] 
            detected_counts[raw_name] = detected_counts.get(raw_name, 0) + 1
            detected_types.add(raw_name)

        cols_stats = st.columns(len(detected_types))
        for idx, raw_name in enumerate(detected_types):
             info = pcb_error_database.get(raw_name)
             with cols_stats[idx]:
                 if info:
                     st.metric(label=f"Toplam {info['gorunen_ad']}", value=detected_counts[raw_name], delta="Tespit Edildi", delta_color="inverse")

        st.markdown("### 📘 Teknik Açıklamalar ve Çözümler")
        
        for raw_name in detected_types:
            info = pcb_error_database.get(raw_name)
            if info:
                with st.expander(f"🚨 {info['gorunen_ad']} - Analiz Raporu", expanded=True):
                    # 1. Tanım ve Sorunlar
                    c1, c2 = st.columns(2)
                    with c1:
                        st.markdown(f"**Tanım:** {info['tanim']}")
                        st.markdown("**❌ Neden Riskli?**")
                        for sorun in info['sorunlar']:
                            st.markdown(f"- {sorun}")
                            
                    # 2. Çözüm Önerileri
                    with c2:
                        st.markdown("**✅ Nasıl Çözülür? (Aksiyon Planı)**")
                        for cozum in info['cozumler']:
                            st.success(cozum) 
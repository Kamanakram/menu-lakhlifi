import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import datetime
import os
import io

# ============================================================
# 1. إعدادات الصفحة
# ============================================================
st.set_page_config(
    page_title="دار الخليفي | المنيو اليومي",
    page_icon="🍲",
    layout="centered"
)

# ============================================================
# 2. قاعدة البيانات
# ============================================================
if "custom_dishes" not in st.session_state:
    st.session_state.custom_dishes = {
        "الإثنين": [
            {"name": "ربع دجاج معمر بلافيرميسيل + سلطة", "price": "35 درهم", "available": True},
            {"name": "دجاجة معمرة بلافيرميسيل + سلطة", "price": "140 درهم", "available": True},
            {"name": "ربع دجاج بالدغميرة", "price": "35 درهم", "available": True},
            {"name": "دجاجة بالدغميرة", "price": "120 درهم", "available": True},
            {"name": "طاجين اللحم بالبرقوق", "price": "40 درهم", "available": True},
            {"name": "سلطة زعلوك", "price": "10 دراهم", "available": True},
            {"name": "سلطة خيزو مشرمل", "price": "10 دراهم", "available": True}
        ],
        "الثلاثاء": [
            {"name": "سفة مدفونة بالدجاج", "price": "35 درهم", "available": True},
            {"name": "طاجين سردين كواري", "price": "30 درهم", "available": True},
            {"name": "ربع دجاج بالدغميرة", "price": "35 درهم", "available": True},
            {"name": "دجاجة بالدغميرة", "price": "120 درهم", "available": True},
            {"name": "طاجين اللحم بالبرقوق", "price": "40 درهم", "available": True}
        ],
        "الأربعاء": [
            {"name": "طبق بورماش / الرفيسة بالدجاج", "price": "35 درهم", "available": True},
            {"name": "قصعة الرفيسة بالدجاج", "price": "250 درهم", "available": True},
            {"name": "ربع دجاج بالدغميرة", "price": "35 درهم", "available": True}
        ],
        "الخميس": [
            {"name": "ربع دجاج معمر بالمعدنوس + سلطة", "price": "35 درهم", "available": True},
            {"name": "سفة مدفونة بالدجاج", "price": "35 درهم", "available": True},
            {"name": "طاجين سردين كواري", "price": "30 درهم", "available": True},
            {"name": "ربع دجاج بالدغميرة", "price": "35 درهم", "available": True}
        ],
        "الجمعة": [
            {"name": "طبق كسكسو بالدجاج", "price": "35 درهم", "available": True},
            {"name": "طبق كسكسو باللحم", "price": "45 درهم", "available": True},
            {"name": "قصعة كسكسو بالدجاج", "price": "250 درهم", "available": True}
        ],
        "السبت": [
            {"name": "ميني بسطيلة دجاج", "price": "15 درهم", "available": True},
            {"name": "ميني بسطيلة حوت", "price": "20 درهم", "available": True},
            {"name": "بسطيلة دجاج (شخصين)", "price": "99 درهم", "available": True},
            {"name": "بسطيلة حوت (شخصين)", "price": "159 درهم", "available": True}
        ],
        "الأحد": []
    }

# ============================================================
# 3. التاريخ والوقت
# ============================================================
now = datetime.datetime.now()
days_map = ["الإثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة", "السبت", "الأحد"]
today_name = days_map[now.weekday()]
date_text = now.strftime("%Y-%m-%d")
time_text = now.strftime("%H:%M")
PHONE = "0775978088"

# ============================================================
# 4. دالة توليد صورة הـ Story (PNG)
# ============================================================
def create_story_image(day_name, dishes):
    WIDTH, HEIGHT = 1080, 1920
    img = Image.new("RGB", (WIDTH, HEIGHT), "#720000")
    draw = ImageDraw.Draw(img)

    # محاولة تحميل خط عربي أو الخط الافتراضي
    try:
        font_path = "/usr/share/fonts/truetype/noto/NotoSansArabic-Bold.ttf"
        title_font = ImageFont.truetype(font_path, 65)
        sub_font = ImageFont.truetype(font_path, 40)
        item_font = ImageFont.truetype(font_path, 32)
    except:
        title_font = sub_font = item_font = ImageFont.load_default()

    # الإطار الذهبي
    draw.rectangle([30, 30, WIDTH - 30, HEIGHT - 30], outline="#D4AF37", width=8)

    # العنوان
    draw.text((WIDTH//2, 120), "مطعم دار الخليفي 🍲", fill="white", font=title_font, anchor="ms")
    draw.text((WIDTH//2, 200), f"قائمة أطباق يوم {day_name}", fill="#D4AF37", font=sub_font, anchor="ms")
    draw.line([(100, 240), (WIDTH - 100, 240)], fill="#D4AF37", width=3)

    # الأطباق
    y = 300
    for dish in dishes:
        if y > 1600:
            break
        # خلفية بيضاء لكل طبق
        draw.rounded_rectangle([80, y, WIDTH - 80, y + 90], radius=15, fill="white")
        # اسم الطبق والثمن
        draw.text((WIDTH - 120, y + 45), dish["name"], fill="#222222", font=item_font, anchor="rm")
        draw.text((120, y + 45), dish["price"], fill="#720000", font=item_font, anchor="lm")
        y += 110

    # الفوتر
    draw.line([(100, 1720), (WIDTH - 100, 1720)], fill="#D4AF37", width=3)
    draw.text((WIDTH//2, 1780), "📍 مكناس - الزيتون", fill="white", font=sub_font, anchor="ms")
    draw.text((WIDTH//2, 1840), f"📱 للطلب المباشر: {PHONE}", fill="#D4AF37", font=sub_font, anchor="ms")

    return img

# ============================================================
# 5. الواجهة الرئيسية
# ============================================================
st.title("🍲 مطعم دار الخليفي")
st.subheader("مكناس - الزيتون | المنيو اليومي والطلبات")
st.caption(f"📅 اليوم: {today_name} {date_text} | ⏰ الساعة: {time_text}")
st.divider()

# التحكم الجانبي
with st.sidebar:
    st.header("⚙️ لوحة التحكم")
    selected_day = st.selectbox("📅 اختر اليوم:", days_map, index=now.weekday())
    is_closed = st.checkbox("🚨 المطعم مغلق اليوم", value=(selected_day == "الأحد"))
    
    st.divider()
    st.subheader("➕ إضافة طبق جديد")
    new_name = st.text_input("اسم الطبق:")
    new_price = st.text_input("الثمن (مثال: 35 درهم):")
    if st.button("حفظ الطبق", use_container_width=True):
        if new_name and new_price:
            st.session_state.custom_dishes[selected_day].append({"name": new_name, "price": new_price, "available": True})
            st.success("تمت الإضافة بنجاح!")
            st.rerun()

if is_closed:
    st.error(f"🔴 مطعم دار الخليفي مغلق يوم {selected_day}. نلقاكم غداً إن شاء الله!")
else:
    # عرض الأطباق
    st.header(f"🍽️ أطباق يوم {selected_day}")
    dishes = st.session_state.custom_dishes.get(selected_day, [])
    
    if not dishes:
        st.info("لا توجد أطباق مسجلة لهذا اليوم بعد.")
    else:
        for idx, dish in enumerate(dishes):
            col1, col2, col3 = st.columns([4, 2, 1])
            with col1:
                st.write(f"**{dish['name']}**")
            with col2:
                st.write(f"💰 {dish['price']}")
            with col3:
                if st.button("حذف 🗑️", key=f"del_{selected_day}_{idx}"):
                    st.session_state.custom_dishes[selected_day].pop(idx)
                    st.rerun()

    st.divider()

    # أسعار التوصيل
    with st.expander("🛵 أسعار التوصيل (مكناس)"):
        st.write("- **منطقة الزيتون:** 5 دراهم")
        st.write("- **المناطق القريبة:** 10 دراهم")
        st.write("- **حمرية والمناطق المجاورة:** 15 درهم")
        st.write("- **البساتين، البريدية، رياض تولال:** 20 درهم")
        st.write("- **التوصيل السريع VIP:** من 15 إلى 25 درهم")

    # زر الواتساب
    wa_url = f"https://wa.me/212775978088?text=سلام%20دار%20الخليفي،%20بغيت%20نطلب%20من%20المنيو"
    st.link_button("📱 اضغط هنا للطلب المباشر عبر الواتساب (0775978088)", wa_url, use_container_width=True)

    st.divider()

    # قسم الـ Story
    st.header("📱 بطاقة الستوري (WhatsApp & Instagram)")
    st.caption("صورة بمقاس الستوري الرسمي (1080×1920) تتعدل أوتوماتيكياً مع الأطباق:")

    # توليد الصورة
    available_dishes = [d for d in dishes if d.get("available", True)]
    story_img = create_story_image(selected_day, available_dishes)

    # تحويل الصورة لبايت للتحميل
    buf = io.BytesIO()
    story_img.save(buf, format="PNG")
    byte_im = buf.getvalue()

    # عرض الصورة وزر التحميل
    st.image(story_img, width=350)
    st.download_button(
        label="📥 تحميل صورة الـ Story عالية الجودة",
        data=byte_im,
        file_name=f"Story_{selected_day}.png",
        mime="image/png",
        use_container_width=True
    )

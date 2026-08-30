import streamlit as st
import datetime

# إعدادات الصفحة
st.set_page_config(page_title="دار الخليفي - المنيو اليومي", page_icon="🍲", layout="centered")

# تخصيص التصميم بدعم للغة العربية
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    html, body, [class*="css"]  {
        font-family: 'Tajawal', sans-serif;
        direction: rtl;
        text-align: right;
    }
    .main-title {
        color: #8B0000;
        text-align: center;
        font-weight: bold;
        font-size: 32px;
        margin-bottom: 5px;
    }
    .sub-title {
        text-align: center;
        color: #555;
        font-size: 18px;
        margin-bottom: 20px;
    }
    .dish-card {
        background-color: #fdfbf7;
        padding: 15px;
        border-radius: 10px;
        border-right: 5px solid #8B0000;
        margin-bottom: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .delivery-card {
        background-color: #f0f7f4;
        padding: 15px;
        border-radius: 10px;
        border-right: 5px solid #2e7d32;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# العنوان الرئيسي
st.markdown("<div class='main-title'>مطعم دار الخليفي 🍲</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>مكناس - الزيتون | قائمة الطعام والطلبات</div>", unsafe_allow_html=True)

# التحكم فـ الحالة (عطلة أو شغل)
is_closed = st.sidebar.checkbox("🚨 تفعيل وضع العطلة (المطعم مغلق اليوم)")

if is_closed:
    st.error("🔴 سمحوا لينا، مطعم دار الخليفي فـ عطلة اليوم. نلقاكم غداً إن شاء الله!")
else:
    # اختيار اليوم والتاريخ
    days = ["الإثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة", "السبت", "الأحد"]
    now = datetime.datetime.now()
    today_index = now.weekday()  # 0 is Monday
    
    selected_day = st.sidebar.selectbox("اختر اليوم لتحديث المنيو:", days, index=today_index)
    selected_date = st.sidebar.date_input("التاريخ:", now.date())

    st.subheader(f"📅 منيو يوم {selected_day} ({selected_date.strftime('%Y-%m-%d')})")

    # قاعدة بيانات الأطباق حسب الأيام
    default_dishes = {
        "الإثنين": [
            {"name": "ربع دجاج معمر بلافيرميسيل + سلطة", "price": "35 درهم"},
            {"name": "دجاجة معمرة بلافيرميسيل + سلطة", "price": "140 درهم"},
            {"name": "ربع دجاج بالدغميرة", "price": "35 درهم"},
            {"name": "دجاجة بالدغميرة", "price": "120 درهم"},
            {"name": "طاجين اللحم بالبرقوق", "price": "40 درهم"},
            {"name": "طاجين اللحم (سفرجل / ملوخية / بطاطس وزيتون / خرشف)", "price": "40 درهم"},
            {"name": "سلطة زعلوك", "price": "10 دراهم"},
            {"name": "سلطة خيزو مشرمل", "price": "10 دراهم"},
        ],
        "الثلاثاء": [
            {"name": "سفة مدفونة بالدجاج", "price": "35 درهم"},
            {"name": "طاجين سردين كواري", "price": "30 درهم"},
            {"name": "ربع دجاج بالدغميرة", "price": "35 درهم"},
            {"name": "دجاجة بالدغميرة", "price": "120 درهم"},
            {"name": "طاجين اللحم بالبرقوق", "price": "40 درهم"},
            {"name": "سلطة زعلوك", "price": "10 دراهم"},
            {"name": "سلطة خيزو مشرمل", "price": "10 دراهم"},
        ],
        "الأربعاء": [
            {"name": "طبق بورماش / الرفيسة بالدجاج", "price": "35 درهم"},
            {"name": "قصعة الرفيسة بالدجاج", "price": "250 درهم"},
            {"name": "ربع دجاج بالدغميرة", "price": "35 درهم"},
            {"name": "دجاجة بالدغميرة", "price": "120 درهم"},
        ],
        "الخميس": [
            {"name": "ربع دجاج معمر بالمعدنوس + سلطة", "price": "35 درهم"},
            {"name": "دجاجة معمرة بالمعدنوس + سلطة", "price": "140 درهم"},
            {"name": "سفة مدفونة بالدجاج", "price": "35 درهم"},
            {"name": "طاجين سردين كواري", "price": "30 درهم"},
            {"name": "ربع دجاج بالدغميرة", "price": "35 درهم"},
            {"name": "دجاجة بالدغميرة", "price": "120 درهم"},
            {"name": "طاجين اللحم بالبرقوق", "price": "40 درهم"},
            {"name": "سلطة زعلوك", "price": "10 دراهم"},
            {"name": "سلطة خيزو مشرمل", "price": "10 دراهم"},
        ],
        "الجمعة": [
            {"name": "طبق كسكسو بالدجاج", "price": "35 درهم"},
            {"name": "طبق كسكسو باللحم", "price": "45 درهم"},
            {"name": "قصعة كسكسو بالدجاج", "price": "250 درهم"},
            {"name": "ربع دجاج بالدغميرة", "price": "35 درهم"},
            {"name": "دجاجة بالدغميرة", "price": "120 درهم"},
        ],
        "السبت": [
            {"name": "ميني بسطيلة دجاج", "price": "15 درهم"},
            {"name": "ميني بسطيلة حوت", "price": "20 درهم"},
            {"name": "بسطيلة دجاج (شخصين)", "price": "99 درهم"},
            {"name": "بسطيلة حوت (شخصين)", "price": "159 درهم"},
            {"name": "ربع دجاج بالدغميرة", "price": "35 درهم"},
            {"name": "دجاجة بالدغميرة", "price": "120 درهم"},
            {"name": "سلطة زعلوك", "price": "10 دراهم"},
            {"name": "سلطة خيزو مشرمل", "price": "10 دراهم"},
        ],
        "الأحد": [
            {"name": "ربع دجاج بالدغميرة", "price": "35 درهم"},
            {"name": "دجاجة بالدغميرة", "price": "120 درهم"},
            {"name": "طاجين اللحم بالبرقوق", "price": "40 درهم"},
        ]
    }

    # عرض الأطباق مع إمكانية التحكم فـ التوفر
    st.write("### 🍽️ الأطباق المتوفرة اليوم:")
    
    current_dishes = default_dishes.get(selected_day, [])
    
    for idx, dish in enumerate(current_dishes):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"<div class='dish-card'><b>{dish['name']}</b> — <span style='color: #8B0000; font-weight: bold;'>{dish['price']}</span></div>", unsafe_allow_html=True)
        with col2:
            st.checkbox("متوفر", value=True, key=f"dish_{selected_day}_{idx}")

    # معلومات التوصيل
    st.markdown("""
    <div class='delivery-card'>
        <h3>🛵 خدمات التوصيل (حسب الأسبقية)</h3>
        <ul>
            <li><b>الزيتون والمناطق القريبة:</b> 10 دراهم</li>
            <li><b>حمرية والمناطق المجاورة:</b> 15 درهم</li>
            <li><b>البساتين، التلال، البريدية:</b> 20 درهم</li>
            <li><b>التوصيل السريع (المزروبين):</b> مابين 15 و 25 درهم (حسب الموزع)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # زر الطلب المباشر عبر واتساب
    st.write("---")
    whatsapp_number = "212600000000"  # كتحط نمرة الواتساب هنا
    st.markdown(f"""
        <a href="https://wa.me/{whatsapp_number}?text=سلام%20دار%20الخليفي،%20بغيت%20نطلب%20من%20المنيو" target="_blank">
            <button style="background-color: #25D366; color: white; padding: 12px 20px; border: none; border-radius: 8px; font-size: 18px; width: 100%; cursor: pointer;">
                📱 اضغط هنا للطلب عبر الواتساب
            </button>
        </a>
    """, unsafe_allow_html=True)

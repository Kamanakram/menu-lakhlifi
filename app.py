import streamlit as st
import datetime

# إعدادات الصفحة
st.set_page_config(page_title="دار الخليفي | المنيو اليومي", page_icon="🍲", layout="centered")

# CSS الواجهة بالتصميم المغربي الأنيق
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    html, body, [class*="css"] {
        font-family: 'Tajawal', sans-serif;
        direction: rtl;
        text-align: right;
        background-color: #fdfbf7;
    }
    .main-header {
        background: linear-gradient(135deg, #8B0000, #B22222);
        color: white;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    }
    .dish-card {
        background-color: white;
        padding: 12px 15px;
        border-radius: 10px;
        border-right: 5px solid #8B0000;
        margin-bottom: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .delivery-box {
        background-color: #eef7ee;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #c2e0c2;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# قاعدة البيانات الافتراضية
if 'custom_dishes' not in st.session_state:
    st.session_state.custom_dishes = {
        "الإثنين": [
            {"name": "ربع دجاج معمر بلافيرميسيل + سلطة", "price": "35 درهم"},
            {"name": "دجاجة معمرة بلافيرميسيل + سلطة", "price": "140 درهم"},
            {"name": "ربع دجاج بالدغميرة", "price": "35 درهم"},
            {"name": "دجاجة بالدغميرة", "price": "120 درهم"},
            {"name": "طاجين اللحم بالبرقوق", "price": "40 درهم"},
            {"name": "سلطة زعلوك", "price": "10 دراهم"},
            {"name": "سلطة خيزو مشرمل", "price": "10 دراهم"}
        ],
        "الثلاثاء": [
            {"name": "سفة مدفونة بالدجاج", "price": "35 درهم"},
            {"name": "طاجين سردين كواري", "price": "30 درهم"},
            {"name": "ربع دجاج بالدغميرة", "price": "35 درهم"},
            {"name": "دجاجة بالدغميرة", "price": "120 درهم"},
            {"name": "طاجين اللحم بالبرقوق", "price": "40 درهم"}
        ],
        "الأربعاء": [
            {"name": "طبق بورماش / الرفيسة بالدجاج", "price": "35 درهم"},
            {"name": "قصعة الرفيسة بالدجاج", "price": "250 درهم"},
            {"name": "ربع دجاج بالدغميرة", "price": "35 درهم"}
        ],
        "الخميس": [
            {"name": "ربع دجاج معمر بالمعدنوس + سلطة", "price": "35 درهم"},
            {"name": "سفة مدفونة بالدجاج", "price": "35 درهم"},
            {"name": "طاجين سردين كواري", "price": "30 درهم"},
            {"name": "ربع دجاج بالدغميرة", "price": "35 درهم"}
        ],
        "الجمعة": [
            {"name": "طبق كسكسو بالدجاج", "price": "35 درهم"},
            {"name": "طبق كسكسو باللحم", "price": "45 درهم"},
            {"name": "قصعة كسكسو بالدجاج", "price": "250 درهم"}
        ],
        "السبت": [
            {"name": "ميني بسطيلة دجاج", "price": "15 درهم"},
            {"name": "ميني بسطيلة حوت", "price": "20 درهم"},
            {"name": "بسطيلة دجاج (شخصين)", "price": "99 درهم"},
            {"name": "بسطيلة حوت (شخصين)", "price": "159 درهم"}
        ]
    }

# الوقت والتاريخ الحالي
now = datetime.datetime.now()
days_map = ["الإثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة", "السبت", "الأحد"]
today_name = days_map[now.weekday()]
current_time_str = now.strftime("%H:%M")
current_date_str = now.strftime("%Y-%m-%d")

# الهيدر
st.markdown(f"""
    <div class='main-header'>
        <h1>مطعم دار الخليفي 🍲</h1>
        <p style='margin: 0; font-size: 16px;'>مكناس - الزيتون | المنيو اليومي والطلبات</p>
        <small>📅 {today_name} {current_date_str} | ⏰ الساعة {current_time_str}</small>
    </div>
""", unsafe_allow_html=True)

# التحكم الجانبي
st.sidebar.title("⚙️ لوحة التحكم")
selected_day = st.sidebar.selectbox("اختر اليوم للعرض أو التعديل:", days_map, index=now.weekday())

# نمرة الواتساب المباشرة للمطعم
phone_number = "212775978088"

is_sunday = (selected_day == "الأحد")
manual_closed = st.sidebar.checkbox("🚨 تفعيل وضع العطلة للفيوم الحالي", value=is_sunday)

if manual_closed:
    st.error(f"🔴 **مطعم دار الخليفي فـ عطلة يوم {selected_day}. نلقاكم غداً إن شاء الله!**")
else:
    # إضافة طبق جديد
    st.sidebar.markdown("---")
    st.sidebar.subheader("➕ إضافة طبق جديد:")
    new_dish_name = st.sidebar.text_input("اسم الطبق:")
    new_dish_price = st.sidebar.text_input("الثمن (مثال: 40 درهم):")
    
    if st.sidebar.button("حفظ الطبق"):
        if new_dish_name and new_dish_price:
            if selected_day not in st.session_state.custom_dishes:
                st.session_state.custom_dishes[selected_day] = []
            st.session_state.custom_dishes[selected_day].append({"name": new_dish_name, "price": new_dish_price})
            st.sidebar.success("تمت الإضافة بنجاح!")
            st.rerun()

    # عرض الأطباق
    st.subheader(f"🍽️ أطباق يوم {selected_day}:")
    dishes = st.session_state.custom_dishes.get(selected_day, [])

    if not dishes:
        st.info("لا توجد أطباق مسجلة لهذا اليوم بعد. يمكنك إضافتها من القائمة الجانبية.")
    else:
        for idx, dish in enumerate(dishes):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"""
                    <div class='dish-card'>
                        <b>{dish['name']}</b> — <span style='color: #8B0000; font-weight: bold;'>{dish['price']}</span>
                    </div>
                """, unsafe_allow_html=True)
            with col2:
                st.checkbox("متوفر", value=True, key=f"v_{selected_day}_{idx}")
                if st.button("حذف 🗑️", key=f"d_{selected_day}_{idx}"):
                    st.session_state.custom_dishes[selected_day].pop(idx)
                    st.rerun()

    # أسعار التوصيل المعدلة بـ رياض تولال
    st.markdown("""
        <div class='delivery-box'>
            <h4 style='color: #2e7d32; margin: 0;'>🛵 أسعار التوصيل (حسب الأسبقية):</h4>
            <ul style='font-size: 14px; margin-top: 5px; line-height: 1.8;'>
                <li><b>منطقة الزيتون:</b> 5 دراهم</li>
                <li><b>المناطق القريبة من الزيتون:</b> 10 دراهم</li>
                <li><b>حمرية والمناطق المجاورة:</b> 15 درهم</li>
                <li><b>البساتين، البريدية، رياض تولال:</b> 20 درهم</li>
                <li><b>🚀 التوصيل السريع (VIP للمزروبين):</b> ما بين 15 و 25 درهم (حسب الموزع)</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    # زر الواتساب المباشر
    st.write("---")
    st.markdown(f"""
        <a href="https://wa.me/{phone_number}?text=سلام%20دار%20الخليفي،%20بغيت%20نطلب%20من%20المنيو" target="_blank">
            <button style="background-color: #25D366; color: white; padding: 14px; border: none; border-radius: 10px; font-size: 18px; width: 100%; font-weight: bold; cursor: pointer; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                📱 اضغط هنا للطلب المباشر عبر الواتساب (0775978088)
            </button>
        </a>
    """, unsafe_allow_html=True)

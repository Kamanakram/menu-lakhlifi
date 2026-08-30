import streamlit as st
import datetime
import html

# ============================================================
# 1. إعدادات الصفحة
# ============================================================

st.set_page_config(
    page_title="دار الخليفي | المنيو اليومية",
    page_icon="🍲",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# 2. CSS — الواجهة الرئيسية
# ============================================================

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;600;700;800;900&display=swap');

    html, body, [class*="css"] {
        font-family: 'Tajawal', sans-serif !important;
        direction: rtl;
    }

    .stApp {
        background:
            radial-gradient(circle at 0% 0%, rgba(212,175,55,0.09), transparent 25%),
            radial-gradient(circle at 100% 20%, rgba(114,0,0,0.07), transparent 30%),
            #f7f4ee;
    }

    #MainMenu, footer, header { visibility: hidden; }

    .block-container {
        max-width: 1200px !important;
        padding-top: 20px !important;
        padding-bottom: 50px !important;
    }

    /* HERO */
    .hero {
        position: relative;
        overflow: hidden;
        background:
            radial-gradient(circle at 15% 20%, rgba(212,175,55,0.22), transparent 30%),
            linear-gradient(135deg, #260000 0%, #620000 50%, #8f0f0f 100%);
        border-radius: 28px;
        padding: 40px 36px;
        color: white;
        box-shadow: 0 22px 55px rgba(60,0,0,0.25);
        margin-bottom: 26px;
        border: 1px solid rgba(212,175,55,0.35);
    }
    .hero-kicker {
        display: inline-block;
        font-size: 13px;
        letter-spacing: 0.5px;
        opacity: 0.85;
        background: rgba(212,175,55,0.18);
        border: 1px solid rgba(212,175,55,0.4);
        padding: 5px 14px;
        border-radius: 50px;
        margin-bottom: 14px;
        color: #f0d98c;
    }
    .hero-title {
        font-size: 42px;
        line-height: 1.15;
        font-weight: 900;
        margin: 0;
        text-shadow: 0 2px 12px rgba(0,0,0,0.25);
    }
    .hero-subtitle { font-size: 16px; opacity: 0.92; margin-top: 8px; }
    .hero-date {
        display: inline-block;
        margin-top: 18px;
        padding: 9px 20px;
        border-radius: 50px;
        background: rgba(255,255,255,0.12);
        border: 1px solid rgba(255,255,255,0.18);
        font-size: 14px;
        font-weight: 600;
    }

    /* TITLES */
    .section-title { color: #4b0000; font-size: 26px; font-weight: 900; margin-top: 6px; }
    .section-description { color: #8a8377; font-size: 14px; margin-bottom: 18px; }

    /* DISH CARD */
    .dish-card {
        background: white;
        border-radius: 18px;
        padding: 16px 20px;
        margin-bottom: 9px;
        border: 1px solid rgba(80,0,0,0.07);
        box-shadow: 0 6px 22px rgba(0,0,0,0.05);
        transition: transform .15s ease, box-shadow .15s ease;
    }
    .dish-card:hover { transform: translateY(-2px); box-shadow: 0 12px 28px rgba(70,0,0,0.10); }
    .dish-card.unavailable { opacity: 0.5; }
    .dish-name { color: #222; font-size: 16.5px; font-weight: 800; }
    .dish-name.strike { text-decoration: line-through; }
    .dish-price { color: #820000; font-size: 15.5px; font-weight: 900; margin-top: 4px; }
    .unavailable-tag {
        display: inline-block;
        font-size: 11px;
        font-weight: 700;
        color: #9a3d00;
        background: #fdeee0;
        border-radius: 20px;
        padding: 2px 10px;
        margin-right: 8px;
    }

    /* INFO */
    .info-card {
        background: white;
        border-radius: 22px;
        padding: 24px;
        border: 1px solid #ece8df;
        box-shadow: 0 8px 30px rgba(0,0,0,0.045);
    }
    .info-title { color: #470000; font-size: 19px; font-weight: 900; margin-bottom: 12px; }
    .delivery-line {
        padding: 9px 0;
        border-bottom: 1px dashed #e4dfd5;
        font-size: 14px;
        color: #444;
    }
    .delivery-line:last-child { border-bottom: none; }

    /* GEMINI PROMPT SECTION */
    .gemini-header {
        background: linear-gradient(135deg, #260000, #650000);
        color: white;
        border-radius: 22px;
        padding: 24px;
        margin-top: 28px;
        margin-bottom: 16px;
        box-shadow: 0 15px 40px rgba(60,0,0,0.15);
        border: 1px solid rgba(212,175,55,0.3);
    }
    .gemini-title { font-size: 22px; font-weight: 900; }
    .gemini-description { color: #e7ddc9; font-size: 13.5px; margin-top: 6px; }
    .gemini-meta {
        background: white;
        border-radius: 14px;
        padding: 12px 18px;
        border: 1px solid #ece8df;
        font-size: 14px;
        color: #444;
        margin-bottom: 14px;
    }

    /* SIDEBAR */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #250000, #560000 55%, #300000);
    }
    section[data-testid="stSidebar"] * { color: white !important; }
    section[data-testid="stSidebar"] input,
    section[data-testid="stSidebar"] textarea { color: #222 !important; background: white !important; }
    section[data-testid="stSidebar"] [data-baseweb="select"] { background: white !important; }
    section[data-testid="stSidebar"] [data-baseweb="select"] * { color: #222 !important; }
    section[data-testid="stSidebar"] [data-baseweb="tab-list"] { gap: 4px; }

    /* BUTTONS */
    .stButton > button, .stDownloadButton > button {
        min-height: 46px !important;
        border-radius: 13px !important;
        font-family: 'Tajawal', sans-serif !important;
        font-weight: 800 !important;
    }

    @media (max-width: 700px) {
        .block-container { padding: 12px !important; }
        .hero { padding: 28px 20px; border-radius: 22px; }
        .hero-title { font-size: 30px; }
        .hero-subtitle { font-size: 13.5px; }
        .section-title { font-size: 22px; }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# 3. قاعدة البيانات (الأطباق كما هي — لم يتم تغييرها)
# ============================================================

DAYS = ["الإثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة", "السبت", "الأحد"]

if "custom_dishes" not in st.session_state:
    st.session_state.custom_dishes = {
        "الإثنين": [
            {"name": "ربع دجاج معمر بلافيرميسيل + سلطة", "price": "35 درهم", "available": True},
            {"name": "دجاجة معمرة بلافيرميسيل + سلطة", "price": "140 درهم", "available": True},
            {"name": "ربع دجاج بالدغميرة", "price": "35 درهم", "available": True},
            {"name": "دجاجة بالدغميرة", "price": "120 درهم", "available": True},
            {"name": "طاجين اللحم بالبرقوق", "price": "40 درهم", "available": True},
            {"name": "سلطة زعلوك", "price": "10 دراهم", "available": True},
            {"name": "سلطة خيزو مشرمل", "price": "10 دراهم", "available": True},
        ],
        "الثلاثاء": [
            {"name": "سفة مدفونة بالدجاج", "price": "35 درهم", "available": True},
            {"name": "طاجين سردين كواري", "price": "30 درهم", "available": True},
            {"name": "ربع دجاج بالدغميرة", "price": "35 درهم", "available": True},
            {"name": "دجاجة بالدغميرة", "price": "120 درهم", "available": True},
            {"name": "طاجين اللحم بالبرقوق", "price": "40 درهم", "available": True},
        ],
        "الأربعاء": [
            {"name": "طبق بورماش / الرفيسة بالدجاج", "price": "35 درهم", "available": True},
            {"name": "قصعة الرفيسة بالدجاج", "price": "250 درهم", "available": True},
            {"name": "ربع دجاج بالدغميرة", "price": "35 درهم", "available": True},
        ],
        "الخميس": [
            {"name": "ربع دجاج معمر بالمعدنوس + سلطة", "price": "35 درهم", "available": True},
            {"name": "سفة مدفونة بالدجاج", "price": "35 درهم", "available": True},
            {"name": "طاجين سردين كواري", "price": "30 درهم", "available": True},
            {"name": "ربع دجاج بالدغميرة", "price": "35 درهم", "available": True},
        ],
        "الجمعة": [
            {"name": "طبق كسكسو بالدجاج", "price": "35 درهم", "available": True},
            {"name": "طبق كسكسو باللحم", "price": "45 درهم", "available": True},
            {"name": "قصعة كسكسو بالدجاج", "price": "250 درهم", "available": True},
        ],
        "السبت": [
            {"name": "ميني بسطيلة دجاج", "price": "15 درهم", "available": True},
            {"name": "ميني بسطيلة حوت", "price": "20 درهم", "available": True},
            {"name": "بسطيلة دجاج (شخصين)", "price": "99 درهم", "available": True},
            {"name": "بسطيلة حوت (شخصين)", "price": "159 درهم", "available": True},
        ],
        "الأحد": []
    }

if "closed_days" not in st.session_state:
    st.session_state.closed_days = {day: (day == "الأحد") for day in DAYS}

# ============================================================
# 4. التاريخ والوقت
# ============================================================

now = datetime.datetime.now()
weekday_index = now.weekday()  # الإثنين = 0
today_name = DAYS[weekday_index]
date_text = now.strftime("%d/%m/%Y")
time_text = now.strftime("%H:%M")
PHONE = "0775978088"

# ============================================================
# 5. توليد Prompt احترافي لـGemini (بدل توليد الصورة داخل التطبيق)
# ============================================================

def build_gemini_prompt(restaurant_name, location, phone, day_name, dishes):
    """
    يبني Prompt جاهز بالإنجليزية لتصميم بطاقة Story عبر Gemini،
    بناءً على الأطباق المتوفرة فعلياً (available=True) لليوم المختار.
    """

    def format_dish_line(dish):
        return f'- {dish["name"]} — {dish["price"]}'

    common_rules = """For every dish:

- Display the exact Arabic dish name.
- Display the exact price.
- Make the dish name large and clearly readable.
- Make the price visually prominent.
- Maintain excellent spacing between dishes.
- Do not make the text tiny.

The restaurant name must be prominent at the top.

The day must be clearly visible.

The menu must be the main visual focus.

At the bottom, clearly display:

📍 {location}
📱 {phone}

Make the typography elegant, large and highly readable on a smartphone.

Do not overcrowd the design.

Do not make the text extremely small just to fit more dishes.

If there are many dishes, intelligently organize them into a clean multi-column or structured menu layout while keeping every dish readable.

If the number of dishes makes it impossible to maintain good readability in one poster, prioritize readability and create a visually balanced layout rather than shrinking the text excessively.

No unnecessary English text should appear in the final poster.

No fake restaurant logo.

No fake address.

No fake phone number.

No additional dishes.

No invented prices.

No random food names.

No spelling changes.

No distorted Arabic typography.

No blurry text.

No tiny text.

No excessive decorative elements that interfere with readability.

The final result should look like a premium Moroccan restaurant's professionally designed social media poster.

It must be immediately ready to publish as an Instagram Story.""".format(location=location, phone=phone)

    if len(dishes) > 8:
        midpoint = -(-len(dishes) // 2)  # تقسيم متوازن (ceil)
        group_one = dishes[:midpoint]
        group_two = dishes[midpoint:]
        group_one_block = "\n".join(format_dish_line(d) for d in group_one)
        group_two_block = "\n".join(format_dish_line(d) for d in group_two)

        menu_section = f"""If there are too many menu items for one readable Instagram Story, create TWO coordinated Instagram Story posters.

Story 1:
{group_one_block}

Story 2:
{group_two_block}

Both posters must use the same visual identity and design system.

Do not sacrifice readability to fit all dishes into one image."""
    else:
        dishes_block = "\n".join(format_dish_line(d) for d in dishes)
        menu_section = f"""Use exactly the following menu items:

{dishes_block}"""

    prompt = f"""Create a premium traditional Moroccan restaurant Instagram Story poster for "{restaurant_name}".

The design must feel authentic, elegant, warm, traditional Moroccan and premium, inspired by Moroccan gastronomy and Moroccan hospitality.

Restaurant:
{restaurant_name}

Location:
{location}

Phone:
{phone}

Day:
{day_name}

Create a vertical Instagram Story poster in 9:16 format.

The poster must be designed specifically for Instagram Story and WhatsApp Status.

Use a sophisticated Moroccan visual identity:
deep burgundy / dark red, warm cream, subtle gold accents, elegant Moroccan patterns, refined traditional Moroccan decorative elements, subtle zellige-inspired details, premium Moroccan restaurant atmosphere.

The design must look like a professionally designed restaurant menu poster, not like an AI-generated generic poster.

IMPORTANT:
The Arabic text must be extremely clear, readable and correctly written.

Do not invent, modify, translate, shorten or misspell any restaurant information, dish name, price, phone number or location.

{menu_section}

{common_rules}"""

    return prompt

# ============================================================
# 7. Sidebar — لوحة الإدارة
# ============================================================

with st.sidebar:
    st.markdown(
        """
        <div style="text-align:center; padding:8px 0 22px;">
            <div style="font-size:50px;">🍲</div>
            <div style="font-size:25px; font-weight:900;">دار الخليفي</div>
            <div style="font-size:12.5px; opacity:.75; margin-top:4px;">لوحة إدارة المنيو</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    selected_day = st.selectbox("📅 اختار اليوم", DAYS, index=weekday_index)

    is_closed = st.checkbox(
        "🚨 المطعم مغلق هذا اليوم",
        value=st.session_state.closed_days.get(selected_day, False),
        key=f"closed_checkbox_{selected_day}"
    )
    st.session_state.closed_days[selected_day] = is_closed

    st.markdown("---")

    tab_add, tab_edit = st.tabs(["➕ إضافة", "✏️ تعديل / حذف"])

    with tab_add:
        new_dish_name = st.text_input("اسم الطبق", placeholder="مثال: طاجين اللحم...", key="new_dish_name")
        new_dish_price = st.text_input("الثمن", placeholder="مثال: 40 درهم", key="new_dish_price")

        if st.button("➕ إضافة الطبق", use_container_width=True, key="add_dish_btn"):
            if new_dish_name.strip() and new_dish_price.strip():
                st.session_state.custom_dishes[selected_day].append(
                    {"name": new_dish_name.strip(), "price": new_dish_price.strip(), "available": True}
                )
                st.success("تمت إضافة الطبق ✅")
                st.rerun()
            else:
                st.warning("دخل اسم الطبق والثمن.")

    with tab_edit:
        day_dishes = st.session_state.custom_dishes.get(selected_day, [])

        if not day_dishes:
            st.info("لا توجد أطباق مسجلة لهذا اليوم بعد.")
        else:
            options = list(range(len(day_dishes)))
            selected_index = st.selectbox(
                "اختار الطبق",
                options,
                format_func=lambda i: f'{day_dishes[i]["name"]} — {day_dishes[i]["price"]}',
                key=f"edit_select_{selected_day}"
            )

            dish_ref = day_dishes[selected_index]

            edited_name = st.text_input("اسم الطبق", value=dish_ref["name"], key=f"edit_name_{selected_day}_{selected_index}")
            edited_price = st.text_input("الثمن", value=dish_ref["price"], key=f"edit_price_{selected_day}_{selected_index}")
            edited_available = st.checkbox("متوفر", value=dish_ref.get("available", True), key=f"edit_avail_{selected_day}_{selected_index}")

            col_update, col_delete = st.columns(2)

            with col_update:
                if st.button("💾 تحديث", use_container_width=True, key=f"update_btn_{selected_day}_{selected_index}"):
                    if edited_name.strip() and edited_price.strip():
                        dish_ref["name"] = edited_name.strip()
                        dish_ref["price"] = edited_price.strip()
                        dish_ref["available"] = edited_available
                        st.success("تم التحديث ✅")
                        st.rerun()
                    else:
                        st.warning("لا يمكن ترك الاسم أو الثمن فارغاً.")

            with col_delete:
                if st.button("🗑️ حذف", use_container_width=True, key=f"delete_btn_{selected_day}_{selected_index}"):
                    day_dishes.pop(selected_index)
                    st.success("تم الحذف 🗑️")
                    st.rerun()

# ============================================================
# 8. Header
# ============================================================

st.markdown(
    f"""
    <div class="hero">
        <div class="hero-kicker">مطعم مغربي أصيل • مكناس</div>
        <div class="hero-title">مطعم دار الخليفي 🍲</div>
        <div class="hero-subtitle">المنيو اليومية والطلبات</div>
        <div class="hero-date">📅 {today_name} {date_text} &nbsp;•&nbsp; ⏰ {time_text}</div>
    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# 9. حالة الإغلاق
# ============================================================

if st.session_state.closed_days.get(selected_day, False):
    st.error(f"🔴 مطعم دار الخليفي مغلق يوم {selected_day}.\n\nنلقاكم غداً إن شاء الله ❤️")
    st.stop()

# ============================================================
# 10. عرض الأطباق
# ============================================================

all_dishes = st.session_state.custom_dishes.get(selected_day, [])
available_dishes = [d for d in all_dishes if d.get("available", True)]
unavailable_dishes = [d for d in all_dishes if not d.get("available", True)]

st.markdown(
    f"""
    <div class="section-title">🍽️ منيو {selected_day}</div>
    <div class="section-description">{len(available_dishes)} أطباق متوفرة حالياً</div>
    """,
    unsafe_allow_html=True
)

if not all_dishes:
    st.info("🍽️ ما كاين حتى طبق مسجل لهذا اليوم.")
else:
    for dish in available_dishes:
        st.markdown(
            f"""
            <div class="dish-card">
                <div class="dish-name">{html.escape(dish["name"])}</div>
                <div class="dish-price">{html.escape(dish["price"])}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    if unavailable_dishes:
        with st.expander(f"⏸️ أطباق غير متوفرة حالياً ({len(unavailable_dishes)})"):
            for dish in unavailable_dishes:
                st.markdown(
                    f"""
                    <div class="dish-card unavailable">
                        <span class="unavailable-tag">غير متوفر</span>
                        <span class="dish-name strike">{html.escape(dish["name"])}</span>
                        <div class="dish-price">{html.escape(dish["price"])}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

# ============================================================
# 11. التوصيل
# ============================================================

st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    """
    <div class="info-card">
        <div class="info-title">🛵 أسعار التوصيل</div>
        <div class="delivery-line">📍 <b>منطقة الزيتون:</b> 5 دراهم</div>
        <div class="delivery-line">📍 <b>المناطق القريبة من الزيتون:</b> 10 دراهم</div>
        <div class="delivery-line">📍 <b>حمرية والمناطق المجاورة:</b> 15 درهم</div>
        <div class="delivery-line">📍 <b>البساتين، البريدية، رياض تولال:</b> 20 درهم</div>
        <div class="delivery-line">🚀 <b>التوصيل السريع VIP:</b> من 15 إلى 25 درهم</div>
    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# 12. زر WhatsApp للطلب
# ============================================================

st.markdown("<br>", unsafe_allow_html=True)

whatsapp_url = (
    "https://wa.me/212775978088"
    "?text=سلام%20دار%20الخليفي،"
    "%20بغيت%20نطلب%20من%20المنيو%20ديال%20اليوم"
)

st.markdown(
    f"""
    <a href="{whatsapp_url}" target="_blank" style="text-decoration:none;">
        <div style="
            background: linear-gradient(135deg, #128C7E, #25D366);
            color:white; padding:19px; border-radius:18px; text-align:center;
            font-size:19px; font-weight:900;
            box-shadow: 0 12px 30px rgba(37,211,102,.18);
        ">
            📱 اطلب الآن عبر WhatsApp
            <div style="font-size:13px; font-weight:500; margin-top:5px;">0775978088</div>
        </div>
    </a>
    """,
    unsafe_allow_html=True
)

# ============================================================
# 13. تصميم Story عبر Gemini
# ============================================================

st.markdown(
    """
    <div class="gemini-header">
        <div class="gemini-title">🎨 تصميم Story عبر Gemini</div>
        <div class="gemini-description">اختار اليوم، خذ الـPrompt، انسخو في Gemini، وخلي Gemini يصاوب لك الصورة.</div>
    </div>
    """,
    unsafe_allow_html=True
)

if not available_dishes:
    st.warning("ما كايناش أطباق متوفرة اليوم باش نولدو Prompt. فعّل شي طبق أولاً من لوحة التحكم.")
else:
    st.markdown(
        f'<div class="gemini-meta">📅 <b>اليوم:</b> {html.escape(selected_day)} &nbsp;|&nbsp; 🍽️ <b>الأطباق المتوفرة:</b> {len(available_dishes)}</div>',
        unsafe_allow_html=True
    )

    gemini_prompt = build_gemini_prompt(
        restaurant_name="مطعم دار الخليفي",
        location="مكناس - الزيتون",
        phone=PHONE,
        day_name=selected_day,
        dishes=available_dishes
    )

    st.markdown("**📝 Prompt جاهز لـGemini:**")
    st.code(gemini_prompt, language=None)
    st.caption("💡 مرري الماوس فوق المربع واضغطي على أيقونة النسخ في الزاوية لنسخ الـPrompt كاملاً.")

    st.link_button("✨ افتح Gemini", "https://gemini.google.com/app", use_container_width=True)

# ============================================================
# 14. Footer
# ============================================================

st.markdown(
    """
    <div style="text-align:center; color:#999; font-size:13px; margin-top:45px; padding:20px;">
        🍲 مطعم دار الخليفي<br>
        مكناس • الزيتون<br>
        0775978088
    </div>
    """,
    unsafe_allow_html=True
)

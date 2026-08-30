import streamlit as st
import datetime
import io
import base64
import html
from PIL import Image, ImageDraw, ImageFont

# ============================================================
# CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="دار الخليفي | المنيو اليومي",
    page_icon="🍲",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# GLOBAL CSS — MODERN PREMIUM UI
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;600;700;800;900&display=swap');

* {
    font-family: 'Tajawal', sans-serif !important;
}

html, body, [class*="css"] {
    direction: rtl;
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(139,0,0,.05), transparent 25%),
        radial-gradient(circle at 90% 20%, rgba(212,175,55,.06), transparent 25%),
        #f7f4ef;
}

/* Hide Streamlit decoration */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}

/* Main container */
.block-container {
    max-width: 1250px !important;
    padding-top: 2rem !important;
    padding-bottom: 4rem !important;
}

/* ================= HEADER ================= */

.hero {
    position: relative;
    overflow: hidden;
    background:
        linear-gradient(135deg, #450000 0%, #760000 45%, #a51d1d 100%);
    border-radius: 28px;
    padding: 42px 35px;
    color: white;
    box-shadow: 0 20px 50px rgba(69,0,0,.20);
    margin-bottom: 28px;
}

.hero:before {
    content: "";
    position: absolute;
    width: 280px;
    height: 280px;
    border-radius: 50%;
    background: rgba(255,255,255,.05);
    top: -130px;
    left: -80px;
}

.hero:after {
    content: "";
    position: absolute;
    width: 220px;
    height: 220px;
    border-radius: 50%;
    background: rgba(212,175,55,.08);
    bottom: -120px;
    right: -50px;
}

.hero-content {
    position: relative;
    z-index: 2;
}

.hero-title {
    font-size: 42px;
    font-weight: 900;
    margin: 0;
    letter-spacing: -1px;
}

.hero-subtitle {
    margin-top: 8px;
    font-size: 17px;
    opacity: .9;
}

.hero-date {
    display: inline-block;
    margin-top: 22px;
    padding: 8px 16px;
    border-radius: 30px;
    background: rgba(255,255,255,.12);
    border: 1px solid rgba(255,255,255,.16);
    font-size: 14px;
}

/* ================= SECTION TITLES ================= */

.section-title {
    font-size: 25px;
    font-weight: 900;
    color: #450000;
    margin-top: 10px;
    margin-bottom: 18px;
}

.section-subtitle {
    color: #777;
    margin-top: -10px;
    margin-bottom: 20px;
}

/* ================= DISH CARD ================= */

.dish-card {
    background: rgba(255,255,255,.92);
    border: 1px solid rgba(69,0,0,.07);
    border-radius: 18px;
    padding: 18px 20px;
    margin-bottom: 13px;
    box-shadow: 0 7px 25px rgba(0,0,0,.055);
    transition: all .25s ease;
}

.dish-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 30px rgba(69,0,0,.10);
    border-color: rgba(139,0,0,.18);
}

.dish-name {
    font-size: 17px;
    font-weight: 800;
    color: #222;
}

.dish-price {
    color: #8b0000;
    font-size: 16px;
    font-weight: 900;
    margin-top: 5px;
}

/* ================= INFO BOX ================= */

.info-card {
    background: white;
    border-radius: 20px;
    padding: 22px;
    border: 1px solid #eee;
    box-shadow: 0 8px 30px rgba(0,0,0,.05);
}

.delivery-card {
    background: linear-gradient(135deg, #f0f9f1, #ffffff);
    border: 1px solid #cce7ce;
    border-radius: 20px;
    padding: 25px;
    box-shadow: 0 8px 30px rgba(0,0,0,.04);
}

.delivery-title {
    color: #237b2d;
    font-weight: 900;
    font-size: 19px;
    margin-bottom: 12px;
}

.delivery-line {
    padding: 8px 0;
    border-bottom: 1px dashed #d9e6d9;
    color: #333;
}

.delivery-line:last-child {
    border-bottom: none;
}

/* ================= STORY AREA ================= */

.story-container {
    background: #181818;
    border-radius: 25px;
    padding: 25px;
    box-shadow: 0 20px 50px rgba(0,0,0,.15);
    margin-top: 20px;
}

.story-title {
    color: white;
    font-size: 23px;
    font-weight: 900;
    margin-bottom: 4px;
}

.story-description {
    color: #aaa;
    font-size: 14px;
}

/* ================= SIDEBAR ================= */

section[data-testid="stSidebar"] {
    background:
        linear-gradient(180deg, #300000 0%, #500000 55%, #370000 100%);
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

section[data-testid="stSidebar"] input {
    color: #222 !important;
    background: white !important;
}

section[data-testid="stSidebar"] textarea {
    color: #222 !important;
    background: white !important;
}

section[data-testid="stSidebar"] [data-baseweb="select"] {
    background: white !important;
}

section[data-testid="stSidebar"] [data-baseweb="select"] * {
    color: #222 !important;
}

/* ================= BUTTONS ================= */

.stButton > button {
    border-radius: 12px !important;
    font-weight: 800 !important;
    min-height: 45px !important;
    border: none !important;
    transition: .2s ease !important;
}

.stButton > button:hover {
    transform: translateY(-2px);
}

/* ================= FOOTER ================= */

.footer {
    margin-top: 50px;
    padding: 25px;
    text-align: center;
    color: #888;
    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# DEFAULT DATABASE
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
# DATE
# ============================================================

now = datetime.datetime.now()

days_map = [
    "الإثنين",
    "الثلاثاء",
    "الأربعاء",
    "الخميس",
    "الجمعة",
    "السبت",
    "الأحد"
]

today_name = days_map[now.weekday()]
current_time = now.strftime("%H:%M")
current_date = now.strftime("%d/%m/%Y")

# ============================================================
# SETTINGS
# ============================================================

phone_number = "212775978088"
app_url = "https://menu-lakhlifi-iptwnqbcfs3nbergvdqshg.streamlit.app"

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown("""
<div style="
text-align:center;
padding:15px 0 25px 0;
">
<div style="font-size:42px;">🍲</div>
<div style="font-size:23px;font-weight:900;">دار الخليفي</div>
<div style="font-size:13px;opacity:.75;">لوحة إدارة المنيو</div>
</div>
""", unsafe_allow_html=True)

selected_day = st.sidebar.selectbox(
    "📅 اختر اليوم",
    days_map,
    index=now.weekday()
)

st.sidebar.markdown("---")

manual_closed = st.sidebar.checkbox(
    "🚨 إغلاق المطعم لهذا اليوم",
    value=(selected_day == "الأحد")
)

# ============================================================
# HEADER
# ============================================================

st.markdown(f"""
<div class="hero">
    <div class="hero-content">
        <div style="font-size:14px;opacity:.75;margin-bottom:7px;">
            مطعم مغربي أصيل • مكناس
        </div>

        <div class="hero-title">
            دار الخليفي 🍲
        </div>

        <div class="hero-subtitle">
            المنيو اليومي • الطلبات • المشاركة في الستوري
        </div>

        <div class="hero-date">
            📅 {today_name} {current_date}
            &nbsp;&nbsp;•&nbsp;&nbsp;
            ⏰ {current_time}
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# CLOSED
# ============================================================

if manual_closed:

    st.error(
        f"🔴 مطعم دار الخليفي في عطلة يوم {selected_day}. "
        "نلقاكم غداً إن شاء الله ❤️"
    )

else:

    # ========================================================
    # ADD DISH
    # ========================================================

    with st.sidebar:

        st.markdown("---")
        st.markdown("### ➕ إضافة طبق")

        new_name = st.text_input(
            "اسم الطبق",
            placeholder="مثال: طاجين اللحم..."
        )

        new_price = st.text_input(
            "الثمن",
            placeholder="مثال: 40 درهم"
        )

        if st.button(
            "➕ إضافة الطبق",
            use_container_width=True
        ):

            if new_name.strip() and new_price.strip():

                if selected_day not in st.session_state.custom_dishes:
                    st.session_state.custom_dishes[selected_day] = []

                st.session_state.custom_dishes[selected_day].append({
                    "name": new_name.strip(),
                    "price": new_price.strip(),
                    "available": True
                })

                st.success("تمت إضافة الطبق ✅")
                st.rerun()

            else:
                st.warning("دخل اسم الطبق والثمن.")

    # ========================================================
    # DISHES
    # ========================================================

    dishes = st.session_state.custom_dishes.get(
        selected_day,
        []
    )

    st.markdown(
        f"""
        <div class="section-title">
            🍽️ منيو {selected_day}
        </div>

        <div class="section-subtitle">
            {len(dishes)} طبق مسجل • يمكنك إظهار أو إخفاء أي طبق
        </div>
        """,
        unsafe_allow_html=True
    )

    if not dishes:

        st.info("🍽️ لا توجد أطباق مسجلة لهذا اليوم.")

    else:

        for idx, dish in enumerate(dishes):

            col1, col2, col3 = st.columns(
                [6, 2, 1],
                vertical_alignment="center"
            )

            with col1:

                safe_name = html.escape(dish["name"])
                safe_price = html.escape(dish["price"])

                st.markdown(
                    f"""
                    <div class="dish-card">
                        <div class="dish-name">
                            {safe_name}
                        </div>
                        <div class="dish-price">
                            {safe_price}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col2:

                available = st.checkbox(
                    "متوفر",
                    value=dish.get("available", True),
                    key=f"available_{selected_day}_{idx}"
                )

                st.session_state.custom_dishes[
                    selected_day
                ][idx]["available"] = available

            with col3:

                if st.button(
                    "🗑️",
                    key=f"delete_{selected_day}_{idx}"
                ):

                    st.session_state.custom_dishes[
                        selected_day
                    ].pop(idx)

                    st.rerun()

    # ========================================================
    # DELIVERY
    # ========================================================

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="delivery-card">

        <div class="delivery-title">
            🛵 أسعار التوصيل
        </div>

        <div class="delivery-line">
            📍 <b>منطقة الزيتون:</b> 5 دراهم
        </div>

        <div class="delivery-line">
            📍 <b>المناطق القريبة من الزيتون:</b> 10 دراهم
        </div>

        <div class="delivery-line">
            📍 <b>حمرية والمناطق المجاورة:</b> 15 درهم
        </div>

        <div class="delivery-line">
            📍 <b>البساتين، البريدية، رياض تولال:</b> 20 درهم
        </div>

        <div class="delivery-line">
            🚀 <b>التوصيل السريع VIP:</b> من 15 إلى 25 درهم
        </div>

    </div>
    """, unsafe_allow_html=True)

    # ========================================================
    # WHATSAPP ORDER
    # ========================================================

    st.markdown("<br>", unsafe_allow_html=True)

    whatsapp_url = (
        f"https://wa.me/{phone_number}"
        "?text=سلام%20دار%20الخليفي،%20بغيت%20نطلب%20من%20المنيو%20ديال%20اليوم"
    )

    st.markdown(
        f"""
        <a href="{whatsapp_url}" target="_blank" style="text-decoration:none;">
            <div style="
                background:linear-gradient(135deg,#128C7E,#25D366);
                color:white;
                padding:18px;
                border-radius:18px;
                text-align:center;
                font-size:18px;
                font-weight:900;
                box-shadow:0 10px 30px rgba(37,211,102,.20);
            ">
                📱 اطلب دابا عبر WhatsApp
                <div style="font-size:13px;font-weight:500;margin-top:4px;">
                    0775978088
                </div>
            </div>
        </a>
        """,
        unsafe_allow_html=True
    )

    # ========================================================
    # STORY GENERATOR
    # ========================================================

    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="story-container">

        <div class="story-title">
            📱 Story Maker
        </div>

        <div class="story-description">
            الكارت كتتحدث أوتوماتيكياً حسب المنيو الحالية
            • Format 1080 × 1920
        </div>

    </div>
    """, unsafe_allow_html=True)

    # ========================================================
    # STORY HTML
    # ========================================================

    available_dishes = [
        d for d in dishes
        if d.get("available", True)
    ]

    story_items = ""

    for d in available_dishes:

        story_items += f"""
        <div style="
            background:rgba(255,255,255,.96);
            border-radius:22px;
            padding:18px 20px;
            margin-bottom:13px;
            display:flex;
            justify-content:space-between;
            align-items:center;
            gap:15px;
            box-shadow:0 8px 25px rgba(0,0,0,.16);
        ">

            <div style="
                color:#222;
                font-size:27px;
                font-weight:800;
                flex:1;
                line-height:1.35;
            ">
                {html.escape(d["name"])}
            </div>

            <div style="
                background:#8B0000;
                color:#fff;
                padding:9px 15px;
                border-radius:14px;
                font-size:24px;
                font-weight:900;
                white-space:nowrap;
            ">
                {html.escape(d["price"])}
            </div>

        </div>
        """

    if not story_items:

        story_items = """
        <div style="
            background:white;
            color:#555;
            padding:30px;
            border-radius:20px;
            text-align:center;
            font-size:25px;
        ">
            لا توجد أطباق متوفرة اليوم
        </div>
        """

    story_html = f"""
    <html dir="rtl">

    <head>

    <meta name="viewport"
          content="width=device-width,
                   initial-scale=1.0">

    <link href="
    https://fonts.googleapis.com/css2?family=Tajawal:wght@500;700;800;900
    &display=swap"
    rel="stylesheet">

    <style>

    * {{
        box-sizing:border-box;
    }}

    body {{
        margin:0;
        padding:20px;
        background:#111;
        font-family:'Tajawal',sans-serif;
    }}

    .story {{
        width:100%;
        max-width:540px;
        aspect-ratio:9 / 16;
        margin:auto;

        padding:38px 30px;

        border-radius:32px;

        background:
        radial-gradient(circle at 15% 10%,
            rgba(212,175,55,.25),
            transparent 20%),

        radial-gradient(circle at 90% 85%,
            rgba(255,255,255,.08),
            transparent 25%),

        linear-gradient(
            160deg,
            #3c0000 0%,
            #730000 45%,
            #9d1616 100%
        );

        border:3px solid #d4af37;

        box-shadow:
            0 25px 60px rgba(0,0,0,.5);

        overflow:hidden;
    }}

    .brand {{
        text-align:center;
        color:white;
        font-size:38px;
        font-weight:900;
    }}

    .location {{
        text-align:center;
        color:#e7ca72;
        font-size:20px;
        margin-top:5px;
    }}

    .line {{
        height:2px;
        background:#d4af37;
        opacity:.6;
        margin:25px 0;
    }}

    .day {{
        color:white;
        text-align:center;
        font-size:30px;
        font-weight:900;
        margin-bottom:25px;
    }}

    .footer {{
        color:white;
        text-align:center;
        margin-top:25px;
        font-size:20px;
        line-height:1.7;
    }}

    .phone {{
        display:inline-block;
        background:#25D366;
        padding:9px 18px;
        border-radius:30px;
        margin-top:8px;
        font-weight:900;
    }}

    </style>

    </head>

    <body>

        <div class="story">

            <div class="brand">
                دار الخليفي 🍲
            </div>

            <div class="location">
                مكناس • الزيتون
            </div>

            <div class="line"></div>

            <div class="day">
                منيو {selected_day}
            </div>

            {story_items}

            <div class="footer">

                🍽️ مرحباً بكم

                <br>

                📱 للطلب عبر WhatsApp

                <br>

                <span class="phone">
                    0775978088
                </span>

            </div>

        </div>

    </body>
    </html>
    """

    # ========================================================
    # PREVIEW
    # ========================================================

    st.components.v1.html(
        story_html,
        height=900,
        scrolling=True
    )

    # ========================================================
    # STORY IMAGE — 1080 x 1920
    # ========================================================

    def get_font(size, bold=False):

        paths = [
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
            if bold
            else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",

            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
        ]

        for path in paths:
            try:
                return ImageFont.truetype(path, size)
            except:
                pass

        return ImageFont.load_default()


    def create_story_image():

        W, H = 1080, 1920

        img = Image.new(
            "RGB",
            (W, H),
            "#550000"
        )

        draw = ImageDraw.Draw(img)

        # Background gradient
        for y in range(H):

            ratio = y / H

            r = int(65 + ratio * 65)
            g = int(0 + ratio * 15)
            b = int(0 + ratio * 15)

            draw.line(
                [(0, y), (W, y)],
                fill=(r, g, b)
            )

        # Gold border
        draw.rounded_rectangle(
            (20, 20, W-20, H-20),
            radius=45,
            outline="#D4AF37",
            width=7
        )

        title_font = get_font(66, True)
        subtitle_font = get_font(34, True)
        day_font = get_font(48, True)
        item_font = get_font(31, True)
        price_font = get_font(28, True)
        footer_font = get_font(30, True)

        # Title
        draw.text(
            (W//2, 110),
            "مطعم دار الخليفي",
            font=title_font,
            fill="white",
            anchor="ma"
        )

        draw.text(
            (W//2, 190),
            "مكناس • الزيتون",
            font=subtitle_font,
            fill="#E7CA72",
            anchor="ma"
        )

        draw.line(
            (100, 255, W-100, 255),
            fill="#D4AF37",
            width=3
        )

        draw.text(
            (W//2, 320),
            f"منيو {selected_day}",
            font=day_font,
            fill="white",
            anchor="ma"
        )

        y = 410

        max_items = 8

        visible = available_dishes[:max_items]

        for d in visible:

            box_h = 125

            draw.rounded_rectangle(
                (70, y, W-70, y+box_h),
                radius=22,
                fill="white"
            )

            name = d["name"]

            if len(name) > 32:
                name = name[:31] + "…"

            draw.text(
                (W-100, y+box_h//2),
                name,
                font=item_font,
                fill="#222222",
                anchor="rm"
            )

            price_text = d["price"]

            draw.rounded_rectangle(
                (90, y+25, 270, y+100),
                radius=18,
                fill="#8B0000"
            )

            draw.text(
                (180, y+62),
                price_text,
                font=price_font,
                fill="white",
                anchor="mm"
            )

            y += 145

        # Footer
        draw.line(
            (100, H-300, W-100, H-300),
            fill="#D4AF37",
            width=3
        )

        draw.text(
            (W//2, H-245),
            "🍽️ مرحباً بكم",
            font=footer_font,
            fill="white",
            anchor="ma"
        )

        draw.text(
            (W//2, H-190),
            "📱 للطلب: 0775978088",
            font=footer_font,
            fill="white",
            anchor="ma"
        )

        draw.text(
            (W//2, H-110),
            "دار الخليفي • مكناس",
            font=get_font(24, True),
            fill="#E7CA72",
            anchor="ma"
        )

        output = io.BytesIO()

        img.save(
            output,
            format="PNG",
            optimize=True
        )

        output.seek(0)

        return output


    story_image = create_story_image()

    # ========================================================
    # SHARE / DOWNLOAD
    # ========================================================

    st.markdown("""
    <div style="
        background:white;
        padding:22px;
        border-radius:20px;
        margin-top:25px;
        border:1px solid #eee;
    ">

        <div style="
            font-size:21px;
            font-weight:900;
            color:#450000;
        ">
            📲 مشاركة الـStory
        </div>

        <div style="
            color:#777;
            font-size:14px;
            margin-top:5px;
            line-height:1.7;
        ">
            الصورة جاهزة بحجم 1080×1920.
            اضغط على مشاركة الصورة من الهاتف لاختيار
            WhatsApp أو Instagram أو أي تطبيق يدعم مشاركة الصور.
        </div>

    </div>
    """, unsafe_allow_html=True)

    share_col1, share_col2 = st.columns(2)

    with share_col1:

        st.download_button(
            label="⬇️ تحميل صورة Story",
            data=story_image,
            file_name=f"dar_lakhlifi_{selected_day}.png",
            mime="image/png",
            use_container_width=True
        )

    with share_col2:

        # Rewind BytesIO for base64
        story_image.seek(0)

        image_b64 = base64.b64encode(
            story_image.read()
        ).decode()

        share_html = f"""
        <button
            onclick="shareStory()"
            style="
                width:100%;
                min-height:45px;
                border:none;
                border-radius:12px;
                background:linear-gradient(135deg,#8B0000,#B22222);
                color:white;
                font-family:Tajawal,sans-serif;
                font-size:16px;
                font-weight:900;
                cursor:pointer;
            "
        >
            📲 مشاركة الصورة
        </button>

        <script>

        async function shareStory() {{

            try {{

                const base64 = "{image_b64}";

                const binary = atob(base64);

                const bytes = new Uint8Array(binary.length);

                for (let i = 0; i < binary.length; i++) {{
                    bytes[i] = binary.charCodeAt(i);
                }}

                const blob = new Blob(
                    [bytes],
                    {{type:"image/png"}}
                );

                const file = new File(
                    [blob],
                    "dar_lakhlifi_{selected_day}.png",
                    {{type:"image/png"}}
                );

                if (
                    navigator.share &&
                    navigator.canShare &&
                    navigator.canShare({{files:[file]}})
                ) {{

                    await navigator.share({{
                        title:"منيو دار الخليفي",
                        text:"منيو اليوم من مطعم دار الخليفي 🍲",
                        files:[file]
                    }});

                }} else {{

                    alert(
                        "الهاتف أو المتصفح لا يدعم المشاركة المباشرة للصورة. استعمل زر تحميل الصورة."
                    );

                }}

            }} catch(error) {{

                console.log(error);

            }}

        }}

        </script>
        """

        st.components.v1.html(
            share_html,
            height=60
        )

    # ========================================================
    # IMPORTANT NOTE
    # ========================================================

    st.info(
        "💡 من الهاتف: الأفضل تستعمل زر «مشاركة الصورة». "
        "غادي يعطيك Share Sheet ديال الهاتف، ومن تما تختار التطبيق اللي بغيتي. "
        "زر التحميل كيبقى حل مضمون إذا المتصفح منع المشاركة المباشرة."
    )

# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">
    🍲 مطعم دار الخليفي — مكناس، الزيتون
    <br>
    © 2026 جميع الحقوق محفوظة
</div>
""", unsafe_allow_html=True)

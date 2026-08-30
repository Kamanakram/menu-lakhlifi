import streamlit as st
import datetime
import json
import html
import base64
import urllib.parse

# =========================================================
# إعداد الصفحة
# =========================================================

st.set_page_config(
    page_title="دار الخليفي | المنيو",
    page_icon="🍲",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CSS — DESIGN MODERN / PREMIUM
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;600;700;800;900&display=swap');

:root {
    --red: #720000;
    --dark-red: #3d0000;
    --gold: #d4af37;
    --cream: #f8f5ef;
    --white: #ffffff;
    --text: #202020;
    --muted: #777777;
}

html,
body,
[class*="css"] {
    font-family: 'Tajawal', sans-serif !important;
    direction: rtl;
}

.stApp {
    background:
        radial-gradient(
            circle at 0% 0%,
            rgba(212,175,55,0.08),
            transparent 28%
        ),
        radial-gradient(
            circle at 100% 20%,
            rgba(114,0,0,0.06),
            transparent 30%
        ),
        #f8f5ef;
}

/* إخفاء أشياء Streamlit غير الضرورية */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}

/* الحاوية */

.block-container {
    max-width: 1250px !important;
    padding-top: 25px !important;
    padding-bottom: 50px !important;
}

/* =========================================================
   HERO
   ========================================================= */

.hero {
    position: relative;
    overflow: hidden;

    background:
        radial-gradient(
            circle at 15% 20%,
            rgba(212,175,55,0.18),
            transparent 25%
        ),
        linear-gradient(
            135deg,
            #300000 0%,
            #650000 48%,
            #930e0e 100%
        );

    border-radius: 30px;
    padding: 42px 38px;
    color: white;

    box-shadow:
        0 20px 55px rgba(60,0,0,0.20);

    margin-bottom: 28px;
}

.hero::before {
    content: "";
    position: absolute;

    width: 300px;
    height: 300px;

    border: 1px solid rgba(212,175,55,0.20);
    border-radius: 50%;

    top: -180px;
    left: -100px;
}

.hero::after {
    content: "";
    position: absolute;

    width: 250px;
    height: 250px;

    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 50%;

    bottom: -170px;
    right: -80px;
}

.hero-content {
    position: relative;
    z-index: 5;
}

.hero-small {
    font-size: 14px;
    opacity: 0.72;
    margin-bottom: 8px;
}

.hero-title {
    font-size: 44px;
    line-height: 1.15;
    font-weight: 900;
    margin: 0;
}

.hero-subtitle {
    font-size: 17px;
    opacity: 0.9;
    margin-top: 10px;
}

.hero-date {
    display: inline-block;

    margin-top: 22px;

    padding: 9px 17px;

    border-radius: 50px;

    background: rgba(255,255,255,0.10);
    border: 1px solid rgba(255,255,255,0.15);

    font-size: 14px;
}

/* =========================================================
   SECTION
   ========================================================= */

.section-title {
    color: #470000;
    font-size: 26px;
    font-weight: 900;
    margin-top: 10px;
}

.section-subtitle {
    color: #888;
    font-size: 14px;
    margin-bottom: 22px;
}

/* =========================================================
   DISH
   ========================================================= */

.dish {
    background: rgba(255,255,255,0.95);

    border: 1px solid rgba(80,0,0,0.07);

    border-radius: 20px;

    padding: 17px 20px;

    margin-bottom: 12px;

    box-shadow:
        0 7px 25px rgba(0,0,0,0.045);

    transition:
        transform .2s ease,
        box-shadow .2s ease;
}

.dish:hover {
    transform: translateY(-2px);

    box-shadow:
        0 12px 30px rgba(70,0,0,0.09);
}

.dish-name {
    font-size: 17px;
    font-weight: 800;
    color: #202020;
}

.dish-price {
    margin-top: 5px;

    color: #820000;

    font-size: 16px;

    font-weight: 900;
}

/* =========================================================
   INFO CARDS
   ========================================================= */

.info-card {
    background: white;

    border-radius: 22px;

    padding: 24px;

    border: 1px solid #ece8df;

    box-shadow:
        0 8px 30px rgba(0,0,0,0.045);
}

.info-title {
    color: #470000;

    font-size: 20px;

    font-weight: 900;

    margin-bottom: 14px;
}

.delivery-line {
    padding: 10px 0;

    border-bottom: 1px dashed #e5e1d8;

    font-size: 14px;

    color: #444;
}

.delivery-line:last-child {
    border-bottom: none;
}

/* =========================================================
   STORY SECTION
   ========================================================= */

.story-box {
    background:
        linear-gradient(
            145deg,
            #190000,
            #360000
        );

    border-radius: 28px;

    padding: 28px;

    margin-top: 30px;

    box-shadow:
        0 20px 50px rgba(0,0,0,0.18);
}

.story-heading {
    color: white;

    font-size: 25px;

    font-weight: 900;
}

.story-desc {
    color: #cfcfcf;

    font-size: 14px;

    margin-top: 5px;
}

/* =========================================================
   SIDEBAR
   ========================================================= */

section[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #280000,
            #550000 55%,
            #320000
        );
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

section[data-testid="stSidebar"] input {
    color: #222 !important;
    background: white !important;
}

section[data-testid="stSidebar"] [data-baseweb="select"] {
    background: white !important;
}

section[data-testid="stSidebar"] [data-baseweb="select"] * {
    color: #222 !important;
}

/* =========================================================
   BUTTONS
   ========================================================= */

.stButton > button,
.stDownloadButton > button {
    border-radius: 13px !important;

    min-height: 46px !important;

    font-family:
        'Tajawal',
        sans-serif !important;

    font-weight: 800 !important;

    transition:
        transform .18s ease,
        box-shadow .18s ease !important;
}

.stButton > button:hover,
.stDownloadButton > button:hover {
    transform: translateY(-2px) !important;
}

/* =========================================================
   MOBILE
   ========================================================= */

@media (max-width: 700px) {

    .block-container {
        padding: 15px !important;
    }

    .hero {
        padding: 30px 23px;
        border-radius: 24px;
    }

    .hero-title {
        font-size: 32px;
    }

    .hero-subtitle {
        font-size: 14px;
    }

    .story-box {
        padding: 18px;
        border-radius: 22px;
    }

}

</style>
""", unsafe_allow_html=True)


# =========================================================
# البيانات
# =========================================================

if "custom_dishes" not in st.session_state:

    st.session_state.custom_dishes = {

        "الإثنين": [
            {
                "name": "ربع دجاج معمر بلافيرميسيل + سلطة",
                "price": "35 درهم",
                "available": True
            },
            {
                "name": "دجاجة معمرة بلافيرميسيل + سلطة",
                "price": "140 درهم",
                "available": True
            },
            {
                "name": "ربع دجاج بالدغميرة",
                "price": "35 درهم",
                "available": True
            },
            {
                "name": "دجاجة بالدغميرة",
                "price": "120 درهم",
                "available": True
            },
            {
                "name": "طاجين اللحم بالبرقوق",
                "price": "40 درهم",
                "available": True
            },
            {
                "name": "سلطة زعلوك",
                "price": "10 دراهم",
                "available": True
            },
            {
                "name": "سلطة خيزو مشرمل",
                "price": "10 دراهم",
                "available": True
            }
        ],

        "الثلاثاء": [
            {
                "name": "سفة مدفونة بالدجاج",
                "price": "35 درهم",
                "available": True
            },
            {
                "name": "طاجين سردين كواري",
                "price": "30 درهم",
                "available": True
            },
            {
                "name": "ربع دجاج بالدغميرة",
                "price": "35 درهم",
                "available": True
            },
            {
                "name": "دجاجة بالدغميرة",
                "price": "120 درهم",
                "available": True
            },
            {
                "name": "طاجين اللحم بالبرقوق",
                "price": "40 درهم",
                "available": True
            }
        ],

        "الأربعاء": [
            {
                "name": "طبق بورماش / الرفيسة بالدجاج",
                "price": "35 درهم",
                "available": True
            },
            {
                "name": "قصعة الرفيسة بالدجاج",
                "price": "250 درهم",
                "available": True
            },
            {
                "name": "ربع دجاج بالدغميرة",
                "price": "35 درهم",
                "available": True
            }
        ],

        "الخميس": [
            {
                "name": "ربع دجاج معمر بالمعدنوس + سلطة",
                "price": "35 درهم",
                "available": True
            },
            {
                "name": "سفة مدفونة بالدجاج",
                "price": "35 درهم",
                "available": True
            },
            {
                "name": "طاجين سردين كواري",
                "price": "30 درهم",
                "available": True
            },
            {
                "name": "ربع دجاج بالدغميرة",
                "price": "35 درهم",
                "available": True
            }
        ],

        "الجمعة": [
            {
                "name": "طبق كسكسو بالدجاج",
                "price": "35 درهم",
                "available": True
            },
            {
                "name": "طبق كسكسو باللحم",
                "price": "45 درهم",
                "available": True
            },
            {
                "name": "قصعة كسكسو بالدجاج",
                "price": "250 درهم",
                "available": True
            }
        ],

        "السبت": [
            {
                "name": "ميني بسطيلة دجاج",
                "price": "15 درهم",
                "available": True
            },
            {
                "name": "ميني بسطيلة حوت",
                "price": "20 درهم",
                "available": True
            },
            {
                "name": "بسطيلة دجاج (شخصين)",
                "price": "99 درهم",
                "available": True
            },
            {
                "name": "بسطيلة حوت (شخصين)",
                "price": "159 درهم",
                "available": True
            }
        ],

        "الأحد": []
    }


# =========================================================
# الوقت
# =========================================================

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

date_text = now.strftime("%d/%m/%Y")
time_text = now.strftime("%H:%M")

PHONE = "212775978088"

APP_URL = (
    "https://menu-lakhlifi-iptwnqbcfs3nbergvdqshg."
    "streamlit.app"
)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        """
        <div style="
            text-align:center;
            padding:10px 0 25px;
        ">
            <div style="font-size:50px;">🍲</div>

            <div style="
                font-size:25px;
                font-weight:900;
            ">
                دار الخليفي
            </div>

            <div style="
                font-size:13px;
                opacity:.70;
                margin-top:5px;
            ">
                إدارة المنيو
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    selected_day = st.selectbox(
        "📅 اليوم",
        days_map,
        index=now.weekday()
    )

    st.markdown("---")

    closed = st.checkbox(
        "🚨 المطعم مغلق اليوم",
        value=(selected_day == "الأحد")
    )

    st.markdown("---")

    st.markdown(
        """
        <div style="
            font-size:19px;
            font-weight:900;
            margin-bottom:12px;
        ">
            ➕ إضافة طبق
        </div>
        """,
        unsafe_allow_html=True
    )

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

            st.session_state.custom_dishes[
                selected_day
            ].append(
                {
                    "name": new_name.strip(),
                    "price": new_price.strip(),
                    "available": True
                }
            )

            st.success("تمت إضافة الطبق ✅")

            st.rerun()

        else:

            st.warning(
                "خاصك تدخل اسم الطبق والثمن."
            )


# =========================================================
# HEADER
# =========================================================

st.markdown(
    f"""
    <div class="hero">

        <div class="hero-content">

            <div class="hero-small">
                مطعم مغربي أصيل • مكناس
            </div>

            <div class="hero-title">
                مطعم دار الخليفي 🍲
            </div>

            <div class="hero-subtitle">
                المنيو اليومية والطلبات
                ومشاركة القائمة في الستوري
            </div>

            <div class="hero-date">
                📅 {today_name} {date_text}
                &nbsp;&nbsp; • &nbsp;&nbsp;
                ⏰ {time_text}
            </div>

        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# إغلاق المطعم
# =========================================================

if closed:

    st.error(
        f"🔴 مطعم دار الخليفي مغلق يوم {selected_day}. "
        "نلقاكم غداً إن شاء الله ❤️"
    )

    st.stop()


# =========================================================
# GET DISHES
# =========================================================

dishes = st.session_state.custom_dishes.get(
    selected_day,
    []
)

available_dishes = [
    d for d in dishes
    if d.get("available", True)
]


# =========================================================
# MENU
# =========================================================

st.markdown(
    f"""
    <div class="section-title">
        🍽️ منيو {selected_day}
    </div>

    <div class="section-subtitle">
        {len(available_dishes)} أطباق متوفرة حالياً
    </div>
    """,
    unsafe_allow_html=True
)


if not dishes:

    st.info(
        "🍽️ مازال ما كاين حتى طبق مسجل لهذا اليوم."
    )

else:

    for index, dish in enumerate(dishes):

        col1, col2, col3 = st.columns(
            [6, 1.5, .7],
            vertical_alignment="center"
        )

        with col1:

            st.markdown(
                f"""
                <div class="dish">

                    <div class="dish-name">
                        {html.escape(dish["name"])}
                    </div>

                    <div class="dish-price">
                        {html.escape(dish["price"])}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:

            available = st.checkbox(
                "متوفر",
                value=dish.get(
                    "available",
                    True
                ),
                key=f"available_{selected_day}_{index}"
            )

            st.session_state.custom_dishes[
                selected_day
            ][index]["available"] = available

        with col3:

            if st.button(
                "🗑️",
                key=f"delete_{selected_day}_{index}"
            ):

                st.session_state.custom_dishes[
                    selected_day
                ].pop(index)

                st.rerun()


# =========================================================
# DELIVERY
# =========================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    """
    <div class="info-card">

        <div class="info-title">
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
            🚀 <b>التوصيل السريع VIP:</b>
            من 15 إلى 25 درهم
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# WHATSAPP ORDER
# =========================================================

st.markdown("<br>", unsafe_allow_html=True)

whatsapp_message = urllib.parse.quote(
    "سلام دار الخليفي، بغيت نطلب من المنيو ديال اليوم 🍲"
)

whatsapp_order_url = (
    f"https://wa.me/{PHONE}"
    f"?text={whatsapp_message}"
)

st.markdown(
    f"""
    <a
        href="{whatsapp_order_url}"
        target="_blank"
        style="text-decoration:none;"
    >

        <div style="
            background:
                linear-gradient(
                    135deg,
                    #128C7E,
                    #25D366
                );

            color:white;

            padding:19px;

            border-radius:18px;

            text-align:center;

            font-size:19px;

            font-weight:900;

            box-shadow:
                0 12px 30px
                rgba(37,211,102,.18);
        ">

            📱 اطلب دابا عبر WhatsApp

            <div style="
                font-size:13px;
                font-weight:500;
                margin-top:5px;
            ">
                0775978088
            </div>

        </div>

    </a>
    """,
    unsafe_allow_html=True
)


# =========================================================
# STORY MAKER
# =========================================================

st.markdown(
    """
    <div class="story-box">

        <div class="story-heading">
            📱 Story Maker
        </div>

        <div class="story-desc">
            الكارت كتتولد بنسبة 9:16 وبمقاس
            1080 × 1920، وجميع الأطباق المتوفرة
            كتدخل فيها أوتوماتيكياً.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# DATA FOR JAVASCRIPT
# =========================================================

story_data = {
    "restaurant": "مطعم دار الخليفي",
    "location": "مكناس • الزيتون",
    "day": f"منيو {selected_day}",
    "phone": "0775978088",
    "dishes": [
        {
            "name": d["name"],
            "price": d["price"]
        }
        for d in available_dishes
    ]
}

story_json = json.dumps(
    story_data,
    ensure_ascii=False
)

story_json_safe = (
    story_json
    .replace("\\", "\\\\")
    .replace("</", "<\\/")
    .replace("'", "\\'")
)


# =========================================================
# STORY PREVIEW + IMAGE GENERATOR
# =========================================================

story_component = f"""
<!DOCTYPE html>

<html lang="ar" dir="rtl">

<head>

<meta charset="UTF-8">

<meta
    name="viewport"
    content="
        width=device-width,
        initial-scale=1.0
    "
>

<link
    href="
    https://fonts.googleapis.com/css2?
    family=Tajawal:wght@400;500;600;700;800;900
    &display=swap"
    rel="stylesheet"
>

<style>

* {{
    box-sizing:border-box;
}}

body {{
    margin:0;

    padding:15px;

    background:#111;

    font-family:
        'Tajawal',
        sans-serif;

    color:white;
}}

.wrapper {{
    display:flex;

    justify-content:center;
}}

.story {{
    width:min(100%, 540px);

    aspect-ratio:9 / 16;

    position:relative;

    overflow:hidden;

    border-radius:28px;

    border:3px solid #D4AF37;

    background:
        radial-gradient(
            circle at 15% 8%,
            rgba(212,175,55,.22),
            transparent 22%
        ),
        radial-gradient(
            circle at 90% 88%,
            rgba(255,255,255,.07),
            transparent 25%
        ),
        linear-gradient(
            155deg,
            #350000 0%,
            #680000 45%,
            #970f0f 100%
        );

    box-shadow:
        0 25px 60px
        rgba(0,0,0,.55);

    padding:
        7%
        6%;

    display:flex;

    flex-direction:column;
}}

.logo {{
    text-align:center;

    font-size:clamp(
        22px,
        5vw,
        38px
    );

    font-weight:900;

    line-height:1.2;
}}

.location {{
    text-align:center;

    color:#E9CF78;

    font-size:clamp(
        12px,
        2.5vw,
        20px
    );

    font-weight:700;

    margin-top:5px;
}}

.divider {{
    width:75%;

    height:2px;

    background:#D4AF37;

    opacity:.7;

    margin:
        4% auto;
}}

.day {{
    text-align:center;

    font-size:clamp(
        18px,
        4vw,
        30px
    );

    font-weight:900;

    margin-bottom:4%;
}}

.menu {{
    flex:1;

    display:flex;

    flex-direction:column;

    justify-content:center;

    gap:clamp(
        6px,
        1.2vw,
        13px
    );

    min-height:0;
}}

.item {{
    background:rgba(
        255,
        255,
        255,
        .97
    );

    color:#202020;

    border-radius:16px;

    padding:
        clamp(8px,1.7vw,18px)
        clamp(10px,2vw,20px);

    display:flex;

    align-items:center;

    justify-content:space-between;

    gap:10px;

    box-shadow:
        0 5px 18px
        rgba(0,0,0,.14);

    min-height:0;
}}

.item-name {{
    font-weight:800;

    line-height:1.25;

    font-size:clamp(
        11px,
        2.3vw,
        24px
    );

    overflow-wrap:anywhere;
}}

.price {{
    background:#720000;

    color:white;

    border-radius:10px;

    padding:
        5px 9px;

    font-size:clamp(
        10px,
        2vw,
        20px
    );

    font-weight:900;

    white-space:nowrap;
}}

.footer {{
    text-align:center;

    margin-top:4%;

    font-size:clamp(
        11px,
        2.2vw,
        19px
    );

    line-height:1.5;

    font-weight:700;
}}

.phone {{
    display:inline-block;

    background:#25D366;

    color:white;

    border-radius:30px;

    padding:
        5px 14px;

    margin-top:5px;

    font-weight:900;
}}

</style>

</head>

<body>

<div class="wrapper">

    <div
        class="story"
        id="story"
    >

        <div class="logo">
            🍲 مطعم دار الخليفي
        </div>

        <div class="location">
            مكناس • الزيتون
        </div>

        <div class="divider"></div>

        <div
            class="day"
            id="day"
        ></div>

        <div
            class="menu"
            id="menu"
        ></div>

        <div class="footer">

            📍 مكناس - الزيتون

            <br>

            📱 للطلب عبر WhatsApp

            <br>

            <span class="phone">
                0775978088
            </span>

        </div>

    </div>

</div>

<script>

const DATA = {story_json_safe};

const menu = document.getElementById(
    "menu"
);

const day = document.getElementById(
    "day"
);

day.textContent = DATA.day;


/*
    الحساب الذكي:

    عدد قليل من الأطباق
    = حجم كبير

    عدد كبير من الأطباق
    = حجم أصغر

    ولكن دائماً داخل
    1080 × 1920
*/

const count = DATA.dishes.length;

let itemSize = 1;

if (count <= 4) {{
    itemSize = 1.20;
}}
else if (count <= 6) {{
    itemSize = 1.00;
}}
else if (count <= 8) {{
    itemSize = 0.88;
}}
else if (count <= 10) {{
    itemSize = 0.76;
}}
else if (count <= 12) {{
    itemSize = 0.66;
}}
else {{
    itemSize = 0.58;
}}

DATA.dishes.forEach(
    (dish) => {{

        const item =
            document.createElement(
                "div"
            );

        item.className = "item";

        item.style.fontSize =
            (itemSize * 100) + "%";

        const name =
            document.createElement(
                "div"
            );

        name.className =
            "item-name";

        name.textContent =
            dish.name;

        const price =
            document.createElement(
                "div"
            );

        price.className =
            "price";

        price.textContent =
            dish.price;

        item.appendChild(name);

        item.appendChild(price);

        menu.appendChild(item);
    }}
);


/*
    توليد صورة حقيقية
    1080 × 1920
*/

async function createStoryBlob() {{

    await document.fonts.ready;

    const source =
        document.getElementById(
            "story"
        );

    const canvas =
        document.createElement(
            "canvas"
        );

    canvas.width = 1080;
    canvas.height = 1920;

    const ctx =
        canvas.getContext("2d");

    /*
        background
    */

    const gradient =
        ctx.createLinearGradient(
            0,
            0,
            1080,
            1920
        );

    gradient.addColorStop(
        0,
        "#350000"
    );

    gradient.addColorStop(
        .5,
        "#680000"
    );

    gradient.addColorStop(
        1,
        "#970f0f"
    );

    ctx.fillStyle = gradient;

    ctx.fillRect(
        0,
        0,
        1080,
        1920
    );

    /*
        decorative circles
    */

    ctx.globalAlpha = .10;

    ctx.beginPath();

    ctx.arc(
        130,
        120,
        180,
        0,
        Math.PI * 2
    );

    ctx.fillStyle = "#D4AF37";

    ctx.fill();

    ctx.globalAlpha = 1;

    /*
        border
    */

    ctx.strokeStyle =
        "#D4AF37";

    ctx.lineWidth = 8;

    ctx.roundRect(
        22,
        22,
        1036,
        1876,
        48
    );

    ctx.stroke();


    /*
        helpers
    */

    function roundedRect(
        x,
        y,
        w,
        h,
        r,
        color
    ) {{

        ctx.fillStyle = color;

        ctx.beginPath();

        ctx.roundRect(
            x,
            y,
            w,
            h,
            r
        );

        ctx.fill();
    }}


    function drawCenteredText(
        text,
        x,
        y,
        font,
        color
    ) {{

        ctx.font = font;

        ctx.fillStyle = color;

        ctx.textAlign = "center";

        ctx.direction = "rtl";

        ctx.fillText(
            text,
            x,
            y
        );
    }}


    /*
        Header
    */

    drawCenteredText(
        "🍲 مطعم دار الخليفي",
        540,
        145,
        "900 68px Tajawal",
        "#FFFFFF"
    );

    drawCenteredText(
        "مكناس • الزيتون",
        540,
        205,
        "700 34px Tajawal",
        "#E9CF78"
    );

    ctx.strokeStyle =
        "#D4AF37";

    ctx.lineWidth = 3;

    ctx.beginPath();

    ctx.moveTo(
        130,
        270
    );

    ctx.lineTo(
        950,
        270
    );

    ctx.stroke();


    drawCenteredText(
        DATA.day,
        540,
        345,
        "900 48px Tajawal",
        "#FFFFFF"
    );


    /*
        Menu
    */

    const count =
        DATA.dishes.length;

    const top = 400;

    const bottom = 1550;

    const availableHeight =
        bottom - top;

    let gap = 18;

    let itemHeight =
        (
            availableHeight -
            gap * Math.max(
                0,
                count - 1
            )
        ) / Math.max(
            1,
            count
        );

    /*
        الحفاظ على حجم معقول
    */

    itemHeight =
        Math.max(
            72,
            Math.min(
                145,
                itemHeight
            )
        );

    /*
        إذا كان عدد الأطباق كبير
        نقلل gap
    */

    if (count >= 10) {{
        gap = 10;
    }}

    if (count >= 13) {{
        gap = 7;
        itemHeight = 70;
    }}

    let y = top;

    DATA.dishes.forEach(
        (dish, index) => {{

            roundedRect(
                75,
                y,
                930,
                itemHeight,
                20,
                "#FFFFFF"
            );

            /*
                الاسم
            */

            let fontSize = 31;

            if (count >= 8) {{
                fontSize = 27;
            }}

            if (count >= 11) {{
                fontSize = 23;
            }}

            if (count >= 14) {{
                fontSize = 20;
            }}

            ctx.font =
                "800 " +
                fontSize +
                "px Tajawal";

            ctx.fillStyle =
                "#202020";

            ctx.textAlign =
                "right";

            ctx.direction =
                "rtl";

            let name =
                dish.name;

            /*
                إذا كان الاسم طويل جداً
                نقصه بطريقة محسوبة
            */

            while (
                ctx.measureText(
                    name
                ).width > 690 &&
                name.length > 10
            ) {{
                name =
                    name.substring(
                        0,
                        name.length - 1
                    );
            }}

            if (
                name !== dish.name
            ) {{
                name += "…";
            }}

            ctx.fillText(
                name,
                955,
                y +
                itemHeight / 2 +
                fontSize / 3
            );


            /*
                السعر
            */

            const priceWidth =
                170;

            const priceHeight =
                Math.min(
                    65,
                    itemHeight - 20
                );

            const priceY =
                y +
                (
                    itemHeight -
                    priceHeight
                ) / 2;

            roundedRect(
                95,
                priceY,
                priceWidth,
                priceHeight,
                15,
                "#720000"
            );

            let priceFont =
                26;

            if (count >= 10) {{
                priceFont = 22;
            }}

            drawCenteredText(
                dish.price,
                180,
                priceY +
                priceHeight / 2 +
                priceFont / 3,
                "900 " +
                priceFont +
                "px Tajawal",
                "#FFFFFF"
            );

            y +=
                itemHeight +
                gap;
        }}
    );


    /*
        Footer
    */

    ctx.strokeStyle =
        "#D4AF37";

    ctx.lineWidth = 3;

    ctx.beginPath();

    ctx.moveTo(
        130,
        1690
    );

    ctx.lineTo(
        950,
        1690
    );

    ctx.stroke();


    drawCenteredText(
        "📍 مكناس - الزيتون",
        540,
        1750,
        "700 30px Tajawal",
        "#FFFFFF"
    );

    drawCenteredText(
        "📱 للطلب: 0775978088",
        540,
        1810,
        "800 30px Tajawal",
        "#FFFFFF"
    );


    return new Promise(
        resolve => {{
            canvas.toBlob(
                blob => resolve(blob),
                "image/png",
                1
            );
        }}
    );
}}


/*
    زر تحميل الصورة
*/

async function downloadStory() {{

    const blob =
        await createStoryBlob();

    const url =
        URL.createObjectURL(blob);

    const a =
        document.createElement(
            "a"
        );

    a.href = url;

    a.download =
        "dar-lakhlifi-{selected_day}.png";

    document.body.appendChild(a);

    a.click();

    a.remove();

    URL.revokeObjectURL(url);
}}


/*
    مشاركة الصورة الحقيقية
*/

async function shareStory() {{

    const blob =
        await createStoryBlob();

    const file =
        new File(
            [
                blob
            ],
            "dar-lakhlifi-{selected_day}.png",
            {{
                type:
                    "image/png"
            }}
        );

    if (
        navigator.share &&
        navigator.canShare &&
        navigator.canShare({{
            files: [file]
        }})
    ) {{

        try {{

            await navigator.share({{
                title:
                    "منيو دار الخليفي",

                text:
                    "منيو اليوم 🍲",

                files:
                    [file]
            }});

        }} catch (error) {{

            console.log(
                "Share cancelled",
                error
            );

        }}

    }} else {{

        await downloadStory();

        alert(
            "المتصفح لا يدعم مشاركة الصور مباشرة. تم تحميل الصورة، ويمكنك مشاركتها من الهاتف."
        );
    }}
}}

</script>

</body>
</html>
"""


# =========================================================
# عرض الـ STORY
# =========================================================

st.components.v1.html(
    story_component,
    height=1050,
    scrolling=True
)


# =========================================================
# أزرار المشاركة
# =========================================================

st.markdown(
    """
    <div style="
        background:white;
        border-radius:22px;
        padding:24px;
        margin-top:20px;
        border:1px solid #ece8df;
        box-shadow:0 8px 30px rgba(0,0,0,.04);
    ">

        <div style="
            color:#470000;
            font-size:21px;
            font-weight:900;
        ">
            📲 نشر الـStory
        </div>

        <div style="
            color:#777;
            font-size:14px;
            margin-top:6px;
            line-height:1.7;
        ">
            الصورة مصممة أصلاً بمقاس
            1080 × 1920 بنسبة 9:16،
            وهي نفس النسبة المناسبة للـInstagram Story
            وWhatsApp Status.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


share_html = """
<script>

async function shareFromParent() {

    /*
        هذه الدالة ستبحث عن
        iframe الخاص بالـStory
        وتستعمل دالة المشاركة
        الموجودة داخله.
    */

    try {

        const frames =
            window.parent.document
            .querySelectorAll("iframe");

        for (
            const frame of frames
        ) {

            try {

                if (
                    frame.contentWindow &&
                    frame.contentWindow.shareStory
                ) {

                    await
                    frame.contentWindow
                    .shareStory();

                    return;
                }

            } catch(e) {}

        }

        alert(
            "استعمل زر تحميل الصورة إذا لم يدعم المتصفح المشاركة المباشرة."
        );

    } catch(error) {

        console.log(error);

    }
}

async function downloadFromParent() {

    try {

        const frames =
            window.parent.document
            .querySelectorAll("iframe");

        for (
            const frame of frames
        ) {

            try {

                if (
                    frame.contentWindow &&
                    frame.contentWindow.downloadStory
                ) {

                    await
                    frame.contentWindow
                    .downloadStory();

                    return;
                }

            } catch(e) {}

        }

    } catch(error) {

        console.log(error);

    }
}

</script>

<div style="
    display:flex;
    gap:12px;
">

<button
    onclick="shareFromParent()"
    style="
        flex:1;
        min-height:52px;
        border:none;
        border-radius:15px;
        background:
            linear-gradient(
                135deg,
                #720000,
                #A81717
            );
        color:white;
        font-family:Tajawal,sans-serif;
        font-size:16px;
        font-weight:900;
        cursor:pointer;
    "
>
    📲 مشاركة الصورة
</button>

<button
    onclick="downloadFromParent()"
    style="
        flex:1;
        min-height:52px;
        border:none;
        border-radius:15px;
        background:#222;
        color:white;
        font-family:Tajawal,sans-serif;
        font-size:16px;
        font-weight:900;
        cursor:pointer;
    "
>
    ⬇️ تحميل PNG
</button>

</div>
"""

st.components.v1.html(
    share_html,
    height=75
)


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div style="
        text-align:center;
        color:#999;
        font-size:13px;
        margin-top:45px;
        padding:20px;
    ">
        🍲 مطعم دار الخليفي — مكناس، الزيتون
        <br>
        المنيو اليومية • 2026
    </div>
    """,
    unsafe_allow_html=True
)

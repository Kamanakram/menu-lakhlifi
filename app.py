import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import datetime
import os
import io
import textwrap
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

    @import url(
        'https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;600;700;800;900&display=swap'
    );

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
                transparent 25%
            ),
            radial-gradient(
                circle at 100% 20%,
                rgba(114,0,0,0.07),
                transparent 30%
            ),
            #f7f4ee;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        background: transparent !important;
    }

    .block-container {
        max-width: 1250px !important;
        padding-top: 25px !important;
        padding-bottom: 50px !important;
    }


    /* ========================================================
       HERO
       ======================================================== */

    .hero {
        position: relative;
        overflow: hidden;

        background:
            radial-gradient(
                circle at 15% 20%,
                rgba(212,175,55,0.20),
                transparent 27%
            ),
            linear-gradient(
                135deg,
                #280000 0%,
                #620000 50%,
                #950f0f 100%
            );

        border-radius: 30px;

        padding: 42px 35px;

        color: white;

        box-shadow:
            0 20px 55px rgba(60,0,0,0.20);

        margin-bottom: 30px;
    }

    .hero-content {
        position: relative;
        z-index: 2;
    }

    .hero-kicker {
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

        margin-top: 20px;

        padding: 9px 18px;

        border-radius: 50px;

        background: rgba(255,255,255,0.10);

        border:
            1px solid
            rgba(255,255,255,0.15);

        font-size: 14px;
    }


    /* ========================================================
       TITLES
       ======================================================== */

    .section-title {
        color: #4b0000;
        font-size: 27px;
        font-weight: 900;
        margin-top: 10px;
    }

    .section-description {
        color: #888;
        font-size: 14px;
        margin-bottom: 20px;
    }


    /* ========================================================
       DISH CARD
       ======================================================== */

    .dish-card {
        background: white;

        border-radius: 19px;

        padding: 17px 20px;

        margin-bottom: 10px;

        border:
            1px solid
            rgba(80,0,0,0.06);

        box-shadow:
            0 7px 25px
            rgba(0,0,0,0.045);

        transition:
            transform .18s ease,
            box-shadow .18s ease;
    }

    .dish-card:hover {
        transform: translateY(-2px);

        box-shadow:
            0 12px 30px
            rgba(70,0,0,0.09);
    }

    .dish-name {
        color: #222;

        font-size: 17px;

        font-weight: 800;
    }

    .dish-price {
        color: #820000;

        font-size: 16px;

        font-weight: 900;

        margin-top: 5px;
    }


    /* ========================================================
       INFO
       ======================================================== */

    .info-card {
        background: white;

        border-radius: 22px;

        padding: 24px;

        border:
            1px solid
            #ece8df;

        box-shadow:
            0 8px 30px
            rgba(0,0,0,0.045);
    }

    .info-title {
        color: #470000;

        font-size: 20px;

        font-weight: 900;

        margin-bottom: 12px;
    }

    .delivery-line {
        padding: 9px 0;

        border-bottom:
            1px dashed
            #e4dfd5;

        font-size: 14px;

        color: #444;
    }

    .delivery-line:last-child {
        border-bottom: none;
    }


    /* ========================================================
       STORY SECTION
       ======================================================== */

    .story-header {
        background:
            linear-gradient(
                135deg,
                #280000,
                #650000
            );

        color: white;

        border-radius: 24px;

        padding: 25px;

        margin-top: 30px;

        margin-bottom: 18px;

        box-shadow:
            0 15px 40px
            rgba(60,0,0,0.15);
    }

    .story-title {
        font-size: 25px;
        font-weight: 900;
    }

    .story-description {
        color: #ddd;
        font-size: 14px;
        margin-top: 6px;
    }


    /* ========================================================
       SIDEBAR
       ======================================================== */

    section[data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                #270000,
                #580000 55%,
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

    section[data-testid="stSidebar"]
    [data-baseweb="select"] {
        background: white !important;
    }

    section[data-testid="stSidebar"]
    [data-baseweb="select"] * {
        color: #222 !important;
    }


    /* ========================================================
       BUTTONS
       ======================================================== */

    .stButton > button,
    .stDownloadButton > button {

        min-height: 46px !important;

        border-radius: 13px !important;

        font-family:
            'Tajawal',
            sans-serif !important;

        font-weight: 800 !important;
    }


    /* ========================================================
       MOBILE
       ======================================================== */

    @media (max-width: 700px) {

        .block-container {
            padding:
                12px !important;
        }

        .hero {
            padding:
                30px 22px;

            border-radius:
                23px;
        }

        .hero-title {
            font-size:
                32px;
        }

        .hero-subtitle {
            font-size:
                14px;
        }

        .section-title {
            font-size:
                23px;
        }

    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# 3. قاعدة البيانات
# ============================================================

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


# ============================================================
# 4. التاريخ والوقت
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

date_text = now.strftime("%d/%m/%Y")
time_text = now.strftime("%H:%M")

PHONE = "0775978088"


# ============================================================
# 5. البحث عن خط عربي
# ============================================================

def find_arabic_font(bold=False):

    possible_fonts = []

    if bold:
        possible_fonts = [
            "/usr/share/fonts/truetype/noto/NotoSansArabic-Bold.ttf",
            "/usr/share/fonts/truetype/noto/NotoKufiArabic-Bold.ttf",
            "/usr/share/fonts/truetype/noto/NotoNaskhArabic-Bold.ttf",
        ]
    else:
        possible_fonts = [
            "/usr/share/fonts/truetype/noto/NotoSansArabic-Regular.ttf",
            "/usr/share/fonts/truetype/noto/NotoSansArabicUI-Regular.ttf",
            "/usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf",
        ]

    for font in possible_fonts:

        if os.path.exists(font):
            return font

    return None


# ============================================================
# 6. تحميل الخط
# ============================================================

def load_font(size, bold=False):

    font_path = find_arabic_font(bold)

    if font_path:

        return ImageFont.truetype(
            font_path,
            size
        )

    return ImageFont.load_default()


# ============================================================
# 7. رسم نص عربي
# ============================================================

def draw_centered_text(
    draw,
    text,
    center_x,
    y,
    font,
    fill
):

    bbox = draw.textbbox(
        (0, 0),
        text,
        font=font
    )

    width = bbox[2] - bbox[0]

    x = center_x - width / 2

    draw.text(
        (x, y),
        text,
        font=font,
        fill=fill
    )


# ============================================================
# 8. رسم مستطيل دائري
# ============================================================

def rounded_rectangle(
    draw,
    xy,
    radius,
    fill,
    outline=None,
    width=1
):

    draw.rounded_rectangle(
        xy,
        radius=radius,
        fill=fill,
        outline=outline,
        width=width
    )


# ============================================================
# 9. إنشاء صورة الـStory
# ============================================================

def create_story_image(
    restaurant_name,
    location,
    day_name,
    phone,
    dishes
):

    WIDTH = 1080
    HEIGHT = 1920

    image = Image.new(
        "RGB",
        (WIDTH, HEIGHT),
        "#4b0000"
    )

    draw = ImageDraw.Draw(image)


    # --------------------------------------------------------
    # Background gradient
    # --------------------------------------------------------

    top_color = (48, 0, 0)
    bottom_color = (135, 12, 12)

    for y in range(HEIGHT):

        ratio = y / HEIGHT

        r = int(
            top_color[0]
            +
            (
                bottom_color[0]
                -
                top_color[0]
            )
            * ratio
        )

        g = int(
            top_color[1]
            +
            (
                bottom_color[1]
                -
                top_color[1]
            )
            * ratio
        )

        b = int(
            top_color[2]
            +
            (
                bottom_color[2]
                -
                top_color[2]
            )
            * ratio
        )

        draw.line(
            [(0, y), (WIDTH, y)],
            fill=(r, g, b)
        )


    # --------------------------------------------------------
    # Decorative circles
    # --------------------------------------------------------

    draw.ellipse(
        (-160, -160, 330, 330),
        outline="#806A20",
        width=4
    )

    draw.ellipse(
        (850, 1600, 1250, 2000),
        outline="#806A20",
        width=4
    )


    # --------------------------------------------------------
    # Border
    # --------------------------------------------------------

    rounded_rectangle(
        draw,
        (25, 25, WIDTH - 25, HEIGHT - 25),
        45,
        fill=None,
        outline="#D4AF37",
        width=8
    )


    # --------------------------------------------------------
    # Fonts
    # --------------------------------------------------------

    logo_font = load_font(
        66,
        bold=True
    )

    location_font = load_font(
        34,
        bold=True
    )

    day_font = load_font(
        48,
        bold=True
    )

    footer_font = load_font(
        30,
        bold=True
    )


    # --------------------------------------------------------
    # Header
    # --------------------------------------------------------

    draw_centered_text(
        draw,
        "🍲 " + restaurant_name,
        WIDTH // 2,
        100,
        logo_font,
        "#FFFFFF"
    )

    draw_centered_text(
        draw,
        location,
        WIDTH // 2,
        185,
        location_font,
        "#E7C85C"
    )


    # --------------------------------------------------------
    # Divider
    # --------------------------------------------------------

    draw.line(
        [(130, 265), (950, 265)],
        fill="#D4AF37",
        width=3
    )


    # --------------------------------------------------------
    # Day
    # --------------------------------------------------------

    draw_centered_text(
        draw,
        f"منيو يوم {day_name}",
        WIDTH // 2,
        320,
        day_font,
        "#FFFFFF"
    )


    # --------------------------------------------------------
    # MENU AREA
    # --------------------------------------------------------

    menu_left = 75
    menu_right = 1005

    menu_top = 420
    menu_bottom = 1570

    count = len(dishes)

    if count == 0:

        empty_font = load_font(
            40,
            bold=True
        )

        draw_centered_text(
            draw,
            "لا توجد أطباق متوفرة اليوم",
            WIDTH // 2,
            900,
            empty_font,
            "#FFFFFF"
        )

    else:

        # المسافة بين البطاقات
        if count <= 5:
            gap = 22
        elif count <= 8:
            gap = 16
        elif count <= 11:
            gap = 11
        else:
            gap = 7

        available_height = (
            menu_bottom
            -
            menu_top
            -
            gap * (count - 1)
        )

        item_height = (
            available_height
            /
            count
        )

        # حجم الخط حسب عدد الأطباق
        if count <= 5:
            name_size = 34
            price_size = 28

        elif count <= 8:
            name_size = 30
            price_size = 25

        elif count <= 11:
            name_size = 25
            price_size = 22

        elif count <= 14:
            name_size = 21
            price_size = 19

        else:
            name_size = 18
            price_size = 17

        name_font = load_font(
            name_size,
            bold=True
        )

        price_font = load_font(
            price_size,
            bold=True
        )


        y = menu_top


        for dish in dishes:

            # ------------------------------------------------
            # Card
            # ------------------------------------------------

            rounded_rectangle(
                draw,
                (
                    menu_left,
                    int(y),
                    menu_right,
                    int(y + item_height)
                ),
                20,
                fill="#FFFFFF"
            )


            # ------------------------------------------------
            # Price badge
            # ------------------------------------------------

            badge_width = 185

            badge_height = min(
                70,
                int(item_height - 18)
            )

            badge_x1 = 92

            badge_y1 = (
                y
                +
                (
                    item_height
                    -
                    badge_height
                )
                / 2
            )

            badge_x2 = (
                badge_x1
                +
                badge_width
            )

            badge_y2 = (
                badge_y1
                +
                badge_height
            )

            rounded_rectangle(
                draw,
                (
                    int(badge_x1),
                    int(badge_y1),
                    int(badge_x2),
                    int(badge_y2)
                ),
                15,
                fill="#720000"
            )


            # ------------------------------------------------
            # Price text
            # ------------------------------------------------

            price_bbox = draw.textbbox(
                (0, 0),
                dish["price"],
                font=price_font
            )

            price_w = (
                price_bbox[2]
                -
                price_bbox[0]
            )

            price_h = (
                price_bbox[3]
                -
                price_bbox[1]
            )

            draw.text(
                (
                    int(
                        badge_x1
                        +
                        (
                            badge_width
                            -
                            price_w
                        )
                        / 2
                    ),
                    int(
                        badge_y1
                        +
                        (
                            badge_height
                            -
                            price_h
                        )
                        / 2
                        -
                        3
                    )
                ),
                dish["price"],
                font=price_font,
                fill="#FFFFFF"
            )


            # ------------------------------------------------
            # Dish name
            # ------------------------------------------------

            dish_name = dish["name"]

            max_width = 690

            # تقليص الاسم إذا كان طويلاً جداً
            while (
                draw.textbbox(
                    (0, 0),
                    dish_name,
                    font=name_font
                )[2]
                >
                max_width
                and len(dish_name) > 10
            ):

                dish_name = (
                    dish_name[:-1]
                    .rstrip()
                    + "…"
                )


            name_bbox = draw.textbbox(
                (0, 0),
                dish_name,
                font=name_font
            )

            name_w = (
                name_bbox[2]
                -
                name_bbox[0]
            )

            name_h = (
                name_bbox[3]
                -
                name_bbox[1]
            )

            name_x = (
                960
                -
                name_w
            )

            name_y = (
                y
                +
                (
                    item_height
                    -
                    name_h
                )
                / 2
                -
                4
            )

            draw.text(
                (
                    int(name_x),
                    int(name_y)
                ),
                dish_name,
                font=name_font,
                fill="#222222"
            )


            y += (
                item_height
                +
                gap
            )


    # --------------------------------------------------------
    # Footer
    # --------------------------------------------------------

    draw.line(
        [(130, 1690), (950, 1690)],
        fill="#D4AF37",
        width=3
    )

    draw_centered_text(
        draw,
        "📍 مكناس - الزيتون",
        WIDTH // 2,
        1730,
        footer_font,
        "#FFFFFF"
    )

    draw_centered_text(
        draw,
        f"📱 للطلب: {phone}",
        WIDTH // 2,
        1790,
        footer_font,
        "#FFFFFF"
    )


    # --------------------------------------------------------
    # Return image
    # --------------------------------------------------------

    return image


# ============================================================
# 10. Sidebar
# ============================================================

with st.sidebar:

    st.markdown(
        """
        <div style="
            text-align:center;
            padding:10px 0 25px;
        ">

            <div style="
                font-size:52px;
            ">
                🍲
            </div>

            <div style="
                font-size:26px;
                font-weight:900;
            ">
                دار الخليفي
            </div>

            <div style="
                font-size:13px;
                opacity:.70;
                margin-top:5px;
            ">
                لوحة إدارة المنيو
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    selected_day = st.selectbox(
        "📅 اختار اليوم",
        days_map,
        index=now.weekday()
    )


    st.markdown("---")


    restaurant_closed = st.checkbox(
        "🚨 المطعم مغلق هذا اليوم",
        value=(
            selected_day == "الأحد"
        )
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


    new_dish_name = st.text_input(
        "اسم الطبق",
        placeholder="مثال: طاجين اللحم..."
    )


    new_dish_price = st.text_input(
        "الثمن",
        placeholder="مثال: 40 درهم"
    )


    if st.button(
        "➕ إضافة الطبق",
        use_container_width=True
    ):

        if (
            new_dish_name.strip()
            and
            new_dish_price.strip()
        ):

            st.session_state.custom_dishes[
                selected_day
            ].append(
                {
                    "name":
                        new_dish_name.strip(),

                    "price":
                        new_dish_price.strip(),

                    "available":
                        True
                }
            )

            st.success(
                "تمت إضافة الطبق ✅"
            )

            st.rerun()

        else:

            st.warning(
                "دخل اسم الطبق والثمن."
            )


# ============================================================
# 11. Header
# ============================================================

st.markdown(
    f"""
    <div class="hero">

        <div class="hero-content">

            <div class="hero-kicker">
                مطعم مغربي أصيل • مكناس
            </div>

            <div class="hero-title">
                مطعم دار الخليفي 🍲
            </div>

            <div class="hero-subtitle">
                المنيو اليومية والطلبات
            </div>

            <div class="hero-date">
                📅 {today_name}
                {date_text}
                &nbsp; • &nbsp;
                ⏰ {time_text}
            </div>

        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# 12. إذا كان المطعم مغلق
# ============================================================

if restaurant_closed:

    st.error(
        f"""
        🔴 مطعم دار الخليفي مغلق يوم {selected_day}.

        نلقاكم غداً إن شاء الله ❤️
        """
    )

    st.stop()


# ============================================================
# 13. الأطباق
# ============================================================

dishes = st.session_state.custom_dishes.get(
    selected_day,
    []
)


available_dishes = [
    dish
    for dish in dishes
    if dish.get(
        "available",
        True
    )
]


st.markdown(
    f"""
    <div class="section-title">
        🍽️ منيو {selected_day}
    </div>

    <div class="section-description">
        {len(available_dishes)}
        أطباق متوفرة حالياً
    </div>
    """,
    unsafe_allow_html=True
)


if not dishes:

    st.info(
        "🍽️ ما كاين حتى طبق مسجل لهذا اليوم."
    )

else:

    for index, dish in enumerate(dishes):

        col1, col2, col3 = st.columns(
            [6, 1.5, .6],
            vertical_alignment="center"
        )


        with col1:

            st.markdown(
                f"""
                <div class="dish-card">

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

            is_available = st.checkbox(
                "متوفر",
                value=dish.get(
                    "available",
                    True
                ),
                key=(
                    f"available_"
                    f"{selected_day}_"
                    f"{index}"
                )
            )

            st.session_state.custom_dishes[
                selected_day
            ][index][
                "available"
            ] = is_available


        with col3:

            if st.button(
                "🗑️",
                key=(
                    f"delete_"
                    f"{selected_day}_"
                    f"{index}"
                )
            ):

                st.session_state.custom_dishes[
                    selected_day
                ].pop(index)

                st.rerun()


# ============================================================
# 14. التوصيل
# ============================================================

st.markdown(
    "<br>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="info-card">

        <div class="info-title">
            🛵 أسعار التوصيل
        </div>

        <div class="delivery-line">
            📍 <b>منطقة الزيتون:</b>
            5 دراهم
        </div>

        <div class="delivery-line">
            📍 <b>المناطق القريبة من الزيتون:</b>
            10 دراهم
        </div>

        <div class="delivery-line">
            📍 <b>حمرية والمناطق المجاورة:</b>
            15 درهم
        </div>

        <div class="delivery-line">
            📍 <b>البساتين، البريدية، رياض تولال:</b>
            20 درهم
        </div>

        <div class="delivery-line">
            🚀 <b>التوصيل السريع VIP:</b>
            من 15 إلى 25 درهم
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# 15. زر WhatsApp للطلب
# ============================================================

st.markdown(
    "<br>",
    unsafe_allow_html=True
)

whatsapp_url = (
    "https://wa.me/212775978088"
    "?text=سلام%20دار%20الخليفي،"
    "%20بغيت%20نطلب%20من%20المنيو%20ديال%20اليوم"
)

st.markdown(
    f"""
    <a
        href="{whatsapp_url}"
        target="_blank"
        style="
            text-decoration:none;
        "
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


# ============================================================
# 16. توليد الـStory
# ============================================================

st.markdown(
    """
    <div class="story-header">

        <div class="story-title">
            📱 بطاقة Story
        </div>

        <div class="story-description">
            صورة حقيقية بمقاس 1080 × 1920
            جاهزة للنشر في Instagram Story
            وWhatsApp Status.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


story_image = create_story_image(
    restaurant_name="مطعم دار الخليفي",
    location="مكناس • الزيتون",
    day_name=selected_day,
    phone=PHONE,
    dishes=available_dishes
)


# ============================================================
# 17. عرض الصورة فقط
# ============================================================

st.image(
    story_image,
    width=540
)


# ============================================================
# 18. تحويل الصورة إلى PNG
# ============================================================

image_buffer = io.BytesIO()

story_image.save(
    image_buffer,
    format="PNG"
)

image_bytes = image_buffer.getvalue()


# ============================================================
# 19. أزرار Story
# ============================================================

st.markdown(
    "<br>",
    unsafe_allow_html=True
)

download_col, info_col = st.columns(
    [1, 1]
)


with download_col:

    st.download_button(
        label="📥 تحميل صورة الـStory",
        data=image_bytes,
        file_name=(
            f"dar-lakhlifi-"
            f"{selected_day}.png"
        ),
        mime="image/png",
        use_container_width=True
    )


with info_col:

    st.markdown(
        """
        <div style="
            background:#fff;
            border-radius:14px;
            padding:13px;
            text-align:center;
            border:1px solid #ece8df;
            font-size:13px;
            color:#666;
        ">
            📐 1080 × 1920<br>
            <b>9:16 Story</b>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# 20. تعليمات المشاركة
# ============================================================

st.info(
    """
    📱 **طريقة النشر:**

    اضغطي على «تحميل صورة الـStory»،
    ومن بعد من الهاتف اختاري الصورة من Gallery
    → Share
    → WhatsApp Status أو Instagram Story.

    الصورة نفسها هي اللي غادي تتشارك، ماشي رابط التطبيق.
    """
)


# ============================================================
# 21. Footer
# ============================================================

st.markdown(
    """
    <div style="
        text-align:center;
        color:#999;
        font-size:13px;
        margin-top:45px;
        padding:20px;
    ">

        🍲 مطعم دار الخليفي
        <br>
        مكناس • الزيتون
        <br>
        0775978088

    </div>
    """,
    unsafe_allow_html=True
)

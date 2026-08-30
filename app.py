import streamlit as st
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import datetime
import os
import io
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

    /* STORY SECTION */
    .story-wrap {
        margin-top: 30px;
        margin-bottom: 20px;
        display: flex;
        justify-content: center;
    }
    .story-wrap img {
        border-radius: 22px;
        box-shadow: 0 20px 55px rgba(60,0,0,0.25);
        border: 1px solid rgba(212,175,55,0.35);
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
# 5. الخطوط العربية
# ============================================================

def find_arabic_font(bold=False):
    candidates = (
        [
            "/usr/share/fonts/truetype/noto/NotoSansArabic-Bold.ttf",
            "/usr/share/fonts/truetype/noto/NotoKufiArabic-Bold.ttf",
            "/usr/share/fonts/truetype/noto/NotoNaskhArabic-Bold.ttf",
        ]
        if bold else
        [
            "/usr/share/fonts/truetype/noto/NotoSansArabic-Regular.ttf",
            "/usr/share/fonts/truetype/noto/NotoSansArabicUI-Regular.ttf",
            "/usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf",
        ]
    )
    for font_path in candidates:
        if os.path.exists(font_path):
            return font_path
    return None


_FONT_CACHE = {}

def load_font(size, bold=False):
    key = (size, bold)
    if key in _FONT_CACHE:
        return _FONT_CACHE[key]
    font_path = find_arabic_font(bold)
    font = ImageFont.truetype(font_path, size) if font_path else ImageFont.load_default()
    _FONT_CACHE[key] = font
    return font


def draw_centered_text(draw, text, center_x, y, font, fill):
    bbox = draw.textbbox((0, 0), text, font=font)
    width = bbox[2] - bbox[0]
    draw.text((center_x - width / 2, y), text, font=font, fill=fill)


def rounded_rectangle(draw, xy, radius, fill=None, outline=None, width=1):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def wrap_dish_name(draw, text, font, max_width, max_lines=2):
    """يقسم اسم الطبق إلى سطرين عند الحاجة بدل تصغير الخط أو الحذف بعلامة …"""
    words = text.split(" ")
    lines = []
    current = ""
    for word in words:
        candidate = f"{current} {word}".strip()
        candidate_width = draw.textbbox((0, 0), candidate, font=font)[2]
        if candidate_width <= max_width or not current:
            current = candidate
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)

    if len(lines) > max_lines:
        head = lines[: max_lines - 1]
        tail = " ".join(lines[max_lines - 1:])
        lines = head + [tail]

    return lines


def chunk_dishes_for_stories(dishes, max_per_story=6, single_story_limit=8):
    """
    يقرر عدد صور الـStory اللازمة:
    - حتى 8 أطباق → Story واحدة (بدون التضحية بوضوح النص).
    - أكثر من 8 → يوزَّع المنيو على عدة Stories بشكل متوازن (5-6 أطباق لكل واحدة كحد أقصى)
      حتى يبقى الخط كبيراً ومقروءاً دائماً.
    """
    count = len(dishes)
    if count == 0:
        return [[]]
    if count <= single_story_limit:
        return [dishes]

    num_stories = -(-count // max_per_story)  # ceil division
    base_size = count // num_stories
    remainder = count % num_stories

    chunks = []
    idx = 0
    for i in range(num_stories):
        size = base_size + (1 if i < remainder else 0)
        chunks.append(dishes[idx: idx + size])
        idx += size
    return chunks


def get_dish_font_sizes(count):
    """أحجام الخط حسب عدد الأطباق في نفس الـStory — لا تنزل أبداً تحت حد القراءة الواضحة."""
    if count <= 3:
        return {"name": 40, "price": 36, "gap": 34}
    elif count <= 5:
        return {"name": 38, "price": 34, "gap": 24}
    else:
        return {"name": 32, "price": 28, "gap": 16}


# ============================================================
# 6. توليد صورة/صور الـStory (PNG حقيقية 1080×1920 لكل صورة)
# ============================================================

def render_story_page(restaurant_name, location, day_name, phone, dishes, page_index, total_pages):
    WIDTH, HEIGHT = 1080, 1920
    base = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 255))
    draw = ImageDraw.Draw(base)

    # خلفية متدرجة
    top_color, bottom_color = (40, 0, 0), (128, 14, 14)
    for y in range(HEIGHT):
        ratio = y / HEIGHT
        r = int(top_color[0] + (bottom_color[0] - top_color[0]) * ratio)
        g = int(top_color[1] + (bottom_color[1] - top_color[1]) * ratio)
        b = int(top_color[2] + (bottom_color[2] - top_color[2]) * ratio)
        draw.line([(0, y), (WIDTH, y)], fill=(r, g, b, 255))

    # زخرفة دائرية
    draw.ellipse((-170, -170, 340, 340), outline=(212, 175, 55, 255), width=4)
    draw.ellipse((840, 1610, 1250, 2010), outline=(212, 175, 55, 255), width=4)

    # إطار ذهبي مزدوج (لمسة Canva)
    rounded_rectangle(draw, (25, 25, WIDTH - 25, HEIGHT - 25), 45, outline=(212, 175, 55, 255), width=8)
    rounded_rectangle(draw, (38, 38, WIDTH - 38, HEIGHT - 38), 38, outline=(212, 175, 55, 110), width=2)

    # خطوط الرأس (ضمن الحدود الدنيا/القصوى المطلوبة)
    logo_font = load_font(68, bold=True)          # 50-75px
    location_font = load_font(30, bold=True)      # 25-32px
    day_font = load_font(48, bold=True)           # 40-55px
    footer_font = load_font(32, bold=True)        # 28-35px

    draw_centered_text(draw, "🍲 " + restaurant_name, WIDTH // 2, 92, logo_font, (255, 255, 255, 255))
    draw_centered_text(draw, location, WIDTH // 2, 176, location_font, (231, 200, 92, 255))

    # فاصل مزخرف بمعينة ذهبية في المنتصف
    divider_y = 250
    draw.line([(150, divider_y), (478, divider_y)], fill=(212, 175, 55, 255), width=3)
    draw.line([(602, divider_y), (930, divider_y)], fill=(212, 175, 55, 255), width=3)
    dcx, dcy, dr = WIDTH // 2, divider_y, 10
    draw.polygon(
        [(dcx, dcy - dr), (dcx + dr, dcy), (dcx, dcy + dr), (dcx - dr, dcy)],
        fill=(212, 175, 55, 255)
    )

    title_text = f"منيو يوم {day_name}" if page_index == 0 else f"تكملة منيو {day_name}"
    draw_centered_text(draw, title_text, WIDTH // 2, 296, day_font, (255, 255, 255, 255))

    menu_top = 400
    if total_pages > 1:
        page_tag_font = load_font(24, bold=True)
        draw_centered_text(
            draw, f"({page_index + 1} / {total_pages})", WIDTH // 2, 356, page_tag_font, (231, 200, 92, 255)
        )
        menu_top = 410

    menu_left, menu_right = 75, 1005
    menu_bottom = 1555
    count = len(dishes)

    if count == 0:
        empty_font = load_font(38, bold=True)
        draw_centered_text(draw, "لا توجد أطباق متوفرة اليوم", WIDTH // 2, 950, empty_font, (255, 255, 255, 255))
    else:
        sizes = get_dish_font_sizes(count)
        gap = sizes["gap"]
        name_font = load_font(sizes["name"], bold=True)
        price_font = load_font(sizes["price"], bold=True)

        available_height = (menu_bottom - menu_top) - gap * (count - 1)
        item_height = available_height / count

        # ---- طبقة ظل ناعمة لكل الكروت دفعة واحدة (لمسة Canva احترافية) ----
        shadow_layer = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
        shadow_draw = ImageDraw.Draw(shadow_layer)
        y = menu_top
        for _ in dishes:
            rounded_rectangle(
                shadow_draw,
                (menu_left, int(y + 9), menu_right, int(y + item_height + 9)),
                20,
                fill=(0, 0, 0, 90)
            )
            y += item_height + gap
        shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(10))
        base = Image.alpha_composite(base, shadow_layer)
        draw = ImageDraw.Draw(base)

        # ---- الكروت الفعلية + النصوص ----
        max_name_width = 655
        y = menu_top
        for dish in dishes:
            rounded_rectangle(draw, (menu_left, int(y), menu_right, int(y + item_height)), 20, fill=(255, 255, 255, 255))

            badge_width = 190
            badge_height = max(30, min(74, int(item_height - 18)))
            badge_x1 = 95
            badge_y1 = y + (item_height - badge_height) / 2
            badge_x2 = badge_x1 + badge_width
            badge_y2 = badge_y1 + badge_height
            rounded_rectangle(
                draw,
                (int(badge_x1), int(badge_y1), int(badge_x2), int(badge_y2)),
                15,
                fill=(114, 0, 0, 255),
                outline=(212, 175, 55, 255),
                width=2
            )

            price_bbox = draw.textbbox((0, 0), dish["price"], font=price_font)
            price_w = price_bbox[2] - price_bbox[0]
            price_h = price_bbox[3] - price_bbox[1]
            draw.text(
                (int(badge_x1 + (badge_width - price_w) / 2), int(badge_y1 + (badge_height - price_h) / 2 - 3)),
                dish["price"], font=price_font, fill=(255, 255, 255, 255)
            )

            lines = wrap_dish_name(draw, dish["name"], name_font, max_name_width)
            line_height = name_font.size + 8
            total_text_height = line_height * len(lines)
            text_y = y + (item_height - total_text_height) / 2

            for line in lines:
                line_bbox = draw.textbbox((0, 0), line, font=name_font)
                line_w = line_bbox[2] - line_bbox[0]
                draw.text((960 - line_w, text_y), line, font=name_font, fill=(30, 30, 30, 255))
                text_y += line_height

            y += item_height + gap

    # التذييل
    draw.line([(180, 1650), (900, 1650)], fill=(212, 175, 55, 255), width=3)
    draw_centered_text(draw, "📍 مكناس - الزيتون", WIDTH // 2, 1695, footer_font, (255, 255, 255, 255))
    draw_centered_text(draw, f"📱 {phone}", WIDTH // 2, 1752, footer_font, (255, 255, 255, 255))

    return base.convert("RGB")


def generate_story_images(restaurant_name, location, day_name, phone, dishes):
    """يبني قائمة من صور الـStory (1080×1920 لكل واحدة)، مقسّمة تلقائياً عند الحاجة."""
    chunks = chunk_dishes_for_stories(dishes)
    total = len(chunks)
    return [
        render_story_page(restaurant_name, location, day_name, phone, chunk, i, total)
        for i, chunk in enumerate(chunks)
    ]

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
# 13. توليد بطاقة/بطاقات الـStory
# ============================================================

story_images = generate_story_images(
    restaurant_name="مطعم دار الخليفي",
    location="مكناس • الزيتون",
    day_name=selected_day,
    phone=PHONE,
    dishes=available_dishes
)

total_stories = len(story_images)

for story_idx, story_image in enumerate(story_images):
    image_buffer = io.BytesIO()
    story_image.save(image_buffer, format="PNG")
    image_bytes = image_buffer.getvalue()

    st.markdown('<div class="story-wrap">', unsafe_allow_html=True)
    story_col_left, story_col_center, story_col_right = st.columns([1, 2, 1])
    with story_col_center:
        st.image(story_image, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    if total_stories == 1:
        download_label = "📥 تحميل صورة الـStory"
        file_name = f"dar-lakhlifi-{selected_day}.png"
    else:
        download_label = f"📥 تحميل Story {story_idx + 1}"
        file_name = f"dar-lakhlifi-{selected_day}-part{story_idx + 1}.png"

    btn_left, btn_center, btn_right = st.columns([1, 2, 1])
    with btn_center:
        st.download_button(
            label=download_label,
            data=image_bytes,
            file_name=file_name,
            mime="image/png",
            use_container_width=True,
            key=f"download_story_{story_idx}"
        )

    if story_idx < total_stories - 1:
        st.markdown("<br>", unsafe_allow_html=True)

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

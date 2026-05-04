import flet as ft
import webbrowser

# ══════════════════════════════════════════
#  COLORS
# ══════════════════════════════════════════
BG      = "#060910"
SURFACE = "#0d1117"
CARD    = "#111720"
ACCENT  = "#00d4ff"
ACCENT2 = "#7c3aed"
GOLD    = "#f59e0b"
TEXT    = "#e8edf5"
MUTED   = "#6b7a8d"
SUCCESS = "#10b981"
DANGER  = "#ef4444"
BORDER  = "#1a2535"

DOWNLOAD_LINKS = {
    "Windows (.exe)":    "https://example.com/xenon-ai-setup.exe",
    "Linux (.deb)":      "https://example.com/xenon-ai.deb",
    "Linux (.AppImage)": "https://example.com/xenon-ai.AppImage",
    "Android (.apk)":    "https://example.com/xenon-ai.apk",
    "macOS (.dmg)":      "https://example.com/xenon-ai.dmg",
}

FEATURES = [
    ("⚡", "Молниеносный",  "Ответы за миллисекунды. XENON AI обрабатывает запросы быстро."),
    ("🧠", "Умный",         "Понимает контекст, помнит разговор, делает выводы. Не просто чат-бот."),
    ("🌐", "Многоязычный",  "Русский, английский, казахский и 100+ языков. Общайся как тебе удобно."),
    ("🔒", "Приватный",     "Твои данные не продаются. Никакой слежки. Шифрование end-to-end."),
    ("🎨", "Творческий",    "Генерация кода, текстов и изображений. Помощь в учёбе, дизайне и поиске идей."),
    ("🔧", "Гибкий",        "Подстраивается под тебя: стиль, тон, формат ответов — под твой контроль.      ."),
]

STATS = [
    ("10K+", "Пользователей"),
    ("5.0★",  "Рейтинг"),
    ("99.0%", "Uptime"),
    ("100+",   "Языков"),
]

FAQ_DATA = [
    ("Что такое XENON AI?",
     "XENON AI — интеллектуальная программная среда для эффективной работы с текстом и кодом. "
     "Это независимая разработка, объединяющая передовые алгоритмы в едином интерфейсе для ваших задач."),
    ("Это бесплатно?",
     "Основной функционал XENON доступен бесплатно. Расширенные возможности предусмотрены "
     "в версии Pro с повышенными лимитами и доступом к экспериментальным функциям."),
    ("На каких устройствах работает?",
     "Мы поддерживаем кроссплатформенность: Windows, Linux и Android. Облачная архитектура "
     "позволяет использовать XENON через любой современный браузер без потери производительности."),
    ("Мои данные в безопасности?",
     "Безопасность — наш приоритет. XENON использует сквозное шифрование сессий, а ваши запросы "
     "не передаются третьим лицам и не используются для обучения глобальных моделей."),
    ("Чем XENON отличается от ChatGPT?",
     "XENON — это авторская экосистема с уникальной логикой обработки запросов. Мы предлагаем "
     "более гибкие настройки, отсутствие жестких фильтров и оптимизацию под русскоязычного пользователя."),
]

CHANGELOG = [
    "🆕  Новый движок обработки текста",
    "⚡  Скорость ответа +40%",
    "🎨  Обновлённый интерфейс",
    "🔒  Улучшена система шифрования",
    "🐛  Исправлено 23 бага",
]


# ══════════════════════════════════════════
#  HELPERS
# ══════════════════════════════════════════
def xenon_logo(size=22):
    return ft.ShaderMask(
        content=ft.Text(
            "XENON AI", size=size, weight=ft.FontWeight.W_900,
            font_family="Orbitron", color="white",
        ),
        shader=ft.LinearGradient(
            begin=ft.alignment.Alignment(-1, 0),
            end=ft.alignment.Alignment(1, 0),
            colors=[ACCENT, ACCENT2],
        ),
        blend_mode=ft.BlendMode.SRC_IN,
    )


def gradient_label(text, size=28):
    return ft.ShaderMask(
        content=ft.Text(
            text, size=size, weight=ft.FontWeight.W_900,
            font_family="Orbitron", color="white",
            text_align=ft.TextAlign.CENTER,
        ),
        shader=ft.LinearGradient(
            begin=ft.alignment.Alignment(-1, 0),
            end=ft.alignment.Alignment(1, 0),
            colors=[ACCENT, ACCENT2, GOLD],
        ),
        blend_mode=ft.BlendMode.SRC_IN,
    )


def card_box(content, padding=24, radius=18):
    return ft.Container(
        content=content,
        bgcolor=CARD,
        border_radius=radius,
        border=ft.Border.all(1, BORDER),
        padding=padding,
    )


def sep():
    return ft.Container(height=1, bgcolor=BORDER,
                        margin=ft.Margin.symmetric(vertical=8))


def section_head(left, right):
    return ft.Row([
        ft.Text(left + " ", size=26, weight=ft.FontWeight.W_700,
                color=TEXT, font_family="Orbitron"),
        ft.Text(right, size=26, weight=ft.FontWeight.W_700,
                color=ACCENT, font_family="Orbitron"),
    ])


def accent_btn(label, on_click=None, icon=None):
    return ft.ElevatedButton(
        content=ft.Text(label, weight=ft.FontWeight.W_700, size=14),
        icon=icon,
        on_click=on_click,
        bgcolor=ACCENT,
        color="#000000",
        elevation=6,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            padding=ft.Padding.symmetric(horizontal=24, vertical=14),
        ),
    )

def ghost_btn(label, on_click=None):
    return ft.OutlinedButton(
        content=ft.Text(label, weight=ft.FontWeight.W_600, size=14, color=TEXT),
        on_click=on_click,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            padding=ft.Padding.symmetric(horizontal=24, vertical=14),
            side=ft.BorderSide(1, BORDER),
        ),
    )

# ══════════════════════════════════════════
#  HEADER
# ══════════════════════════════════════════
def build_header(page, scroll_to):
    nav_labels = ["Главная", "О нас", "Функции", "Скачать", "FAQ"]
    nav = ft.Row(
        [ft.TextButton(
            n,
            on_click=lambda e, n=n: scroll_to(n),
            style=ft.ButtonStyle(
                color=MUTED,
                text_style=ft.TextStyle(size=13, weight=ft.FontWeight.W_500),
            ),
        ) for n in nav_labels],
        spacing=0,
    )
    return ft.Container(
        content=ft.Row(
            [xenon_logo(22), nav,
             accent_btn("Скачать", on_click=lambda e: scroll_to("Скачать"))],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor=SURFACE,
        padding=ft.Padding.symmetric(horizontal=40, vertical=14),
        border=ft.Border.only(bottom=ft.BorderSide(1, BORDER)),
    )


# ══════════════════════════════════════════
#  HERO
# ══════════════════════════════════════════
def build_hero(scroll_to):
    badge = ft.Container(
        content=ft.Row([
            ft.Container(
                width=8, height=8, bgcolor=ACCENT, border_radius=50,
            ),
            ft.Text("  Нейросеть нового поколения", size=12, color=ACCENT,
                    weight=ft.FontWeight.W_600),
        ], alignment=ft.MainAxisAlignment.CENTER),
        bgcolor="#0a1e2a",
        border=ft.Border.all(1, "#0a3d4d"),
        border_radius=50,
        padding=ft.Padding.symmetric(horizontal=18, vertical=8),
    )

    big_quote = ft.Container(
        content=ft.Column([
            ft.Text("❝", size=44, color=ACCENT, text_align=ft.TextAlign.CENTER),
            ft.Text(
                "XENON — это не просто нейросеть.\n"
                "Это твой второй разум,\n"
                "который всегда рядом.",
                size=20, color=TEXT, text_align=ft.TextAlign.CENTER,
                weight=ft.FontWeight.W_500,
            ),
            ft.Text("— Команда XENON AI", size=13, color=MUTED,
                    text_align=ft.TextAlign.CENTER),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=12),
        bgcolor="#080f1a",
        border=ft.Border.all(1, "#0a3d4d"),
        border_radius=20,
        padding=ft.Padding.all(32),
        margin=ft.Margin.symmetric(horizontal=60),
    )

    stats = ft.Row(
        [ft.Column([
            ft.Text(s[0], size=26, weight=ft.FontWeight.W_900, color=ACCENT,
                    font_family="Orbitron", text_align=ft.TextAlign.CENTER),
            ft.Text(s[1], size=11, color=MUTED,  # Убрали letter_spacing здесь
                    text_align=ft.TextAlign.CENTER),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            for s in STATS],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=48,
    )

    return ft.Container(
        content=ft.Column([
            ft.Container(height=24),
            badge,
            ft.Container(height=20),
            gradient_label("XENON AI", size=68),
            ft.Container(height=8),
            ft.Text(
                "Будущее говорит с тобой",
                size=20, color=MUTED, text_align=ft.TextAlign.CENTER,
            ),
            ft.Container(height=28),
            big_quote,
            ft.Container(height=28),
            ft.Row([
                accent_btn("⬇  Скачать XENON", on_click=lambda e: scroll_to("Скачать")),
                ghost_btn("Узнать больше", on_click=lambda e: scroll_to("О нас")),
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=14),
            ft.Container(height=40),
            sep(),
            ft.Container(height=24),
            stats,
            ft.Container(height=40),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=0),
        bgcolor=BG,
        padding=ft.Padding.symmetric(horizontal=24),
    )


# ══════════════════════════════════════════
#  ABOUT
# ══════════════════════════════════════════
def build_about():
    cards = ft.Row([
        card_box(ft.Column([
            ft.Text("🎯  Миссия", size=15, weight=ft.FontWeight.W_700, color=TEXT),
            ft.Container(height=8),
            ft.Text(
                "Сделать мощный ИИ доступным каждому. "
                "Без подписок за $20, без VPN, без цензуры.",
                size=13, color=MUTED,
            ),
        ], spacing=0), padding=20),
        card_box(ft.Column([
            ft.Text("🚀  Наш путь", size=15, weight=ft.FontWeight.W_700, color=TEXT),
            ft.Container(height=8),
            ft.Text(
                "Начали в 2026 году. Сегодня XENON AI — "
                "10K+ пользователей и постоянный рост.",
                size=13, color=MUTED,
            ),
        ], spacing=0), padding=20),
        card_box(ft.Column([
            ft.Text("💡  Подход", size=15, weight=ft.FontWeight.W_700, color=TEXT),
            ft.Container(height=8),
            ft.Text(
                "Privacy-first. Никакой продажи данных. "
                "Открытый диалог с сообществом.",
                size=13, color=MUTED,
            ),
        ], spacing=0), padding=20),
    ], spacing=16, wrap=True)

    return ft.Container(
        content=ft.Column([
            section_head("О", "XENON AI"),
            ft.Container(height=12),
            ft.Text(
                "XENON AI — открытая экосистема умных инструментов."
                " Мы создаем уникальную программную среду для удобного взаимодействия с современными нейросетевыми технологиями." 
                " Наша цель — сделать мощный ИИ доступным для каждого пользователя без ограничений, цензуры и сложных настроек",
                size=14, color=MUTED,
            ),
            ft.Container(height=24),
            cards,
        ], spacing=0),
        bgcolor=SURFACE,
        padding=ft.Padding.all(40),
        border=ft.Border.only(
            top=ft.BorderSide(1, BORDER),
            bottom=ft.BorderSide(1, BORDER),
        ),
    )


# ══════════════════════════════════════════
#  FEATURES
# ══════════════════════════════════════════
def build_features():
    feat_cards = []
    for icon, title, desc in FEATURES:
        feat_cards.append(
            ft.Container(
                content=ft.Column([
                    ft.Container(
                        content=ft.Text(icon, size=26),
                        bgcolor="#0a1e2a",
                        border_radius=12,
                        padding=12,
                        width=52, height=52,
                        alignment=ft.alignment.Alignment(0, 0),
                    ),
                    ft.Text(title, size=15, weight=ft.FontWeight.W_700, color=TEXT),
                    ft.Text(desc, size=12, color=MUTED),
                ], spacing=10),
                bgcolor=CARD,
                border_radius=18,
                border=ft.Border.all(1, BORDER),
                padding=22,
                width=270,
            )
        )

    return ft.Container(
        content=ft.Column([
            section_head("Возможности", "XENON"),
            ft.Container(height=8),
            ft.Text("Всё что тебе нужно — уже внутри", size=13, color=MUTED),
            ft.Container(height=24),
            ft.Row(feat_cards, wrap=True, spacing=14, run_spacing=14),
        ], spacing=0),
        bgcolor=BG,
        padding=ft.Padding.all(40),
    )


# ══════════════════════════════════════════
#  DOWNLOAD
# ══════════════════════════════════════════
def build_download(page):
    dd_ref    = ft.Ref[ft.Dropdown]()
    status    = ft.Text("", size=13, color=SUCCESS)

    def on_dl(e):
        dd = dd_ref.current
        if not dd.value:
            status.value = "⚠️  Выбери платформу"
            status.color = GOLD
            page.update()
            return
        url = DOWNLOAD_LINKS.get(dd.value, "")
        if url:
            webbrowser.open(url)
            status.value = f"✅  Загрузка «{dd.value}» начата!"
            status.color = SUCCESS
        else:
            status.value = "❌  Ссылка недоступна"
            status.color = DANGER
        page.update()

    dropdown = ft.Dropdown(
        ref=dd_ref,
        label="Выбери платформу",
        hint_text="Windows, Linux, Android...",
        options=[ft.dropdown.Option(text=k, content=ft.Text(k, color=TEXT)) for k in DOWNLOAD_LINKS],
        border_color=BORDER,
        focused_border_color=ACCENT,
        label_style=ft.TextStyle(color=MUTED),
        text_style=ft.TextStyle(color=TEXT, size=14),
        bgcolor=CARD,
        width=300,
    )

    version_block = ft.Column([
        ft.Row([
            ft.Text("Версия:", size=13, color=MUTED, width=100),
            ft.Text("0.9.4 Beta", size=13, color=ACCENT, weight=ft.FontWeight.W_700),
        ]),
        ft.Row([
            ft.Text("Дата:", size=13, color=MUTED, width=100),
            ft.Text("01.05.2026", size=13, color=TEXT),
        ]),
        ft.Row([
            ft.Text("Размер:", size=13, color=MUTED, width=100),
            ft.Text("~280 MB", size=13, color=TEXT),
        ]),
    ], spacing=8)

    req_block = ft.Column([
        ft.Text("Windows", size=13, color=ACCENT, weight=ft.FontWeight.W_700),
        ft.Text("Win 10/11 · 64-bit · 4 GB RAM", size=12, color=MUTED),
        ft.Container(height=8),
        ft.Text("Linux", size=13, color=ACCENT, weight=ft.FontWeight.W_700),
        ft.Text("Ubuntu 20.04+ · 4 GB RAM", size=12, color=MUTED),
        ft.Container(height=8),
        ft.Text("Android", size=13, color=ACCENT, weight=ft.FontWeight.W_700),
        ft.Text("Android 9.0+ · 2 GB RAM", size=12, color=MUTED),
        ft.Container(height=8),
        ft.Text("macOS", size=13, color=ACCENT, weight=ft.FontWeight.W_700),
        ft.Text("macOS 12+ · 4 GB RAM", size=12, color=MUTED),
    ], spacing=0)

    return ft.Container(
        content=ft.Column([
            section_head("Скачать", "XENON AI"),
            ft.Container(height=8),
            ft.Text("Выбери платформу и начни прямо сейчас", size=13, color=MUTED),
            ft.Container(height=24),
            ft.Row([
                # — Download block
                card_box(ft.Column([
                    ft.Text("⬇  Загрузка", size=17, weight=ft.FontWeight.W_700, color=TEXT),
                    ft.Container(height=16),
                    dropdown,
                    ft.Container(height=14),
                    accent_btn("📥 Скачать", on_click=on_dl, icon=None),
                    ft.Container(height=10),
                    status,
                ], spacing=0), padding=26),

                # — Version info
                card_box(ft.Column([
                    ft.Text("📋  Версия", size=15, weight=ft.FontWeight.W_700, color=TEXT),
                    ft.Container(height=14),
                    version_block,
                    ft.Container(height=14),
                    sep(),
                    ft.Container(height=12),
                    ft.Text("Что нового:", size=12, color=MUTED, weight=ft.FontWeight.W_600),
                    ft.Container(height=8),
                    ft.Column([ft.Text(c, size=12, color=TEXT) for c in CHANGELOG], spacing=5),
                ], spacing=0), padding=26),

                # — Requirements
                card_box(ft.Column([
                    ft.Text("💻  Требования", size=15, weight=ft.FontWeight.W_700, color=TEXT),
                    ft.Container(height=14),
                    req_block,
                ], spacing=0), padding=26),
            ], spacing=16, wrap=True),
        ], spacing=0),
        bgcolor=SURFACE,
        padding=ft.Padding.all(40),
        border=ft.Border.only(
            top=ft.BorderSide(1, BORDER),
            bottom=ft.BorderSide(1, BORDER),
        ),
    )


# ══════════════════════════════════════════
#  FAQ
# ══════════════════════════════════════════
def build_faq():
    items = []
    for q, a in FAQ_DATA:
        tile = ft.ExpansionTile(
            title=ft.Text(q, size=14, weight=ft.FontWeight.W_600, color=TEXT),
            tile_padding=ft.Padding.symmetric(horizontal=20, vertical=4),
            controls=[
                ft.Container(
                    content=ft.Text(a, size=13, color=MUTED),
                    padding=ft.Padding.only(left=20, right=20, bottom=16),
                )
            ],
        )
        items.append(
            ft.Container(
                content=tile,
                bgcolor=CARD,
                border_radius=14,
                border=ft.Border.all(1, BORDER),
                clip_behavior=ft.ClipBehavior.HARD_EDGE,
            )
        )

    return ft.Container(
        content=ft.Column([
            section_head("Частые", "вопросы"),
            ft.Container(height=8),
            ft.Text("Всё что тебя интересует — здесь", size=13, color=MUTED),
            ft.Container(height=24),
            ft.Column(items, spacing=10),
        ], spacing=0),
        bgcolor=BG,
        padding=ft.Padding.all(40),
    )


# ══════════════════════════════════════════
#  CTA BANNER
# ══════════════════════════════════════════
def build_cta(scroll_to):
    return ft.Container(
        content=ft.Column([
            gradient_label("Готов попробовать?", size=40),
            ft.Container(height=10),
            ft.Text(
                "XENON AI — бесплатно, навсегда. Никакой регистрации.",
                size=15, color=MUTED, text_align=ft.TextAlign.CENTER,
            ),
            ft.Container(height=20),
            ft.Row([
                accent_btn("⬇  Скачать XENON AI",
                           on_click=lambda e: scroll_to("Скачать")),
            ], alignment=ft.MainAxisAlignment.CENTER),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=0),
        bgcolor="#060e16",
        border=ft.Border.only(
            top=ft.BorderSide(1, BORDER),
            bottom=ft.BorderSide(1, BORDER),
        ),
        padding=ft.Padding.all(60),
    )


# ══════════════════════════════════════════
#  FOOTER
# ══════════════════════════════════════════
def build_footer(page: ft.Page):
    def show_privacy_dialog(e):
        # Создаем контейнер, который перекрывает всё
        privacy_view = ft.Container(
            bgcolor=TEXT,  # Твой белый цвет
            padding=40,
            expand=True,
            content=ft.Column([
                # Шапка
                ft.Row([
                    ft.TextButton(
                        content=ft.Text("⬅ Назад", color=BG, size=18, weight="bold"),
                        on_click=lambda _: page.overlay.remove(privacy_view) or page.update()
                    ),
                    ft.Text("XENON Privacy Policy", color=BG, size=22, weight="bold")
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),

                ft.Divider(color=BG, height=30),

                # Контент
                ft.Column([
                    ft.Text("ДЕКЛАРАЦИЯ ТЕХНОЛОГИЧЕСКОГО СТЕКА XENON AI", color=BG, weight="bold", size=18),

                    ft.Text("1. АРХИТЕКТУРНЫЕ РЕШЕНИЯ", color=BG, weight="bold", size=14),
                    ft.Text(
                        "Система базируется на гибридной архитектуре «Оркестратор-Исполнитель». "
                        "В основе лежит проприетарный движок XenonEngine, обеспечивающий бесшовную интеграцию "
                        "мультимодальных нейросетей. Использование асинхронного программирования (библиотека asyncio) "
                        "гарантирует работу в фоновом режиме (Background Mode) без блокировки основного потока (Main Thread), "
                        "что критически важно для производительности на Windows и Android.",
                        color=BG, size=11
                    ),

                    ft.Text("\n2. ИНТЕГРАЦИЯ НЕЙРОСЕТЕВЫХ МОДЕЛЕЙ", color=BG, weight="bold", size=14),
                    ft.Text(
                        "XENON осуществляет динамическое переключение между моделями семейства GOOGLE (версии 2.0, 2.0 Flash, 3.0, 3.1). "
                        "Алгоритм выбора модели зависит от текущей нагрузки и сложности задачи. Проект решает проблему "
                        "фрагментарности инструментов, объединяя текстовые интерфейсы Google AI и визуальные генераторы "
                        "в единую экосистему. Это позволяет сократить когнитивную нагрузку на пользователя и ускорить "
                        "создание сложного контента на 40%.",
                        color=BG, size=11
                    ),

                    ft.Text("\n3. ОБРАБОТКА ДАННЫХ И БЕЗОПАСНОСТЬ", color=BG, weight="bold", size=14),
                    ft.Text(
                        "Взаимодействие с внешними API-интерфейсами осуществляется через защищенные протоколы. "
                        "Локальный программный стек на Python/Flet обеспечивает мгновенный отклик интерфейса. "
                        "Все промежуточные данные и история диалогов кэшируются локально, обеспечивая "
                        "автономность работы системы памяти. Шифрование идентификаторов производится по стандарту SHA-256.",
                        color=BG, size=11
                    ),

                    ft.Text("\n4. ПРАВОВЫЕ И ТЕХНИЧЕСКИЕ ПРИМЕЧАНИЯ ", color=BG, weight="bold", size=12),
                    ft.Text(
                        "Проект «XENON AI» является результатом исследования в области кроссплатформенной разработки и "
                        "интеграции ИИ. Использование данного ПО подразумевает понимание принципов работы асинхронных движков. "
                        "Разработчик (Сергей Селихов) не несет ответственности за восстание машин, если вы заставите XENON "
                        "писать код 24/7 без перерыва на питание. Все права на XenonEngine защищены программным кодом 2026 года. "
                        "Если вы читаете этот текст, значит, вы действительно заботитесь о деталях реализации так же, как и мы. "
                        "XENON AI — это не просто чат-бот, это мост между человеческим замыслом и мощью распределенных вычислений.",
                        color=BG, size=9, italic=True
                    ),
                ], scroll=ft.ScrollMode.ADAPTIVE, expand=True)
            ], spacing=20)
        )

        # Вместо AlertDialog используем overlay напрямую
        # Это гарантирует полноэкранность без системных рамок
        privacy_view.left = 0
        privacy_view.top = 0
        privacy_view.width = page.width
        privacy_view.height = page.height

        page.overlay.append(privacy_view)
        page.update()

    async def open_url(e):
        await page.launch_url(e.control.data)

    links = ft.Row([
        ft.TextButton(
            "Политика",
            style=ft.ButtonStyle(text_style=ft.TextStyle(color=MUTED, size=12)),
            on_click=show_privacy_dialog  # Вызываем окно
        ),
        ft.TextButton(
            "GitHub",
            style=ft.ButtonStyle(text_style=ft.TextStyle(color=MUTED, size=12)),
            data="https://github.com/",  # Ссылка
            on_click=open_url
        ),
        ft.TextButton(
            "Telegram",
            style=ft.ButtonStyle(text_style=ft.TextStyle(color=MUTED, size=12)),
            data="https://t.me/+uQhroggleDA2MmZi",  # Ссылка
            on_click=open_url
        ),
    ], spacing=0)

    return ft.Container(
        content=ft.Column([
            ft.Row([
                xenon_logo(20),
                ft.Text("© 2026 XENON AI. Все права защищены.", size=12, color=MUTED),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Container(height=10),
            ft.Row([
                ft.Text("Разработано с ❤️",
                        size=12, color=MUTED),
                links,
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        ], spacing=0),
        bgcolor=SURFACE,
        border=ft.Border.only(top=ft.BorderSide(1, BORDER)),
        padding=ft.Padding.symmetric(horizontal=40, vertical=24),
    )


# ══════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════
async def main(page: ft.Page):
    page.title = "XENON AI — Авторизация"
    page.bgcolor = BG
    page.padding = 0
    page.spacing = 0
    # Отключаем скролл самой страницы, так как скроллиться будет ListView
    page.scroll = None

    page.fonts = {
        "Orbitron": "https://fonts.gstatic.com/s/orbitron/v29/yMJMMIlzdpvBhQQL_SC3X9yhF25-T1nyGy6xpmIyXjU1pg.woff2"
    }

    # --- ПЕРЕМЕННЫЕ ДЛЯ ВХОДА ---
    login_field = ft.TextField(
        label="Логин",
        border_color=BORDER,
        focused_border_color=ACCENT,
        width=300,
        text_style=ft.TextStyle(color=TEXT)
    )
    pass_field = ft.TextField(
        label="Пароль",
        password=True,
        can_reveal_password=True,
        border_color=BORDER,
        focused_border_color=ACCENT,
        width=300,
        text_style=ft.TextStyle(color=TEXT)
    )

    # --- ФУНКЦИЯ ПЕРЕКЛЮЧЕНИЯ (АВТОРИЗАЦИЯ) ---
    async def login_click(e):
        if login_field.value and pass_field.value:
            login_btn.disabled = True
            login_btn.content = ft.ProgressRing(width=16, height=16, stroke_width=2, color="black")
            page.update()

            reg_view.visible = False
            main_view.visible = True
            page.title = "XENON AI — Нейросеть нового поколения"
            page.update()
        else:
            login_field.error_text = "Заполните поле" if not login_field.value else None
            pass_field.error_text = "Заполните поле" if not pass_field.value else None
            page.update()

    login_btn = accent_btn("Войти в XENON", on_click=login_click)

    # --- ОКНО РЕГИСТРАЦИИ (БЛОК 1) ---
    reg_view = ft.Container(
        content=ft.Container(
            content=ft.Column([
                ft.Container(height=100),
                xenon_logo(48),
                ft.Text("SYSTEM ACCESS REQUIRED", color=MUTED, size=12, weight=ft.FontWeight.W_600),
                ft.Container(height=20),
                card_box(ft.Column([
                    login_field,
                    pass_field,
                    ft.Container(height=10),
                    login_btn,
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER), padding=30),
                ft.TextButton("Запросить доступ у администратора", style=ft.ButtonStyle(color=MUTED)),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            width=400,
        ),
        expand=True,
        alignment=ft.Alignment(0, 0),
        visible=True
    )

    # --- КОНТЕНТ САЙТА (БЛОК 2) ---
    # Важно: Контейнерам нужны ключи (key) для скролла
    hero_cont = ft.Container(key="Главная")
    about_cont = ft.Container(key="О нас")
    features_cont = ft.Container(key="Функции")
    download_cont = ft.Container(key="Скачать")
    faq_cont = ft.Container(key="FAQ")

    # ИСПРАВЛЕННАЯ ФУНКЦИЯ СКРОЛЛА
    async def scroll_to(section: str):
        # Словарь, где значения — это сами переменные твоих контейнеров
        targets = {
            "Главная": hero_cont,
            "О нас": about_cont,
            "Функции": features_cont,
            "Скачать": download_cont,
            "FAQ": faq_cont,
        }

        t = targets.get(section)
        if t:
            try:
                # Пытаемся вызвать скролл у списка, передав объект ТЕРВЫМ аргументом
                # БЕЗ слова key= или dest=
                await main_view.scroll_to(t, duration=500)
            except Exception as e:
                # Если не сработало, пробуем через страницу (тоже без имен)
                try:
                    await page.scroll_to(t, duration=500)
                except:
                    print(f"Ошибка скролла: {e}")

        page.update()

    # Сначала создаем ListView
    main_view = ft.ListView([
        build_header(page, lambda n: page.run_task(scroll_to, n)),
        hero_cont,
        about_cont,
        features_cont,
        download_cont,
        faq_cont,
        build_cta(lambda n: page.run_task(scroll_to, n)),
        build_footer(page),
    ], expand=True, auto_scroll=False, visible=False, spacing=0)

    # Теперь наполняем контейнеры контентом
    hero_cont.content = build_hero(lambda n: page.run_task(scroll_to, n))
    about_cont.content = build_about()
    features_cont.content = build_features()
    download_cont.content = build_download(page)
    faq_cont.content = build_faq()

    # Добавляем всё на страницу
    page.add(reg_view, main_view)


if __name__ == "__main__":
    import os
    # Порт 8000 — стандарт для Render, host "0.0.0.0" делает сайт доступным в сети
    ft.app(target=main, view=ft.AppView.WEB_BROWSER, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))

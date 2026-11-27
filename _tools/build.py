#!/usr/bin/env python3
"""Builds mrsam-site/index.html (English) and mrsam-site/ar/index.html (Arabic) from the strings below.
Run:  python3 mrsam-site/_tools/build.py   (from the repo root). Edit the words here, never the generated html.
CONTACT_EMAIL must be a real mailbox before the site is published."""
import json, pathlib, html

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONTACT_EMAIL = "info@mrsam.io"   # confirmed by the owner Nov 27 2026
SITE = "https://mrsam.io"
CASHO = "https://appcasho.com"

T = {
 "en": dict(
  lang="en", dir="ltr", pre="", other_href="ar/", other_label="العربية", other_lang="ar", canonical=SITE + "/",
  title="Mrsam | AI lab and software company",
  desc="Mrsam (مرسام) is an AI lab and software company in Saudi Arabia. We design, build and run our own products, starting with Casho, a marketplace for Saudi Arabia.",
  nav=[("#work", "Work"), ("#about", "About")], contact="Contact", brand="Mrsam",
  h1="AI lab and software company.", lead="We design, build and run our own products, starting with Casho.",
  see="See Casho", talk="Contact",
  work_h="Casho", work_p="A marketplace for Saudi Arabia, built end to end by Mrsam.",
  sheet=[("What it is", "Shop, reels, live shows, auctions and trades"), ("Where", "Saudi Arabia, in Arabic and English"),
         ("AI inside", "Smart search, price tips, listing text, photo safety checks"), ("Payments", "Held until your order arrives, or in installments with Tamara"),
         ("Platform", "iPhone, coming soon to the App Store")],
  visit="Visit appcasho.com", badge="Coming soon to the App Store",
  do_h="What we do", do_p="Three things, done end to end.",
  cells=[("AI", "Applied AI inside real products: search, pricing, writing and safety checks."),
         ("Software", "Mobile apps, backends and payments, built end to end."),
         ("Products", "We run what we build, from support to payouts.")],
  how_h="How we build",
  steps=[("Arabic and English together", "Every screen works in both languages from day one."), ("Safe by design", "Money is held until the order arrives."),
         ("AI where it helps", "Search, pricing and writing, not decoration."), ("Tested on real phones", "Each release is tried on real devices before it ships.")],
  about_h="Mrsam", about_1="Mrsam is an AI lab and software company in Saudi Arabia. We build products from the first sketch to the app store, and we run them ourselves.",
  about_2="Casho is our first.",
  contact_h="Talk to us.", contact_p="Partnerships, investment, press or a project.",
  foot_p="Mrsam, an AI lab and software company in Saudi Arabia.", foot_links=[(CASHO, "Casho"), (CASHO + "/terms.html", "Casho terms"), (CASHO + "/privacy.html", "Casho privacy")],
  steps_n=["01", "02", "03", "04"], logo_alt="Mrsam", casho_alt="Casho", skip="Skip to content"),
 "ar": dict(
  lang="ar", dir="rtl", pre="../", other_href="../", other_label="English", other_lang="en", canonical=SITE + "/ar/",
  title="مرسام (Mrsam) | مختبر ذكاء اصطناعي وشركة برمجيات",
  desc="مرسام (Mrsam) مختبر ذكاء اصطناعي وشركة برمجيات في المملكة العربية السعودية. نصمم ونبني وندير منتجاتنا بأنفسنا، وأولها كاشو، سوق للمملكة العربية السعودية.",
  nav=[("#work", "الأعمال"), ("#about", "من نحن")], contact="تواصل معنا", brand="مرسام",
  h1="مختبر ذكاء اصطناعي وشركة برمجيات.", lead="نصمم ونبني وندير منتجاتنا بأنفسنا، وأولها كاشو.",
  see="شاهد كاشو", talk="تواصل معنا",
  work_h="كاشو", work_p="سوق للمملكة العربية السعودية، بنته مرسام من الفكرة إلى التطبيق.",
  sheet=[("ما هو", "متجر وريلز وبثوث مباشرة ومزادات ومبادلة"), ("أين", "المملكة العربية السعودية، بالعربية والإنجليزية"),
         ("الذكاء الاصطناعي", "بحث ذكي واقتراح أسعار وأوصاف منتجات وفحص سلامة الصور"), ("الدفع", "المبلغ محفوظ حتى يصلك الطلب، أو بالتقسيط مع تمارا"),
         ("المنصة", "الآيفون، قريباً على آب ستور")],
  visit="زر appcasho.com", badge="قريباً على آب ستور",
  do_h="ماذا نفعل", do_p="ثلاثة أشياء، من البداية إلى النهاية.",
  cells=[("ذكاء اصطناعي", "ذكاء اصطناعي داخل منتجات حقيقية: بحث وتسعير وكتابة وفحص أمان."),
         ("برمجيات", "تطبيقات جوال وأنظمة خلفية ومدفوعات، نبنيها من الألف إلى الياء."),
         ("منتجات", "ندير ما نبنيه، من الدعم إلى تحويل الأرباح.")],
  how_h="كيف نبني",
  steps=[("عربي وإنجليزي معاً", "كل شاشة تعمل باللغتين من اليوم الأول."), ("آمن من التصميم", "المبلغ محفوظ حتى يصل الطلب."),
         ("ذكاء اصطناعي حيث ينفع", "بحث وتسعير وكتابة، لا للزينة."), ("مجرّب على جوالات حقيقية", "كل إصدار يُجرَّب على أجهزة حقيقية قبل أن يصدر.")],
  about_h="مرسام", about_1="مرسام مختبر ذكاء اصطناعي وشركة برمجيات في المملكة العربية السعودية. نبني المنتجات من أول فكرة إلى متجر التطبيقات، وندير ما نبنيه بأنفسنا.",
  about_2="كاشو أول منتجاتنا.",
  contact_h="تواصل معنا.", contact_p="شراكات أو استثمار أو صحافة أو مشروع.",
  foot_p="مرسام، مختبر ذكاء اصطناعي وشركة برمجيات في المملكة العربية السعودية.", foot_links=[(CASHO + "/ar/", "كاشو"), (CASHO + "/terms.html", "شروط كاشو"), (CASHO + "/privacy.html", "خصوصية كاشو")],
  steps_n=["٠١", "٠٢", "٠٣", "٠٤"], logo_alt="مرسام", casho_alt="كاشو", skip="تخطَّ إلى المحتوى"),
}
e = html.escape


def page(c):
    p = c["pre"]
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Organization", "@id": SITE + "/#org", "name": "Mrsam", "alternateName": ["مرسام", "Mrsam (مرسام)"], "url": SITE + "/",
         "logo": {"@type": "ImageObject", "url": SITE + "/assets/icon-192.png", "width": 192, "height": 192},
         "description": T["en"]["desc"], "areaServed": "SA", "knowsAbout": ["Artificial intelligence", "Software development", "Marketplaces"],
         "owns": {"@type": "Organization", "name": "Casho", "alternateName": "كاشو", "url": CASHO + "/"}},
        {"@type": "WebSite", "@id": SITE + "/#site", "url": SITE + "/", "name": "Mrsam", "publisher": {"@id": SITE + "/#org"}, "inLanguage": ["en", "ar"]},
        {"@type": "WebPage", "@id": c["canonical"] + "#page", "url": c["canonical"], "name": c["title"], "description": c["desc"], "inLanguage": c["lang"], "isPartOf": {"@id": SITE + "/#site"}, "about": {"@id": SITE + "/#org"}}]}
    nav = "".join(f'<a href="{h}">{e(t)}</a>' for h, t in c["nav"])
    sheet = "".join(f'<li><span class="k">{e(k)}</span><span class="v">{e(v)}</span></li>' for k, v in c["sheet"])
    cells = "".join(f'<div><h3>{e(t)}</h3><p>{e(d)}</p></div>' for t, d in c["cells"])
    steps = "".join(f'<div><span class="figure num">{n}</span><h3>{e(t)}</h3><p>{e(d)}</p></div>' for n, (t, d) in zip(c["steps_n"], c["steps"]))
    foot = "".join(f'<a href="{h}">{e(t)}</a>' for h, t in c["foot_links"])
    return f"""<!doctype html>
<html lang="{c['lang']}" dir="{c['dir']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(c['title'])}</title>
<meta name="description" content="{e(c['desc'])}">
<link rel="canonical" href="{c['canonical']}">
<link rel="alternate" hreflang="en" href="{SITE}/"><link rel="alternate" hreflang="ar" href="{SITE}/ar/"><link rel="alternate" hreflang="x-default" href="{SITE}/">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta property="og:type" content="website"><meta property="og:site_name" content="Mrsam"><meta property="og:title" content="{e(c['title'])}"><meta property="og:description" content="{e(c['desc'])}"><meta property="og:url" content="{c['canonical']}"><meta property="og:image" content="{SITE}/assets/og.png"><meta property="og:locale" content="{'ar_SA' if c['lang']=='ar' else 'en_US'}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{e(c['title'])}"><meta name="twitter:image" content="{SITE}/assets/og.png">
<meta name="theme-color" content="#0c0b0a">
<link rel="icon" href="{p}assets/favicon-48.png" sizes="48x48"><link rel="icon" href="{p}assets/icon-192.png" type="image/png" sizes="192x192"><link rel="apple-touch-icon" href="{p}apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sofia+Sans+Extra+Condensed:wght@200;400&family=Barlow:wght@300;400&display=swap" rel="stylesheet">
<style>@font-face{{font-family:Tajawal;src:url({p}assets/fonts/Tajawal-Regular-ar.woff2) format("woff2");font-weight:400;font-display:swap;unicode-range:U+0600-06FF,U+0750-077F,U+FB50-FDFF,U+FE70-FEFF,U+200C-200F}}@font-face{{font-family:Tajawal;src:url({p}assets/fonts/Tajawal-Bold-ar.woff2) format("woff2");font-weight:700 800;font-display:swap;unicode-range:U+0600-06FF,U+0750-077F,U+FB50-FDFF,U+FE70-FEFF,U+200C-200F}}</style>
<script>document.documentElement.className+=" js"</script>
<link rel="stylesheet" href="{p}styles.css">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False, separators=(',', ':'))}</script>
</head>
<body>
<canvas id="bg" aria-hidden="true"></canvas>
<a class="visually-hidden" href="#main">{e(c['skip'])}</a>
<header class="nav"><div class="container">
<a class="nav__logo" href="{c['other_href'] if False else ('/' if c['lang']=='en' else '/ar/')}" aria-label="{e(c['brand'])}"><img src="{p}assets/mrsam-logo.svg" width="96" height="40" alt="{e(c['logo_alt'])}"></a>
<nav class="nav__links" aria-label="Main">{nav}<a class="nav__contact" href="mailto:{CONTACT_EMAIL}">{e(c['contact'])}</a><a class="nav__lang" href="{c['other_href']}" hreflang="{c['other_lang']}" lang="{c['other_lang']}">{e(c['other_label'])}</a></nav>
</div></header>
<main id="main">
<section class="hero"><div class="container">
<div><h1>{e(c['h1'])}</h1><p class="lead">{e(c['lead'])}</p>
<div class="actions"><a class="btn btn--primary" href="{CASHO}/{'ar/' if c['lang']=='ar' else ''}">{e(c['see'])}</a><a class="btn" href="mailto:{CONTACT_EMAIL}">{e(c['talk'])}</a></div></div>
</div></section>
<section class="section well grained" id="work"><div class="container">
<div class="section__head"><div class="work__brand"><h2><img src="{p}assets/{'casho-logo-ar-dark.webp' if c['lang']=='ar' else 'casho-logo-dark.webp'}" width="{195 if c['lang']=='ar' else 292}" height="80" alt="{e(c['casho_alt'])}" loading="lazy" decoding="async"></h2></div><p>{e(c['work_p'])}</p></div>
<ul class="sheet">{sheet}</ul>
<div class="link-line"><span class="badge" aria-disabled="true"><svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor" aria-hidden="true"><path d="M12.15 6.9c-.95 0-2.4-1.08-3.96-1.04-2.04.03-3.91 1.18-4.96 3.01-2.12 3.68-.55 9.1 1.52 12.09 1.01 1.45 2.2 3.09 3.79 3.04 1.52-.06 2.09-.99 3.94-.99 1.83 0 2.35.99 3.96.95 1.64-.03 2.68-1.48 3.68-2.95 1.16-1.69 1.64-3.33 1.66-3.42-.04-.01-3.18-1.22-3.22-4.86-.03-3.04 2.48-4.49 2.6-4.56-1.43-2.09-3.62-2.32-4.39-2.38-2-.16-3.68 1.09-4.61 1.09zM15.53 3.83c.84-1.01 1.4-2.43 1.25-3.83-1.21.05-2.66.8-3.53 1.82-.78.9-1.45 2.34-1.27 3.71 1.34.1 2.72-.69 3.55-1.7"/></svg>{e(c['badge'])}</span><a href="{CASHO}/{'ar/' if c['lang']=='ar' else ''}">{e(c['visit'])}</a></div>
</div></section>
<section class="section" id="do"><div class="container">
<div class="section__head"><h2>{e(c['do_h'])}</h2><p>{e(c['do_p'])}</p></div>
<div class="cells">{cells}</div>
</div></section>
<section class="section" id="how"><div class="container">
<div class="section__head"><h2>{e(c['how_h'])}</h2></div>
<div class="steps">{steps}</div>
</div></section>
<section class="section about" id="about"><div class="container">
<div class="section__head"><h2>{e(c['about_h'])}</h2><div><p class="lead">{e(c['about_1'])}</p><p class="lead">{e(c['about_2'])}</p></div></div>
</div></section>
<section class="section contact well grained" id="contact"><div class="contact__body"><div class="container">
<h2>{e(c['contact_h'])}</h2><p class="lead">{e(c['contact_p'])}</p>
<a class="contact__mail" href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>
</div></div>
<footer class="foot"><div class="container">
<div><img src="{p}assets/mrsam-logo.svg" width="136" height="56" alt="{e(c['logo_alt'])}" loading="lazy"><p>{e(c['foot_p'])}</p><p>© 2026 {e(c['brand'])}</p></div>
<nav aria-label="Footer">{foot}</nav>
</div></footer>
</section>
</main>
<script src="{p}assets/bg.js" defer></script>
<script src="{p}assets/motion.js" defer></script>
</body>
</html>
"""


(ROOT / "index.html").write_text(page(T["en"]))
(ROOT / "ar").mkdir(exist_ok=True)
(ROOT / "ar" / "index.html").write_text(page(T["ar"]))
words = lambda c: sum(len(str(v).split()) for k, v in c.items() if k in ("h1", "lead", "work_p", "do_p", "about_1", "about_2", "contact_p"))
print("built; EN hero+text words ~", words(T["en"]))

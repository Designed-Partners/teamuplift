import os
ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://teamuplift.org"

I = {
 "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
 "mentor": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 10 12 5 2 10l10 5 10-5z"/><path d="M6 12v5c3 2 9 2 12 0v-5"/></svg>',
 "health": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8l1 1.1L12 21l7.8-7.5 1-1.1a5.5 5.5 0 0 0 0-7.8z"/><path d="M3.5 12h4l2-3 3 6 2-3h6"/></svg>',
 "home": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 10.5 12 3l9 7.5"/><path d="M5 9.5V21h14V9.5"/><path d="M10 21v-6h4v6"/></svg>',
 "vote": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 13h16v8H4z"/><path d="M8 13V5a1 1 0 0 1 1-1h6a1 1 0 0 1 1 1v8"/><path d="m10 8.5 1.5 1.5 3-3"/></svg>',
 "stem": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 3h6"/><path d="M10 3v6L4.5 18.5A1.7 1.7 0 0 0 6 21h12a1.7 1.7 0 0 0 1.5-2.5L14 9V3"/><path d="M7 15h10"/></svg>',
 "money": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 17l6-6 4 4 8-8"/><path d="M15 7h6v6"/></svg>',
 "hands": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/></svg>',
 "gift": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 12v9H4v-9"/><path d="M2 7h20v5H2z"/><path d="M12 21V7"/><path d="M12 7H7.5a2.5 2.5 0 0 1 0-5C11 2 12 7 12 7zM12 7h4.5a2.5 2.5 0 0 0 0-5C13 2 12 7 12 7z"/></svg>',
 "link": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 13a5 5 0 0 0 7.5.5l3-3a5 5 0 0 0-7-7l-1.7 1.7"/><path d="M14 11a5 5 0 0 0-7.5-.5l-3 3a5 5 0 0 0 7 7l1.7-1.7"/></svg>',
 "star": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m12 2 3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/></svg>',
 "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 6-10 7L2 6"/></svg>',
 "user": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></svg>',
 "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg>',
 "lock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg>',
 "ig": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="0.6" fill="currentColor"/></svg>',
}

NAV = [("who-we-are", "Who We Are"), ("what-we-do", "What We Do"), ("get-involved", "Get Involved"), ("contact", "Contact")]

def page(slug, title, desc, body, extra_head="", absolute=False):
    depth_path = f"/{slug}/" if slug else "/"
    links = "".join(
        f'<li><a href="/{s}/"{" aria-current=\"page\"" if s == slug else ""}>{n}</a></li>' for s, n in NAV)
    donate_current = ' aria-current="page"' if slug == "donate" else ""
    full_title = f"{title} | Team Uplift Coalition" if slug else "Team Uplift Coalition | Empowering Youth in Los Angeles"
    html = f"""<!doctype html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}{depth_path}">
<meta name="theme-color" content="#402638">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Team Uplift Coalition">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE}{depth_path}">
<meta property="og:image" content="{SITE}/assets/img/youth-bike-workshop.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="/assets/img/favicon.png">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800;900&family=Fraunces:ital,opsz,wght@1,9..144,500&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/styles.css">
{extra_head}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <nav class="wrap nav" aria-label="Main">
    <a class="brand" href="/" aria-label="Team Uplift home"><img src="/assets/img/logo.png" alt="Team Uplift" width="480" height="355"></a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav-links" aria-label="Open menu"><span></span></button>
    <ul class="nav-links" id="nav-links">
      {links}
      <li><a class="btn btn--gold" href="/donate/"{donate_current}>Donate</a></li>
    </ul>
  </nav>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-brand">
        <img src="/assets/img/logo.png" alt="Team Uplift" width="480" height="355" loading="lazy">
        <p>Team Uplift Coalition, Inc. empowers youth across Los Angeles through mentorship, scholarship, health and wellness, neighborhood service, and civic engagement.</p>
        <div class="social">
          <a href="https://www.instagram.com/teamupliftla/" target="_blank" rel="noopener" aria-label="Team Uplift on Instagram">{I['ig']}</a>
          <a href="mailto:info@teamuplift.org" aria-label="Email Team Uplift">{I['mail']}</a>
        </div>
      </div>
      <div>
        <h4>Explore</h4>
        <ul>
          <li><a href="/who-we-are/">Who We Are</a></li>
          <li><a href="/what-we-do/">What We Do</a></li>
          <li><a href="/get-involved/">Get Involved</a></li>
          <li><a href="/donate/">Donate</a></li>
          <li><a href="/dues/">Members</a></li>
        </ul>
      </div>
      <div>
        <h4>Connect</h4>
        <ul>
          <li><a href="/contact/">Contact Us</a></li>
          <li><a href="mailto:info@teamuplift.org">info@teamuplift.org</a></li>
          <li><a href="https://www.instagram.com/teamupliftla/" target="_blank" rel="noopener">@teamupliftla</a></li>
          <li><a href="https://www.lambdaomicronques.com/" target="_blank" rel="noopener">Lambda Omicron Chapter</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span data-year>2026</span> Team Uplift Coalition, Inc. All rights reserved.</span>
      <span>Proudly serving Los Angeles</span>
    </div>
  </div>
</footer>
<script src="/assets/js/main.js" defer></script>
</body>
</html>
"""
    if not absolute:
        # Relative paths so pages work from any folder or when opened directly from disk
        prefix = "../" if slug else ""
        html = html.replace('href="/"', f'href="{prefix or "./"}"')
        html = html.replace('href="/', f'href="{prefix}').replace('src="/', f'src="{prefix}')
    path = os.path.join(ROOT, slug, "index.html") if slug else os.path.join(ROOT, "index.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(html)

def cta(title_html, text, primary=("/donate/", "Donate today"), secondary=("/get-involved/", "Get involved")):
    return f"""<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="cta reveal">
      <div>
        <h2>{title_html}</h2>
        <p>{text}</p>
      </div>
      <div class="btn-row">
        <a class="btn btn--gold" href="{primary[0]}">{primary[1]} {I['arrow']}</a>
        <a class="btn btn--ghost-light" href="{secondary[0]}">{secondary[1]}</a>
      </div>
    </div>
  </div>
</section>"""

PROGRAMS = [
 ("mentorship", "mentor", "Youth Mentorship &amp; Scholarship", "Mentors who invest in growth, and scholarships that remove financial barriers to higher education."),
 ("health", "health", "Health &amp; Wellness", "Physical, mental, and spiritual well-being as the foundation for everything a young person builds."),
 ("service", "home", "Neighborhood Service", "Initiatives like the Crenshaw Community Clean Up that keep our neighborhoods safe, clean, and cared for."),
 ("civic", "vote", "Civic Engagement", "Nonpartisan voter registration and ballot education that turns registrations into votes cast."),
 ("stem", "stem", "STEM &amp; Career Exposure", "Hands-on STEM learning and career paths young people might not otherwise encounter."),
 ("financial-literacy", "money", "Financial Literacy", "Practical knowledge, from budgeting to long-term planning, for a stable and independent future."),
]

# ---------------- HOME ----------------
cards = "".join(f"""
      <a class="card reveal" href="/what-we-do/#{a}">
        <span class="icon">{I[ic]}</span>
        <h3>{t}</h3>
        <p>{d}</p>
        <span class="more">Learn more {I['arrow']}</span>
      </a>""" for a, ic, t, d in PROGRAMS)

marquee_items = "".join("<span>Together We Can Make A Difference</span>" for _ in range(8))

home = f"""
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <span class="eyebrow">Los Angeles Nonprofit</span>
      <h1>Every child has the right to access. <span class="accent">All 2 million of them.</span></h1>
      <p class="lead">We empower youth in Los Angeles with life skills, exposure to diverse career paths, and comprehensive STEM education, fostering mental, spiritual, and physical well-being while promoting financial literacy.</p>
      <div class="btn-row">
        <a class="btn" href="/donate/">Support our youth {I['arrow']}</a>
        <a class="btn btn--ghost" href="/what-we-do/">See what we do</a>
      </div>
    </div>
    <div class="hero-media">
      <svg class="hero-arrow" viewBox="0 0 120 120" fill="currentColor" aria-hidden="true"><path d="M60 4 100 48H74v64H46V48H20z"/></svg>
      <div class="photo"><img src="/assets/img/wellness-crenshaw-ymca.jpg" alt="Young men and mentors gathered in a circle for a wellness session at the Crenshaw YMCA" width="1132" height="1183" fetchpriority="high"></div>
      <div class="hero-badge"><strong>2 Million</strong><span>children in Los Angeles who deserve opportunity</span></div>
    </div>
  </div>
</section>

<section class="section bg-cream" style="padding-top:var(--section)">
  <div class="wrap">
    <div class="section-head reveal">
      <div>
        <span class="eyebrow">What we do</span>
        <h2>Six ways we invest in the leaders of tomorrow.</h2>
      </div>
      <p class="lead">From mentorship to the ballot box, our programs meet young people and families where they are and help them see what&rsquo;s possible.</p>
    </div>
    <div class="cards">{cards}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div class="split-media reveal">
      <img src="/assets/img/bulldog-run.jpg" alt="Runners showing off their medals at The Bulldog Run 5K" width="1800" height="1200" loading="lazy">
      <span class="tag">The Bulldog Run 5K</span>
    </div>
    <div class="reveal">
      <span class="eyebrow">Community events</span>
      <h2>Running forward, <em class="accent">together.</em></h2>
      <p class="lead">We&rsquo;re proud to sponsor The Bulldog Run, a 5K at Kenneth Hahn State Recreation Area that brings the LA community together in support of health, connection, and shared purpose.</p>
      <p>Our partnership reflects a deeper commitment to the neighborhoods we serve&mdash;championing local events that get residents moving, families cheering, and communities thriving. Whether you&rsquo;re racing for a personal best or walking alongside a friend, every stride helps build the vibrant, active community we all call home.</p>
      <a class="text-link" href="/what-we-do/#health">More on Health &amp; Wellness</a>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap split split--flip">
    <div class="split-media reveal">
      <img src="/assets/img/youth-bike-workshop.jpg" alt="Youth, mentors, and volunteers holding bicycles at a community bike repair workshop" width="1800" height="1350" loading="lazy">
    </div>
    <div class="reveal">
      <span class="eyebrow">Our approach</span>
      <h2>Building stronger communities together.</h2>
      <p class="lead">We&rsquo;re dedicated to fostering vibrant, inclusive neighborhoods where everyone has the opportunity to thrive.</p>
      <p>Through strategic partnerships, community engagement, and innovative programs, we work to enhance local resources, create safe and welcoming spaces, and empower residents to take an active role in shaping their future. Together, we&rsquo;re building stronger connections and creating lasting impact.</p>
      <div class="btn-row" style="margin-top:28px">
        <a class="btn" href="/get-involved/">Get involved {I['arrow']}</a>
      </div>
    </div>
  </div>
</section>

<section class="section band">
  <div class="wrap">
    <div class="reveal" style="max-width:760px">
      <span class="eyebrow">Measurable results</span>
      <h2>Our youth programming is designed to inspire, educate, and empower.</h2>
      <p class="lead">Through mentorship, skill-building workshops, and community-focused initiatives, we provide opportunities for personal growth, leadership development, and meaningful engagement.</p>
    </div>
    <div class="trio reveal">
      <div><span class="num">01</span><h3>Inspire</h3><p>Real relationships with mentors who help young people see what&rsquo;s possible for their future.</p></div>
      <div><span class="num">02</span><h3>Educate</h3><p>STEM learning, career exposure, and financial literacy that open a wider range of futures.</p></div>
      <div><span class="num">03</span><h3>Empower</h3><p>Leadership, service, and civic participation that build confident, connected community members.</p></div>
    </div>
  </div>
</section>

<div class="marquee" aria-hidden="true"><div class="marquee-track">{marquee_items}</div></div>

<section class="section">
  <div class="wrap">
    <div class="partner reveal">
      <div class="partner-media"><img src="/assets/img/team-gala.jpg" alt="Members of Team Uplift and Lambda Omicron Chapter at a community gala" width="1800" height="1200" loading="lazy"></div>
      <div class="partner-body">
        <span class="eyebrow">Established team &middot; Community based</span>
        <h2>Rooted in eight decades of service in South Los Angeles.</h2>
        <p>Team Uplift Coalition, Inc. empowers youth across Los Angeles through mentorship, scholarship, health and wellness, neighborhood service, and civic engagement.</p>
        <p>In partnership with Lambda Omicron Chapter of Omega Psi Phi Fraternity, Inc., we&rsquo;re building a stronger, more informed, and more connected community, <strong>one young person at a time.</strong></p>
        <a class="btn btn--ghost" href="/who-we-are/">Our story {I['arrow']}</a>
      </div>
    </div>
  </div>
</section>

{cta('Together we can <span class="accent">make a difference.</span>', 'Your support directly funds youth programming, scholarships, and community initiatives across Los Angeles.')}
"""
page("", "Home", "Team Uplift Coalition empowers youth in Los Angeles through mentorship, scholarship, health and wellness, neighborhood service, STEM education, financial literacy, and civic engagement.", home)

# ---------------- WHO WE ARE ----------------
principles = "".join(f'<div class="principle reveal"><span class="letter">{w[0]}</span><h3>{w}</h3></div>' for w in ["Manhood", "Scholarship", "Perseverance", "Uplift"])
who = f"""
<section class="page-hero">
  <div class="wrap">
    <span class="eyebrow">Who we are</span>
    <h1>Empowering LA&rsquo;s youth to <span class="accent">thrive.</span></h1>
    <p class="lead">A Los Angeles nonprofit giving young people the skills, exposure, and support they need to build the futures they deserve.</p>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div class="reveal prose">
      <span class="eyebrow">Our story</span>
      <h2 style="color:var(--plum)">Eighty years of community service, carried forward.</h2>
      <p class="lead">Team Uplift Coalition, Inc. is a nonprofit organization dedicated to empowering youth in Los Angeles with the skills, exposure, and support they need to thrive.</p>
      <p>We are proud to partner with <strong>Lambda Omicron Chapter of Omega Psi Phi Fraternity, Inc.</strong>, chartered in 1946 and one of the fraternity&rsquo;s founding chapters in the 12th District, bringing eight decades of community service experience in South Los Angeles to our mission.</p>
      <a class="text-link" href="https://www.lambdaomicronques.com/" target="_blank" rel="noopener">Learn more about our partner chapter</a>
    </div>
    <div class="split-media reveal">
      <img src="/assets/img/team-gala.jpg" alt="Members of Team Uplift and Lambda Omicron Chapter at a community gala" width="1800" height="1200" loading="lazy">
      <span class="tag">Chartered 1946</span>
    </div>
  </div>
</section>

<section class="section bg-cream">
  <div class="wrap">
    <div class="section-head reveal">
      <div>
        <span class="eyebrow">Our foundation</span>
        <h2>Four principles. One legacy.</h2>
      </div>
      <p class="lead">Rooted in Omega Psi Phi&rsquo;s founding principles, we carry that legacy forward through direct investment in the young people and families of our community.</p>
    </div>
    <div class="principles">{principles}</div>
  </div>
</section>

<section class="section">
  <div class="wrap split split--flip">
    <div class="split-media reveal">
      <img src="/assets/img/wellness-crenshaw-ymca.jpg" alt="Young men and mentors gathered in a circle at the Crenshaw YMCA" width="1132" height="1183" loading="lazy">
    </div>
    <div class="reveal prose">
      <span class="eyebrow">Our mission</span>
      <h2 style="color:var(--plum)">Holistic development for every young person.</h2>
      <p class="lead">We work to empower youth in Los Angeles with life skills, exposure to diverse career paths, and comprehensive STEM education.</p>
      <p>We foster holistic development in mental, spiritual, and physical well-being, all while promoting financial literacy, so that a young person&rsquo;s potential is never limited by their circumstances.</p>
      <a class="btn" href="/what-we-do/" style="margin-top:12px">Explore our programs {I['arrow']}</a>
    </div>
  </div>
</section>

{cta('Be part of the <span class="accent">legacy.</span>', 'Volunteer, partner, sponsor, or donate. There are many ways to support our mission.', ("/get-involved/", "Ways to get involved"), ("/contact/", "Contact us"))}
"""
page("who-we-are", "Who We Are", "Team Uplift Coalition, Inc. is a Los Angeles nonprofit empowering youth in partnership with Lambda Omicron Chapter of Omega Psi Phi Fraternity, Inc.", who)

# ---------------- WHAT WE DO ----------------
def prog(n, anchor, icon, title, body):
    return f"""
    <article class="program" id="{anchor}">
      <div class="program-head reveal">
        <span class="icon">{I[icon]}</span>
        <span class="count">{n:02d} / 06</span>
        <h2>{title}</h2>
      </div>
      <div class="program-body prose reveal">{body}</div>
    </article>"""

programs = "".join([
 prog(1, "mentorship", "mentor", "Youth Mentorship &amp; Scholarship", """
        <img src="/assets/img/youth-bike-workshop.jpg" alt="Youth and mentors at a community bike repair workshop" width="1800" height="1350" loading="lazy">
        <p class="lead">We connect young people, with a focus on Black men and boys, to mentors who invest in their growth and help them see what&rsquo;s possible for their future.</p>
        <p>Our scholarship support helps remove financial barriers to higher education, so a student&rsquo;s potential is never limited by their circumstances. Mentorship pairs guidance with real relationships, built over time, that follow young people well beyond a single program or event.</p>"""),
 prog(2, "health", "health", "Health &amp; Wellness", """
        <img src="/assets/img/bulldog-run.jpg" alt="Runners with medals at The Bulldog Run 5K" width="1800" height="1200" loading="lazy">
        <p class="lead">We promote physical, mental, and spiritual well-being as the foundation for everything else a young person builds in life.</p>
        <p>This includes our annual <strong>Bulldog Run at Kenneth Hahn State Recreation Area</strong>, along with programming that supports healthy habits and gives young people tools to manage stress, build resilience, and take care of themselves and each other.</p>"""),
 prog(3, "service", "home", "Neighborhood Service", """
        <p class="lead">We invest directly in the physical health of our community through initiatives like our <strong>Crenshaw Community Clean Up</strong>, keeping the neighborhoods we serve safe, clean, and cared for.</p>
        <p>Service work like this builds pride of place and shows young people what it looks like to show up for your community.</p>"""),
 prog(4, "civic", "vote", "Civic Engagement", """
        <p class="lead">We believe civic participation is one of the most powerful tools a community has, and we work to make it accessible to everyone.</p>
        <p>Each October at <strong>Taste of Soul</strong>, our team runs a voter registration and civic engagement booth on Crenshaw Boulevard, reaching thousands of Los Angeles residents. We help people register to vote, confirm their registration, and understand what&rsquo;s actually on their ballot, since many of the offices that most directly affect housing, schools, and local services are the ones voters know the least about. Our approach is nonpartisan: we don&rsquo;t tell anyone how to vote, only that their vote matters and how to use it.</p>
        <p>Civic engagement doesn&rsquo;t end on Election Day for us. We stay connected with our community in the weeks after registration, sharing reminders about ballot deadlines and drop box locations so that registering to vote turns into a vote that&rsquo;s actually cast.</p>
        <ul class="checklist">
          <li>Registration by QR code, staffed tablet, or paper form, so no one is turned away</li>
          <li>Materials provided in English and Spanish</li>
          <li>Team members walk people through every step</li>
          <li>Follow-up reminders on ballot deadlines and drop box locations</li>
        </ul>"""),
 prog(5, "stem", "stem", "STEM Education &amp; Career Exposure", """
        <p class="lead">We introduce young people to hands-on STEM learning and diverse career paths they might not otherwise encounter.</p>
        <p>By opening doors to new fields and the people who work in them, we help young people see a wider range of futures available to them.</p>"""),
 prog(6, "financial-literacy", "money", "Financial Literacy", """
        <p class="lead">We equip youth with practical financial knowledge, from budgeting to long-term planning, so they can build a stable and independent future.</p>"""),
])
chips = "".join(f'<a href="#{a}">{t}</a>' for a, _, t, _ in PROGRAMS)
what = f"""
<section class="page-hero">
  <div class="wrap">
    <span class="eyebrow">What we do</span>
    <h1>Programs that <span class="accent">inspire, educate &amp; empower.</span></h1>
    <p class="lead">Six program areas working together to support the whole young person and the community around them.</p>
    <nav class="program-nav" aria-label="Programs">{chips}</nav>
  </div>
</section>

<section class="section" style="padding-top:clamp(24px,4vw,48px)">
  <div class="wrap">{programs}
  </div>
</section>

{cta('Help us reach <span class="accent">more young people.</span>', 'Every program is powered by volunteers, partners, sponsors, and donors who believe in LA&rsquo;s youth.')}
"""
page("what-we-do", "What We Do", "Youth mentorship and scholarship, health and wellness, neighborhood service, civic engagement, STEM education, and financial literacy programs in Los Angeles.", what)

# ---------------- GET INVOLVED ----------------
involved = f"""
<section class="page-hero">
  <div class="wrap">
    <span class="eyebrow">Get involved</span>
    <h1>There are many ways to <span class="accent">lift others up.</span></h1>
    <p class="lead">Whether you have an hour, a skill, a business, or a gift to share, there&rsquo;s a place for you on Team Uplift.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="ways">
      <div class="way reveal">
        <span class="icon">{I['hands']}</span>
        <h3>Volunteer</h3>
        <p>Volunteer with us at community events and programming throughout the year, from the Bulldog Run to our Taste of Soul civic engagement booth.</p>
        <a class="btn" href="/contact/?interest=volunteer">Sign up to volunteer {I['arrow']}</a>
      </div>
      <div class="way way--feature reveal">
        <span class="icon">{I['gift']}</span>
        <h3>Donate</h3>
        <p>Donate to directly fund youth programming, scholarships, and community initiatives across Los Angeles.</p>
        <a class="btn btn--gold" href="/donate/">Make a donation {I['arrow']}</a>
      </div>
      <div class="way reveal">
        <span class="icon">{I['link']}</span>
        <h3>Partner</h3>
        <p>Partner with us if you&rsquo;re an organization or business interested in collaborating on youth programming.</p>
        <a class="btn" href="/contact/?interest=partner">Start a partnership {I['arrow']}</a>
      </div>
      <div class="way reveal">
        <span class="icon">{I['star']}</span>
        <h3>Sponsor</h3>
        <p>Sponsor one of our signature community events or initiatives and put your name behind the future of LA&rsquo;s youth.</p>
        <a class="btn" href="/contact/?interest=sponsor">Become a sponsor {I['arrow']}</a>
      </div>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap split">
    <div class="split-media reveal">
      <img src="/assets/img/bulldog-run.jpg" alt="Runners with medals at The Bulldog Run 5K" width="1800" height="1200" loading="lazy">
    </div>
    <div class="reveal">
      <span class="eyebrow">Signature events</span>
      <h2>Show up where it matters.</h2>
      <p class="lead">Our events bring neighbors, families, and young people together.</p>
      <ul class="checklist" style="grid-template-columns:1fr">
        <li><strong>The Bulldog Run</strong> &mdash; our annual 5K at Kenneth Hahn State Recreation Area</li>
        <li><strong>Crenshaw Community Clean Up</strong> &mdash; caring for the neighborhoods we serve</li>
        <li><strong>Taste of Soul</strong> &mdash; voter registration and civic engagement each October on Crenshaw Blvd</li>
      </ul>
    </div>
  </div>
</section>

{cta('Questions? <span class="accent">Let&rsquo;s talk.</span>', 'Reach out and a member of our team will help you find the right way to get involved.', ("/contact/", "Contact us"), ("/what-we-do/", "Our programs"))}
"""
page("get-involved", "Get Involved", "Volunteer, donate, partner, or sponsor with Team Uplift Coalition to support youth programming in Los Angeles.", involved)

# ---------------- CONTACT ----------------
contact = f"""
<section class="page-hero">
  <div class="wrap">
    <span class="eyebrow">Contact</span>
    <h1>We&rsquo;d love to <span class="accent">hear from you.</span></h1>
    <p class="lead">Questions, partnership ideas, volunteer interest, or media inquiries &mdash; send us a note and we&rsquo;ll get back to you.</p>
  </div>
</section>

<section class="section">
  <div class="wrap contact-grid">
    <div class="contact-info reveal">
      <span class="eyebrow">Get in touch</span>
      <h2>Reach our team directly.</h2>
      <p class="lead">Prefer email? Contact us any time.</p>
      <ul class="info-list">
        <li><span class="icon">{I['mail']}</span><div><small>General inquiries</small><a href="mailto:info@teamuplift.org">info@teamuplift.org</a></div></li>
        <li><span class="icon">{I['user']}</span><div><small>President &middot; Jerry Jackson Jr.</small><a href="mailto:jerry.jackson@teamuplift.org">jerry.jackson@teamuplift.org</a></div></li>
        <li><span class="icon">{I['link']}</span><div><small>Partner chapter</small><a href="https://www.lambdaomicronques.com/" target="_blank" rel="noopener">lambdaomicronques.com</a></div></li>
        <li><span class="icon">{I['ig']}</span><div><small>Follow along</small><a href="https://www.instagram.com/teamupliftla/" target="_blank" rel="noopener">@teamupliftla</a></div></li>
      </ul>
    </div>

    <div class="form-card reveal">
      <h2>Send us a message</h2>
      <p>Fields marked optional can be left blank.</p>
      <form action="https://formspree.io/f/meaoqpzg" method="POST" data-formspree>
        <input type="hidden" name="_subject" value="New message from teamuplift.org">
        <div class="hp" aria-hidden="true"><label>Leave this empty <input type="text" name="_gotcha" tabindex="-1" autocomplete="off"></label></div>
        <div class="form-grid">
          <div class="field">
            <label for="name">Full name</label>
            <input id="name" name="name" type="text" autocomplete="name" required>
          </div>
          <div class="field">
            <label for="email">Email</label>
            <input id="email" name="email" type="email" autocomplete="email" required>
          </div>
          <div class="field">
            <label for="phone">Phone <span class="opt">(optional)</span></label>
            <input id="phone" name="phone" type="tel" autocomplete="tel">
          </div>
          <div class="field">
            <label for="interest">I&rsquo;m interested in</label>
            <select id="interest" name="interest">
              <option value="General inquiry">General inquiry</option>
              <option value="Volunteer">Volunteering</option>
              <option value="Partner">Partnering</option>
              <option value="Sponsor">Sponsoring an event</option>
              <option value="Donate">Donating</option>
              <option value="Mentorship">Youth mentorship &amp; programs</option>
              <option value="Media">Media inquiry</option>
            </select>
          </div>
          <div class="field">
            <label for="organization">Organization <span class="opt">(optional)</span></label>
            <input id="organization" name="organization" type="text" autocomplete="organization">
          </div>
          <div class="field field--full">
            <label for="message">Message</label>
            <textarea id="message" name="message" required></textarea>
          </div>
        </div>
        <div class="form-foot">
          <small>We respect your privacy and will only use your information to respond to your message.</small>
          <button class="btn" type="submit">Send message {I['arrow']}</button>
        </div>
        <div class="form-status" role="status" aria-live="polite"></div>
      </form>
    </div>
  </div>
</section>
"""
page("contact", "Contact", "Contact Team Uplift Coalition about volunteering, partnerships, sponsorships, donations, or youth programs in Los Angeles.", contact)

# ---------------- DONATE ----------------
donate = f"""
<section class="page-hero">
  <div class="wrap">
    <span class="eyebrow">Donate</span>
    <h1>Invest in the <span class="accent">leaders of tomorrow.</span></h1>
    <p class="lead">Your gift directly funds youth programming, scholarships, and community initiatives across Los Angeles.</p>
  </div>
</section>

<section class="section">
  <div class="wrap donate-grid">
    <div class="reveal">
      <span class="eyebrow">Your impact</span>
      <h2 style="color:var(--plum)">Where your support goes.</h2>
      <p class="lead">Every dollar helps ensure a young person&rsquo;s potential is never limited by their circumstances.</p>
      <ul class="impact-list">
        <li><span class="icon">{I['mentor']}</span><div><h3>Scholarships</h3><p>Removing financial barriers to higher education for students in our community.</p></div></li>
        <li><span class="icon">{I['hands']}</span><div><h3>Mentorship</h3><p>Connecting young people, with a focus on Black men and boys, to mentors who invest in their growth.</p></div></li>
        <li><span class="icon">{I['health']}</span><div><h3>Health &amp; Wellness</h3><p>Programming and events like the Bulldog Run that build healthy habits and resilience.</p></div></li>
        <li><span class="icon">{I['stem']}</span><div><h3>STEM &amp; Financial Literacy</h3><p>Hands-on learning, career exposure, and practical money skills for a stable future.</p></div></li>
        <li><span class="icon">{I['vote']}</span><div><h3>Community &amp; Civic Initiatives</h3><p>Neighborhood clean ups and nonpartisan voter registration and education.</p></div></li>
      </ul>
    </div>
    <aside class="donate-card reveal" aria-labelledby="give-title">
      <span class="soon-badge">Coming soon</span>
      <h2 id="give-title">Online giving is on its way</h2>
      <p>We&rsquo;re setting up a secure way to donate online. Check back soon.</p>
      <p>In the meantime, reach out and our team will help you make a gift.</p>
      <a class="btn" href="/contact/?interest=donate">Contact us to give {I['arrow']}</a>
      <hr style="border:0;border-top:1px solid var(--line);margin:26px 0">
      <p style="margin:0;font-size:.95rem">Interested in a sponsorship or corporate gift? <a class="text-link" href="/contact/?interest=sponsor">Contact our team</a>.</p>
    </aside>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="partner reveal">
      <div class="partner-media"><img src="/assets/img/youth-bike-workshop.jpg" alt="Youth and volunteers at a community bike workshop" width="1800" height="1350" loading="lazy"></div>
      <div class="partner-body">
        <span class="eyebrow">One young person at a time</span>
        <h2>Building a stronger, more connected community.</h2>
        <p>Team Uplift Coalition, Inc. is a Los Angeles nonprofit working in partnership with Lambda Omicron Chapter of Omega Psi Phi Fraternity, Inc. to empower youth through mentorship, scholarship, health and wellness, neighborhood service, and civic engagement.</p>
        <a class="btn btn--ghost" href="/what-we-do/">See our programs {I['arrow']}</a>
      </div>
    </div>
  </div>
</section>
"""
page("donate", "Donate", "Donate to Team Uplift Coalition to fund youth programming, scholarships, and community initiatives in Los Angeles.", donate)

# ---------------- DUES (Members) ----------------
ZEFFY_EMBED = """<div>
  <div data-zeffy-embed data-form-url="/embed/ticketing/membership-dues-90"></div>
  <div data-zeffy-embed-fallback style="display:none;">
    <div style="position:relative;overflow:hidden;height:450px;width:100%;padding-top:450px;"><iframe title='Donation form powered by Zeffy' style='position: absolute; border: 0; top:0;left:0;bottom:0;right:0;width:100%;height:100%' data-zeffy-embed-src='https://www.zeffy.com/embed/ticketing/membership-dues-90' allowpaymentrequest allowTransparency="true"></iframe></div>
  </div>
  <script
    src="https://www.zeffy.com/embed/v2/zeffy-embed.js"
    onerror="document.querySelectorAll('[data-zeffy-embed-fallback]').forEach(function(el){el.style.display='block';el.querySelectorAll('iframe[data-zeffy-embed-src]').forEach(function(f){f.src=f.getAttribute('data-zeffy-embed-src');});});">
  </script>
</div>"""

dues = f"""
<section class="page-hero">
  <div class="wrap">
    <span class="eyebrow">Members</span>
    <h1>Membership <span class="accent">dues.</span></h1>
    <p class="lead">Members can pay their annual dues securely online below. Thank you for supporting the work of Team Uplift.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="dues-card">
      {ZEFFY_EMBED}
    </div>
    <p class="dues-help">Questions about your dues or membership? Email <a class="text-link" href="mailto:info@teamuplift.org">info@teamuplift.org</a>.</p>
  </div>
</section>
"""
page("dues", "Member Dues", "Pay Team Uplift Coalition membership dues securely online.", dues)

# ---------------- 404 ----------------
nf = f"""
<section class="page-hero" style="min-height:60vh;display:flex;align-items:center">
  <div class="wrap">
    <span class="eyebrow">404</span>
    <h1>This page took a <span class="accent">wrong turn.</span></h1>
    <p class="lead" style="margin-bottom:32px">The page you&rsquo;re looking for doesn&rsquo;t exist or has moved.</p>
    <div class="btn-row"><a class="btn btn--gold" href="/">Back to home {I['arrow']}</a><a class="btn btn--ghost-light" href="/contact/">Contact us</a></div>
  </div>
</section>
"""
page("404tmp", "Page Not Found", "Page not found.", nf, absolute=True)
os.replace(os.path.join(ROOT, "404tmp", "index.html"), os.path.join(ROOT, "404.html"))
os.rmdir(os.path.join(ROOT, "404tmp"))
nf_path = os.path.join(ROOT, "404.html")
nf_html = open(nf_path).read().replace('<link rel="canonical" href="https://teamuplift.org/404tmp/">\n', '').replace("/404tmp/", "/")
open(nf_path, "w").write(nf_html)

with open(os.path.join(ROOT, "robots.txt"), "w") as f:
    f.write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
urls = ["", "who-we-are/", "what-we-do/", "get-involved/", "contact/", "donate/"]
with open(os.path.join(ROOT, "sitemap.xml"), "w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
            "".join(f"  <url><loc>{SITE}/{u}</loc></url>\n" for u in urls) + "</urlset>\n")
print("built")

import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Remove the weak gradient overlay
css_before_old = """    .portfolio-card::before {
      content: '';
      position: absolute;
      inset: 0;
      background: linear-gradient(to top, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0.2) 50%, transparent 100%);
      z-index: 1;
      pointer-events: none;
    }"""

content = content.replace(css_before_old, """    /* Removed weak gradient overlay */""")

# 2. Update .portfolio-meta-top span (we need to target the span specifically, let's just add it)
css_meta_old = """    .portfolio-meta-top {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.025em;
      color: rgba(255, 255, 255, 0.45);
      position: relative;
      z-index: 2;
    }"""

css_meta_new = """    .portfolio-meta-top {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.025em;
      position: relative;
      z-index: 2;
    }

    .portfolio-meta-top > span {
      background: rgba(10, 10, 10, 0.65);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      color: #fff;
      padding: 0.4rem 0.8rem;
      border-radius: 2rem;
      font-weight: 600;
      border: 1px solid rgba(255, 255, 255, 0.1);
    }"""

content = content.replace(css_meta_old, css_meta_new)

# 3. Update badge for glass effect
css_badge_old = """    .portfolio-badge {
      width: 2.75rem;
      height: 2.75rem;
      display: grid;
      place-items: center;
      border-radius: var(--radius-pill);
      background: rgba(255, 255, 255, 0.1);
      color: #ffffff;
      border: 1px solid rgba(255, 255, 255, 0.15);
      font-size: 1.125rem;
      transition: transform 0.35s cubic-bezier(0.2, 0.8, 0.2, 1);
    }"""

css_badge_new = """    .portfolio-badge {
      width: 2.75rem;
      height: 2.75rem;
      display: grid;
      place-items: center;
      border-radius: var(--radius-pill);
      background: rgba(10, 10, 10, 0.65);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      color: #ffffff;
      border: 1px solid rgba(255, 255, 255, 0.15);
      font-size: 1.125rem;
      transition: transform 0.35s cubic-bezier(0.2, 0.8, 0.2, 1);
    }"""

content = content.replace(css_badge_old, css_badge_new)

# 4. Glassmorphism for .portfolio-bottom
css_bottom_old = """    .portfolio-bottom {
      position: relative;
      z-index: 2;
    }

    .portfolio-card-title {
      font-size: 1.5rem;
      font-weight: 500;
      margin-bottom: 0.5rem;
      letter-spacing: -0.02em;
    }

    .portfolio-card-desc {
      font-size: 0.875rem;
      color: rgba(255, 255, 255, 0.7);
      line-height: 1.5;
      margin-bottom: 1.5rem;
    }"""

css_bottom_new = """    .portfolio-bottom {
      position: relative;
      z-index: 2;
      background: rgba(10, 10, 10, 0.7);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      padding: 1.5rem;
      border-radius: 1rem;
      border: 1px solid rgba(255, 255, 255, 0.1);
      margin-top: auto;
      transform: translateY(0);
      transition: all 0.4s ease;
    }

    .portfolio-card:hover .portfolio-bottom {
      background: rgba(10, 10, 10, 0.85);
      border-color: rgba(255, 255, 255, 0.2);
    }

    .portfolio-card-title {
      font-family: 'Instrument Serif', serif;
      font-size: 2rem;
      font-weight: 400;
      margin-bottom: 0.5rem;
      letter-spacing: -0.01em;
      line-height: 1.1;
      color: #ffffff;
    }

    .portfolio-card-desc {
      font-size: 0.95rem;
      color: rgba(255, 255, 255, 0.85);
      line-height: 1.6;
      margin-bottom: 1.5rem;
    }"""

content = content.replace(css_bottom_old, css_bottom_new)

# 5. Make tag chips a bit more premium
css_tags_old = """    .tag-chip {
      font-size: 0.6875rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 0.25rem 0.75rem;
      border-radius: var(--radius-pill);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: rgba(255, 255, 255, 0.6);
    }"""

css_tags_new = """    .tag-chip {
      font-size: 0.7rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 0.35rem 0.8rem;
      border-radius: var(--radius-pill);
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.1);
      color: rgba(255, 255, 255, 0.9);
    }"""

content = content.replace(css_tags_old, css_tags_new)

with open('index.html', 'w') as f:
    f.write(content)

print("Updated perfectly.")

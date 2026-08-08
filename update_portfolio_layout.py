import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Update CSS

# Remove old CSS
css_old_card = """    .portfolio-card {
      position: relative;
      min-height: 22rem;
      overflow: hidden;
      border-radius: var(--radius-card);
      background: var(--ink);
      padding: 1.5rem;
      color: #ffffff;
      box-shadow: 0 0 0 1px rgba(255, 255, 255, 0.05);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: transform 0.35s cubic-bezier(0.2, 0.8, 0.2, 1);
    }

    /* Removed weak gradient overlay */

    .portfolio-bg-img {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      opacity: 1;
      z-index: 0;
      transition: transform 0.4s cubic-bezier(0.2, 0.8, 0.2, 1);
    }

    @media (min-width: 640px) {
      .portfolio-card {
        min-height: 26rem;
        padding: 2rem;
      }
    }

    @media (hover: hover) {
      .portfolio-card:hover {
        transform: translateY(-8px) scale(1.012);
      }
      .portfolio-card:hover .portfolio-bg-img {
        transform: scale(1.05);
      }
    }"""

css_new_card = """    .portfolio-card {
      display: flex;
      flex-direction: column;
      gap: 1rem;
      text-decoration: none;
      transition: transform 0.35s cubic-bezier(0.2, 0.8, 0.2, 1);
    }

    .portfolio-image-wrapper {
      position: relative;
      width: 100%;
      aspect-ratio: 4 / 3;
      border-radius: 1.5rem;
      overflow: hidden;
      background: var(--surface);
      border: 1px solid var(--line);
    }

    .portfolio-bg-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: top;
      transition: transform 0.6s cubic-bezier(0.2, 0.8, 0.2, 1);
    }

    @media (hover: hover) {
      .portfolio-card:hover .portfolio-image-wrapper {
        transform: translateY(-4px);
        box-shadow: 0 12px 30px rgba(0,0,0,0.06);
      }
      .portfolio-card:hover .portfolio-bg-img {
        transform: scale(1.05);
      }
    }"""

content = content.replace(css_old_card, css_new_card)

css_meta_old = """    .portfolio-meta-top {
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

css_meta_new = """    .portfolio-meta-top {
      position: absolute;
      top: 1rem;
      left: 1rem;
      right: 1rem;
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      z-index: 2;
    }

    .portfolio-meta-top > span {
      background: rgba(10, 10, 10, 0.65);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      color: #fff;
      padding: 0.35rem 0.8rem;
      border-radius: 2rem;
      font-weight: 600;
      font-size: 0.7rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      border: 1px solid rgba(255, 255, 255, 0.1);
    }"""

content = content.replace(css_meta_old, css_meta_new)

# Badge css
css_badge_old = """    .portfolio-badge {
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

css_badge_new = """    .portfolio-badge {
      width: 2.5rem;
      height: 2.5rem;
      display: grid;
      place-items: center;
      border-radius: var(--radius-pill);
      background: rgba(10, 10, 10, 0.65);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      color: #ffffff;
      border: 1px solid rgba(255, 255, 255, 0.15);
      font-size: 1rem;
      transition: transform 0.35s ease, background 0.35s ease, color 0.35s ease;
    }"""
content = content.replace(css_badge_old, css_badge_new)

# Bottom css
css_bottom_old = """    .portfolio-bottom {
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

css_bottom_new = """    .portfolio-bottom {
      display: flex;
      flex-direction: column;
      padding: 0.5rem 0;
    }

    .portfolio-card-title {
      font-family: 'Instrument Serif', serif;
      font-size: 2rem;
      font-weight: 400;
      margin-bottom: 0.5rem;
      letter-spacing: -0.01em;
      line-height: 1.1;
      color: var(--foreground);
    }

    .portfolio-card-desc {
      font-size: 0.95rem;
      color: rgba(17,17,17,0.7);
      line-height: 1.5;
      margin-bottom: 1rem;
    }"""

content = content.replace(css_bottom_old, css_bottom_new)

css_tags_old = """    .tag-chip {
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
    
css_tags_new = """    .tag-chip {
      font-size: 0.7rem;
      font-weight: 500;
      padding: 0.25rem 0.75rem;
      border-radius: 2rem;
      background: var(--surface);
      border: 1px solid var(--line);
      color: var(--muted);
    }"""

content = content.replace(css_tags_old, css_tags_new)

# Update HTML Structure 
# Because the current HTML is exactly:
# <a href="..." class="portfolio-card">
#   <img src="..." class="portfolio-bg-img" />
#   <div class="portfolio-meta-top">
#     <span>...</span>
#     <div class="portfolio-badge"><svg>...</svg></div>
#   </div>
#   <div class="portfolio-bottom" style="position:relative; z-index:2;">
#     <h3 class="portfolio-card-title">...</h3>
#     <p class="portfolio-card-desc">...</p>
#     <div class="portfolio-tags">...</div>
#   </div>
# </a>

# Let's loop and replace.
parts = content.split('<a href=')
new_parts = [parts[0]]

for part in parts[1:]:
    if 'class="portfolio-card"' in part[:part.find('>')]:
        # This is a portfolio card
        img_start = part.find('<img src=')
        img_end = part.find('>', img_start) + 1
        img_tag = part[img_start:img_end]
        
        span_start = part.find('<span>', img_end)
        if span_start == -1: 
             new_parts.append(part)
             continue
        span_end = part.find('</span>', span_start)
        span_text = part[span_start+6:span_end]
        
        svg_start = part.find('<svg', span_end)
        svg_end = part.find('</svg>', svg_start) + 6
        svg_tag = part[svg_start:svg_end]
        
        bottom_start = part.find('<h3 class="portfolio-card-title">', svg_end)
        bottom_end = part.rfind('</a>')
        
        bottom_content = part[bottom_start:bottom_end]
        # Strip out closing div tags at the very end
        bottom_content = re.sub(r'</div>\s*</div>\s*$', '</div>', bottom_content.strip())
        bottom_content = re.sub(r'</div>\s*$', '', bottom_content.strip())
        
        new_inner = f"""
              <div class="portfolio-image-wrapper">
                {img_tag}
                <div class="portfolio-meta-top">
                  <span>{span_text}</span>
                  <div class="portfolio-badge">
                    {svg_tag}
                  </div>
                </div>
              </div>
              <div class="portfolio-bottom">
                {bottom_content.strip()}
              </div>
            """
            
        start_a_end = part.find('>') + 1
        new_part = part[:start_a_end] + "\n" + new_inner + "\n</a>" + part[bottom_end+4:]
        new_parts.append(new_part)
    else:
        new_parts.append(part)

content = '<a href='.join(new_parts)

with open('index.html', 'w') as f:
    f.write(content)

print("Portfolio layout updated successfully!")

import re

with open('index.html', 'r') as f:
    content = f.read()

# Define the sections by their preceding comments or tags
sections = [
    ("home", '    <!-- HERO -->', '    <!-- ABOUT -->'),
    ("about", '    <!-- ABOUT -->', '    <!-- CREATE BAND -->'),
    ("create-band", '    <!-- CREATE BAND -->', '    <!-- TECHNICAL SKILLS -->'),
    ("skills", '    <!-- TECHNICAL SKILLS -->', '    <!-- EXPERIENCE & EDUCATION -->'),
    ("experience", '    <!-- EXPERIENCE & EDUCATION -->', '    <!-- CERTIFICATIONS -->'),
    ("certifications", '    <!-- CERTIFICATIONS -->', '    <!-- FEATURED POSTS -->'),
    ("featured", '    <!-- FEATURED POSTS -->', '    <!-- PORTFOLIO -->'),
    ("works", '    <!-- PORTFOLIO -->', '    <!-- SERVICES / EXPERIENCE -->'),
    ("services", '    <!-- SERVICES / EXPERIENCE -->', '    <!-- STATS -->'),
    ("stats", '    <!-- STATS -->', '    <!-- CINEMATIC VIDEO CALLOUT SECTION (Full Bleed) -->'),
    ("cinematic", '    <!-- CINEMATIC VIDEO CALLOUT SECTION (Full Bleed) -->', '  </main>')
]

extracted = {}
for name, start_marker, end_marker in sections:
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
    if start_idx != -1 and end_idx != -1:
        extracted[name] = content[start_idx:end_idx]
    else:
        print(f"Failed to find {name} section. Start: {start_idx}, End: {end_idx}")

# The new order
new_order = [
    "home",
    "about",
    "create-band",
    "skills",
    "experience",
    "works",          # Projects immediately after Experience
    "services",       # Methodology
    "featured",       # Writing
    "certifications", # Awards/Certs
    "stats",
    "cinematic"
]

if len(extracted) == len(sections):
    print("All sections found. Reordering...")
    
    # Get the header part (everything before HERO)
    header_end = content.find('    <!-- HERO -->')
    new_content = content[:header_end]
    
    # Add sections in new order
    for name in new_order:
        new_content += extracted[name]
        
    # Add the footer part (everything from </main> onwards)
    footer_start = content.find('  </main>')
    new_content += content[footer_start:]
    
    with open('index.html', 'w') as f:
        f.write(new_content)
    print("Reordered successfully!")
else:
    print("Did not extract all sections.")


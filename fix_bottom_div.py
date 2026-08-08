import re
with open('index.html', 'r') as f:
    content = f.read()

# Replace "\n</a>" with "  </div>\n</a>" where it matches the portfolio item structure
# Let's just do it cleanly by finding all occurrences of "</div>\n            \n</a>" 
# Actually it looks like:
#               </div>
#             
# </a>

new_content = re.sub(r'(\s*)</div>(\s*)</a>', r'\1</div>\1</div>\2</a>', content)
# Wait, let's be more specific to portfolio-item
parts = content.split('<a href=')
new_parts = [parts[0]]

for part in parts[1:]:
    if 'class="portfolio-card"' in part[:part.find('>')]:
        # find the last </a> and insert </div> before it
        close_a_idx = part.rfind('</a>')
        new_part = part[:close_a_idx] + "  </div>\n" + part[close_a_idx:]
        new_parts.append(new_part)
    else:
        new_parts.append(part)

content = '<a href='.join(new_parts)

with open('index.html', 'w') as f:
    f.write(content)
print("Added missing div")

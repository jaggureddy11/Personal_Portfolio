import re

with open('index.html', 'r') as f:
    content = f.read()

# Find the portfolio grid list
grid_start = content.find('<ul class="portfolio-grid">')
grid_end = content.find('</ul>', grid_start)

grid_content = content[grid_start:grid_end]

# Extract all portfolio items
# Each item starts with <li class="portfolio-item" and ends with </li>
items = []
current_idx = 0
while True:
    start_idx = grid_content.find('<li class="portfolio-item"', current_idx)
    if start_idx == -1:
        break
    # Find matching </li>
    end_idx = grid_content.find('</li>', start_idx) + 5
    item_html = grid_content[start_idx:end_idx]
    
    # Extract the title to identify the item
    title_match = re.search(r'<h3 class="portfolio-card-title">([^<]+)</h3>', item_html)
    title = title_match.group(1).strip() if title_match else "Unknown"
    
    items.append({"title": title, "html": item_html})
    current_idx = end_idx

# Desired order:
# 1. ShopHere
# 2. CapMap
# 3. GitHub Profile Health Auditor
# 4. Code Vault
# 5. Claude Token Counter
# 6. MeasureCraft

target_order = [
    "ShopHere",
    "CapMap",
    "GitHub Profile Health Auditor",
    "Code Vault",
    "Claude Token Counter",
    "MeasureCraft"
]

reordered_items = []
for target_title in target_order:
    for item in items:
        if item["title"] == target_title:
            reordered_items.append(item)
            break

# Add the rest that are not in target_order
for item in items:
    if item["title"] not in target_order:
        reordered_items.append(item)

# Rebuild the grid content
new_grid_content = '<ul class="portfolio-grid">\n'
for item in reordered_items:
    new_grid_content += item["html"] + "\n"

# Replace the old grid content
new_content = content[:grid_start] + new_grid_content + content[grid_end:]

with open('index.html', 'w') as f:
    f.write(new_content)

print("Portfolio projects reordered successfully!")

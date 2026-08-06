import re

with open('index.html', 'r') as f:
    content = f.read()

# Find the portfolio grid list items
start_tag = '<ul class="portfolio-grid">'
end_tag = '</ul>\n      </div>'

start_idx = content.find(start_tag) + len(start_tag)
end_idx = content.find(end_tag)

ul_content = content[start_idx:end_idx]

# Split by <li class="portfolio-item">
items = ul_content.split('<li class="portfolio-item">')
# the first item is whitespace
items = items[1:]

projects = {}
for item in items:
    # get the title
    title_match = re.search(r'<h3 class="portfolio-card-title">(.*?)</h3>', item)
    if title_match:
        title = title_match.group(1)
        projects[title] = '<li class="portfolio-item">' + item
    else:
        print("Title not found for an item")

# Order by impact
order = [
    "Enterprise Workflow",
    "IT Ticket Router",
    "EchoVision",
    "MeasureCraft",
    "CapMap",
    "GitHub Profile Health Auditor",
    "Code Vault",
    "Claude Token Counter",
    "StayOnTrack",
    "ShopHere"
]

new_ul_content = "\n".join([projects[title] for title in order if title in projects])

new_content = content[:start_idx] + "\n" + new_ul_content + content[end_idx:]

with open('index.html', 'w') as f:
    f.write(new_content)

print("Reordered successfully!")

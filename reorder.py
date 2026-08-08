with open('index.html', 'r') as f:
    lines = f.readlines()

# Find Methodology section bounds
methodology_start = -1
methodology_end = -1
for i, line in enumerate(lines):
    if '<!-- SERVICES / EXPERIENCE -->' in line:
        methodology_start = i
    if methodology_start != -1 and '</section>' in line and i > methodology_start:
        methodology_end = i
        break

print(f"Methodology: {methodology_start} to {methodology_end}")

# Find Certifications section bounds
certifications_start = -1
certifications_end = -1
for i, line in enumerate(lines):
    if '<section id="certifications"' in line:
        # Include the comment above it if it exists
        if i > 0 and '<!--' in lines[i-1] and 'CERTIFICATIONS' in lines[i-1].upper():
            certifications_start = i - 1
        else:
            certifications_start = i
    if certifications_start != -1 and '</section>' in line and i > certifications_start:
        certifications_end = i
        break

print(f"Certifications: {certifications_start} to {certifications_end}")

if methodology_start != -1 and certifications_start != -1:
    methodology_lines = lines[methodology_start:methodology_end+1]
    
    # Remove methodology from its current position
    # But wait, if methodology is BEFORE certifications, removing it shifts the certification indices.
    
    new_lines = []
    i = 0
    while i < len(lines):
        if i == methodology_start:
            i = methodology_end + 1
            continue
        new_lines.append(lines[i])
        if i == certifications_end:
            # Insert methodology right after the certifications section ends
            # We add a blank line for spacing
            new_lines.append('\n')
            new_lines.extend(methodology_lines)
            new_lines.append('\n')
        i += 1
        
    with open('index.html', 'w') as f:
        f.writelines(new_lines)
    print("Reordered successfully!")
else:
    print("Could not find sections.")

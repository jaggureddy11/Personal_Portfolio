with open('index.html', 'r') as f:
    lines = f.readlines()

def find_section(comment_str):
    start = -1
    end = -1
    for i, line in enumerate(lines):
        if comment_str in line:
            start = i
            break
    if start != -1:
        for i in range(start + 1, len(lines)):
            if '</section>' in lines[i]:
                end = i
                break
    return start, end

cert_start, cert_end = find_section('<!-- CERTIFICATIONS -->')
methodology_start, methodology_end = find_section('<!-- SERVICES / EXPERIENCE -->')
featured_start, featured_end = find_section('<!-- FEATURED POSTS -->')

print(f"Cert: {cert_start} to {cert_end}")
print(f"Methodology: {methodology_start} to {methodology_end}")
print(f"Featured: {featured_start} to {featured_end}")

if cert_start != -1 and methodology_start != -1 and featured_start != -1:
    # We want to move Cert and Methodology to be before Featured Posts
    # Since Cert and Methodology are currently AFTER Featured, we can extract them and insert them before Featured
    
    cert_lines = lines[cert_start:cert_end+1]
    methodology_lines = lines[methodology_start:methodology_end+1]
    
    # We should delete them from their original positions
    # Need to be careful about indices, delete from bottom up
    if methodology_start > cert_start:
        del lines[methodology_start:methodology_end+1]
        del lines[cert_start:cert_end+1]
    else:
        del lines[cert_start:cert_end+1]
        del lines[methodology_start:methodology_end+1]
        
    # Re-find featured_start since indices might have changed (actually they shouldn't if featured is before them)
    # But just in case, let's re-find it
    featured_start, _ = find_section('<!-- FEATURED POSTS -->')
    
    # Insert Cert and Methodology before Featured
    lines.insert(featured_start, '\n')
    lines = lines[:featured_start] + cert_lines + ['\n'] + methodology_lines + lines[featured_start:]
    
    with open('index.html', 'w') as f:
        f.writelines(lines)
    print("Reordered successfully!")
else:
    print("Could not find all sections.")

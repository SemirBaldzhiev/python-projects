import os

def save_to_file(content, file_path):
    print(file_path)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

html_files = os.listdir("/python-projects/web-view")
html_file_names = [file_name.split(".")[0] for file_name in html_files]

for dir in os.listdir("/python-projects"):
    full_dir_path = f"/python-projects/{dir}"
    
    if os.path.isdir(full_dir_path) and not dir.startswith(".") and dir not in ["scripts", "web-view"]:
        if dir not in html_file_names:
            file = f"/python-projects/web-view/{dir}.html"
            template = f"""<!DOCTYPE html>
<html>
<head>
    <title>{dir}</title>
    <style>
        .back-btn {{ padding: 10px 20px; background: #333; color: white; text-decoration: none; font-family: sans-serif; border-radius: 5px; }}
        .back-btn:hover {{ background: #555; }}
    </style>
</head>
<body style="text-align: center; font-family: sans-serif;">

    <h1>{dir}</h1>
    
    <p><a href="index.html" class="back-btn">← Back to Menu</a></p>
    <br>
    <iframe src="https://trinket.io/embed/python3/id/?outputOnly=true&runOption=run&start=result" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
</body>
</html>"""
            save_to_file(content=template, file_path=file)
            print(f"File {file} created successfuly!")
        
    
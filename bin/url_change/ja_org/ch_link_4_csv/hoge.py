from pathlib import Path

for path in Path(".").rglob("index.md"):
    url = "/" + str(path.parent).replace("\\", "/") + "/"
    print(path, url)

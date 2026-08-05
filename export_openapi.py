import json

from main import app

with open("openapi-export.json", "w", encoding="utf-8") as f:
    json.dump(
        app.openapi(),
        f,
        indent=2
    )

print("OpenAPI exported")
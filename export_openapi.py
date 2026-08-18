"""
Export the FastAPI OpenAPI schema to openapi-export.json.

Generates directly from the app object — no network call needed.
Run from the project root:  python export_openapi.py
"""
import json
import sys

try:
    from main import app
except Exception as e:
    print(f"ERROR: Could not import app — {e}")
    print("Make sure you are running this from the project root.")
    sys.exit(1)

schema = app.openapi()

# Basic sanity check — must have openapi, info, and paths keys
required_keys = {"openapi", "info", "paths"}
missing = required_keys - schema.keys()
if missing:
    print(f"ERROR: Generated schema is missing required keys: {missing}")
    sys.exit(1)

if not schema.get("paths"):
    print("ERROR: Schema has no paths — something is wrong with the app.")
    sys.exit(1)

output_file = "openapi-export.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(schema, f, indent=2)

print(f"OpenAPI schema exported to {output_file}")
print(f"  openapi version : {schema.get('openapi')}")
print(f"  title           : {schema.get('info', {}).get('title')}")
print(f"  paths           : {list(schema['paths'].keys())}")

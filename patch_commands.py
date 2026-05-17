import yaml
import json
import sys
from pathlib import Path

# Paths
commands_path = Path('commands.yml')
patch_path = Path('patch.json')


# Read commands.yml as YAML
with commands_path.open('r') as f:
    commands = yaml.safe_load(f)

# Load or create patch.json
if patch_path.exists():
    with patch_path.open('r') as f:
        patch = json.load(f)
else:
    patch = {"patches": []}


# Build $set ops for each top-level key
ops = []
for key, value in commands.items():
    ops.append({
        "$set": {
            "path": f"$.{key}",
            "value": value
        }
    })

# Add/replace patch for /data/commands.yml
patch_op = {
    "file": "/data/commands.yml",
    "ops": ops
}

# Remove any existing patch for /data/commands.yml
patch["patches"] = [p for p in patch.get("patches", []) if p.get("file") != "/data/commands.yml"]
patch["patches"].append(patch_op)

# Write back to patch.json
with patch_path.open('w') as f:
    json.dump(patch, f, indent=2)

print("Patched patch.json")

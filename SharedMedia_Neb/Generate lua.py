from pathlib import Path

ADDON_NAME = "SharedMedia_Neb"
SOUNDS_DIR = Path("sounds")
OUTPUT_FILE = "RegisterSounds.lua"

HEADER = '''local LSM = LibStub("LibSharedMedia-3.0")

local mediaPath = "Interface\\\\AddOns\\\\SharedMedia_Neb\\\\sounds\\\\"

'''

lines = [HEADER]

for file in sorted(SOUNDS_DIR.rglob("*.ogg")):
    relative = file.relative_to(SOUNDS_DIR)

    filename = file.stem

    pretty_name = (
        filename
        .replace("_", " ")
        .replace("-", " ")
        .title()
    )

    display_name = f"Neb - {pretty_name}"

    lua_path = str(relative).replace("/", "\\\\")

    line = f'LSM:Register("sound", "{display_name}", mediaPath .. "{lua_path}")'
    lines.append(line)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Generated {OUTPUT_FILE}")
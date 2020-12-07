import re

lines = []
passports_str = []
passports = []

with open("input.txt", "r") as f:
    lines = f.readlines()

buffer = ""

for item in lines:
    if not item.startswith("\n"):
        buffer = buffer + " " + item.strip()
    else:
        passports_str.append(buffer.strip())
        buffer = ""

for p in passports_str:
    res = dict(map(str.strip, sub.split(':', 1))
               for sub in p.split(' ') if ':' in sub)
    passports.append(res)


def has_valid_fields(p: dict) -> bool:
    required = ["byr", "iyr", "eyr", "hgt",
                "hcl", "ecl", "pid"]  # cid field optional
    satisfy = True

    for constraint in required:
        if constraint not in i:
            satisfy = False

    return satisfy


def is_valid_passport(p: dict) -> bool:
    if not has_valid_fields(p):
        return False

    if not (1920 <= int(p["byr"]) <= 2002 and 2010 <= int(p["iyr"]) <= 2020 and 2020 <= int(p["eyr"]) <= 2030):
        return False

    height = p["hgt"]

    if not re.match(r"^\d+(cm|in)", height):
        return False
    else:
        height_val = int(height[:-2])

        if "cm" in height:
            if not 150 <= int(height_val) <= 193:
                return False
        else:
            if not 59 <= int(height_val) <= 76:
                return False

    if not re.match(r"^#(?:[0-9a-fA-F]{3}){2}$", p["hcl"]):
        return False

    if not re.match(r"^(amb|blu|brn|gry|grn|hzl|oth)$", p["ecl"]):
        return False

    if not re.match(r"^\d{9}$", p["pid"]):
        return False

    return True

# first part


valid = 0

for i in passports:
    if has_valid_fields(i):
        valid += 1


# second part

valid_ver = 0

for i in passports:
    if is_valid_passport(i):
        valid_ver += 1

print(valid, valid_ver)

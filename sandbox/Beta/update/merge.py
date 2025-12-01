import json


f1 = input()
f2 = input()

with open(f1, encoding="utf-8") as base, open(f2, encoding="utf-8") as update_f:
    users = json.load(base)
    updates = json.load(update_f)
    
user_dct = {user["name"]: {k: v for k, v in user.items() if k != "name"} for user in users}

for update in updates: 
    name = update["name"] 
    if name not in user_dct:
        user_dct[name] = {k: v for k, v in update.items() if k != "name"}
    else:
        for k, v in update.items():
            if k != "name":
                if k not in user_dct[name] or str(user_dct[name][k]) < str(v):
                    user_dct[name][k] = v
                    
with open(f1, "w", encoding="utf-8") as base:
    json.dump(user_dct, base, ensure_ascii=False, indent=2)
# users.json
# updates.json

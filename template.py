import json

__NOTES = {}
__CHANGED = set()
__DELETE = set()

def delete_note(name):
    if name in __CHANGED:
        __CHANGED.remove(name)
    __DELETE.add(name)
def get_note(name):
    name = name.lstrip("\\/ ")
    return str(__NOTES[name])
def set_note(name, value):
    name = name.lstrip("\\/ ")
    __NOTES[name] = str(value)
    if name in __DELETE:
        __DELETE.remove(name)
    __CHANGED.add(name)
# ========= BEGIN =========
{}
# ========== END ==========
s = json.dumps({{i: __NOTES[i] for i in __CHANGED}})
d = json.dumps(list(__DELETE))
with open("output.txt", "w") as f:
    f.write(s)
    f.write("\n")
    f.write(d)

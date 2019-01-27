import pobapi

if __name__ == "__main__":
    with open("../resources/import_code.txt") as f:
        code = f.read()
    build = pobapi.from_import_code(code)

    for group in build.skill_groups:
        print(group.enabled)
        print(group.label)
        print(group.active)
        print(group.gems)
    for i in build.items:
        print(i)

from pobapi import api

if __name__ == "__main__":
    with open("../resources/import_code.txt") as f:
        code = f.read()
    build = api.PathOfBuildingAPI.from_import_code(code)

    for it in build.items:
        print(it.text)

# <Build banditCruel banditMerciless banditNormal targetVersion viewMode>
# <Calcs><Input */>
# <Calcs><Section */>
# <Skills defaultGemLevel>
# <Skills defaultGemQuality>
# <Skills sortGemsByDPS>
# <TreeView *>
# <Config><Input */>

import cc_dat_utils
import json
import cc_classes

#Part 3
#Load your custom JSON file
#Convert JSON data to CCLevelPack
#Save converted data to DAT file

def make_cc_level_pack_from_json(json_data):
    levelPack = cc_classes.CCLevelPack()
    
    levels = json_data["levels"]

    for level in levels:
        gameLevel = cc_classes.CCLevel()

        gameLevel.level_number = level["levelNumber"]
        gameLevel.num_chips = level["chipNumber"]
        gameLevel.time = level["time"]
        gameLevel.upper_layer = level["upperLayer"]

        optionalFields = level["optionalFields"]

        for field in optionalFields:
            if field["fieldType"] == 3:
                gameLevel.optional_fields.append(cc_classes.CCMapTitleField(field["mapTitle"]))
            elif field["fieldType"] == 6:
                gameLevel.optional_fields.append(cc_classes.CCEncodedPasswordField(field["encodedPassword"]))
            elif field["fieldType"] == 7:
                gameLevel.optional_fields.append(cc_classes.CCMapHintField(field["hintText"]))
            elif field["fieldType"] == 10:
                monsters = field["monsters"]
                monsterList = list()
                for monster in monsters:
                    monsterList.append(cc_classes.CCCoordinate(monster["monsterXPos"], monster["monsterYPos"]))
                gameLevel.optional_fields.append(cc_classes.CCMonsterMovementField(monsterList))
        
        levelPack.add_level(gameLevel)

    return levelPack

input_json_file = "data/pkhomche_cc1.json"
output_dat_file = "data/pkhomche_cc1.dat"

with open(input_json_file, "r") as reader:
    level_json_data = json.load(reader)
convertToCCLevelPack =  make_cc_level_pack_from_json(level_json_data)
print(convertToCCLevelPack)

cc_dat_utils.write_cc_level_pack_to_dat(convertToCCLevelPack, output_dat_file)
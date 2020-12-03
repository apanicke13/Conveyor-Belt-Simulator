@namespace
class SpriteKind:
    package = SpriteKind.create()
    button = SpriteKind.create()
    errorBin = SpriteKind.create()
    cheerioBin = SpriteKind.create()
    upBin = SpriteKind.create()
    downBin = SpriteKind.create()
    sideBin = SpriteKind.create()
    unknownBin = SpriteKind.create()
# Pause the game, click reset to restart the game and bring back the box

def on_b_pressed():
    global pause2
    pause2 = not (pause2)
    if True:
        box.set_velocity(0, 0)
        box.set_flag(SpriteFlag.GHOST, True)
        box.set_flag(SpriteFlag.INVISIBLE, True)
    else:
        box.set_flag(SpriteFlag.GHOST, False)
        box.set_flag(SpriteFlag.INVISIBLE, False)
        resetBox()
    scene.camera_follow_sprite(monkey)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

# Reset to initial conditions with new box and parameters for type and dimensions
def resetBox():
    global _type, boxLength, boxWidth, boxHeight, objectMaterial, objectWeight, orientation
    _type = randint(0, 2)
    if _type == 0:
        boxLength = 10
        boxWidth = 10
        boxHeight = 30
        objectMaterial = "Rubber"
        objectWeight = 1
    elif _type == 1:
        boxLength = 20
        boxWidth = 20
        boxHeight = 20
        orientation = randint(0, 1)
        objectMaterial = "Porcelain"
        objectWeight = 0.2
    else:
        boxLength = randint(10, 20)
        boxWidth = randint(10, 20)
        boxHeight = randint(10, 30)
        objectMaterial = "Unknown"
        objectWeight = randint(0, 2)
    print(_type)
    pinkButton.set_flag(SpriteFlag.GHOST, False)
    blueButton.set_flag(SpriteFlag.GHOST, False)
    box.set_flag(SpriteFlag.INVISIBLE, True)
    pause(500)
    tiles.place_on_tile(box, tiles.get_tile_location(0, 7))
    box.set_flag(SpriteFlag.INVISIBLE, False)
    pause(200)
    box.set_velocity(25, 0)
beforeTurn = 0
height = ""
width = ""
length = ""
weight = ""
boxWeight = 0
boxType = 0
onButton2 = 0
onButton1 = 0
orientation = 0
objectWeight = 0
objectMaterial = ""
boxHeight = 0
boxWidth = 0
boxLength = 0
_type = 0
pinkButton: Sprite = None
blueButton: Sprite = None
box: Sprite = None
monkey: Sprite = None
pause2 = False
tiles.set_tilemap(tiles.create_tilemap(hex("""
            1000100004040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040704040404040704040404040404080105010901090106010901030404040404040402040204040402040404040404040404030403040404030404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
        """),
        [myTiles.transparency16,
            sprites.vehicle.road_horizontal,
            sprites.vehicle.road_vertical,
            sprites.dungeon.chest_closed,
            sprites.dungeon.floor_light2,
            sprites.dungeon.button_pink,
            sprites.dungeon.button_teal,
            myTiles.tile1,
            sprites.dungeon.chest_open,
            myTiles.tile2],
        TileScale.SIXTEEN))
pause2 = False
monkey = sprites.create(img("""
        ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ............fffff...............
            ...........feeeeef..............
            ..........fddddeeef.............
            .........cdfddfdeeff............
            .........cdfddfdeeddf...........
            ........cdeeddddeebdc...........
            ........cddddcddeebdc...........
            ........cccccddeeefc............
            .........fddddeeeff.............
            ..........fffffeeeef............
            ............ffeeeeeef.ff........
            ...........feefeefeef.ef........
            ..........feefeefeeef.ef........
            .........fbdfdbfbbfeffef........
            .........fddfddfddbeffff........
            ..........fffffffffffff.........
    """),
    SpriteKind.player)
monkey.set_flag(SpriteFlag.SHOW_PHYSICS, True)
scene.camera_follow_sprite(monkey)
controller.move_sprite(monkey, 100, 100)
tiles.place_on_tile(monkey, tiles.get_tile_location(5, 7))
box = sprites.create(img("""
        f f f f f f f f f f f f f f f f 
            f e e e e e e e e e e e e e e f 
            f e e e e e e e e e e e e e e f 
            f f e e e f f f f f f f f f f f 
            f f f e e e f f e f e e f e e f 
            f e f f e e e f f f e e f e e f 
            f e e f f e e e f f e e f e e f 
            f e e f f f e e e f f e f e e f 
            f e e f e f f e e e f f f e e f 
            f e e f e e f f e e e f f e e f 
            f e e f e e f f f e e e f f e f 
            f e e f e e f e f f e e e f f f 
            f f f f f f f f f f f e e e f f 
            f e e e e e e e e e e e e e e f 
            f e e e e e e e e e e e e e e f 
            f f f f f f f f f f f f f f f f
    """),
    SpriteKind.package)
blueButton = sprites.create(img("""
        . . . . . . . . . . . . . . . b 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.button)
tiles.place_on_tile(blueButton, tiles.get_tile_location(8, 7))
pinkButton = sprites.create(img("""
        . . . . . . . . . . . . . . . b 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.button)
tiles.place_on_tile(pinkButton, tiles.get_tile_location(2, 7))
unknown = sprites.create(img("""
        . . . . . . . . . . . . . . . b 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.unknownBin)
tiles.place_on_tile(unknown, tiles.get_tile_location(4, 9))
cheerio = sprites.create(img("""
        . . . . . . . . . . . . . . . b 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.cheerioBin)
tiles.place_on_tile(cheerio, tiles.get_tile_location(6, 9))
upOrientation = sprites.create(img("""
        . . . . . . . . . . . . . . . b 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.upBin)
tiles.place_on_tile(upOrientation, tiles.get_tile_location(12, 7))
sideOrientation = sprites.create(img("""
        . . . . . . . . . . . . . . . b 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.sideBin)
tiles.place_on_tile(sideOrientation, tiles.get_tile_location(10, 9))
turn1 = sprites.create(img("""
        . . . . . . . . . . . . . . . b 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.button)
tiles.place_on_tile(turn1, tiles.get_tile_location(4, 7))
turn2 = sprites.create(img("""
        . . . . . . . . . . . . . . . b 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.button)
tiles.place_on_tile(turn2, tiles.get_tile_location(6, 7))
turn3 = sprites.create(img("""
        . . . . . . . . . . . . . . . b 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.button)
tiles.place_on_tile(turn3, tiles.get_tile_location(10, 7))
stop1 = sprites.create(img("""
        . . . . . . . . . . . . . . . b 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.button)
tiles.place_on_tile(stop1, tiles.get_tile_location(4, 10))
stop2 = sprites.create(img("""
        . . . . . . . . . . . . . . . b 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.button)
tiles.place_on_tile(stop2, tiles.get_tile_location(6, 10))
stop3 = sprites.create(img("""
        . . . . . . . . . . . . . . . b 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.button)
tiles.place_on_tile(stop3, tiles.get_tile_location(10, 10))
stop4 = sprites.create(img("""
        . . . . . . . . . . . . . . . b 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.button)
tiles.place_on_tile(stop4, tiles.get_tile_location(12, 7))
resetBox()

def on_forever():
    global onButton1, onButton2, boxType, boxWeight, weight, length, width, height, beforeTurn
    if not (box.overlaps_with(pinkButton)) and not (box.overlaps_with(blueButton)):
        onButton1 = 1
        onButton2 = 1
    if box.overlaps_with(pinkButton) and onButton1:
        box.set_velocity(0, 0)
        if objectMaterial == "Rubber":
            boxType = 2
            boxWeight = 1
            weight = convert_to_text(boxWeight)
            length = convert_to_text(boxLength)
            width = convert_to_text(boxWidth)
            height = convert_to_text(boxHeight)
            game.show_long_text("Weight: " + weight + "\\nLength: " + length + "\\nHeight: " + width + "\\nHeight: " + height + "\\nMaterial: " + objectMaterial,
                DialogLayout.TOP)
        elif objectMaterial == "Porcelain":
            boxType = 0
            boxWeight = 0.2
            weight = convert_to_text(boxWeight)
            length = convert_to_text(boxLength)
            width = convert_to_text(boxWidth)
            height = convert_to_text(boxHeight)
            game.show_long_text("Weight: " + weight + "\\nLength: " + length + "\\nHeight: " + width + "\\nHeight: " + height + "\\nMaterial: " + objectMaterial,
                DialogLayout.TOP)
        else:
            boxType = 1
            length = convert_to_text(boxLength)
            width = convert_to_text(boxWidth)
            height = convert_to_text(boxHeight)
            game.show_long_text("Weight: Unknown" + "\\nLength: " + length + "\\nWidth: " + width + "\\nHeight: " + height + "\\nMaterial: Unknown",
                DialogLayout.TOP)
        if controller.A.is_pressed():
            onButton1 = 0
            beforeTurn = 1
            box.set_velocity(25, 0)
    if box.overlaps_with(blueButton) and onButton2:
        box.set_velocity(0, 0)
        if orientation == 0:
            boxType = 0
            game.show_long_text("Orientation: Upright", DialogLayout.TOP)
        else:
            boxType = 3
            game.show_long_text("Orientation: Side", DialogLayout.TOP)
        if controller.A.is_pressed():
            onButton2 = 0
            beforeTurn = 1
            box.set_velocity(25, 0)
    if beforeTurn:
        if boxType == 1 and box.overlaps_with(turn1):
            beforeTurn = 0
            box.set_velocity(0, 25)
        elif boxType == 2 and box.overlaps_with(turn2):
            beforeTurn = 0
            box.set_velocity(0, 25)
        elif boxType == 3 and box.overlaps_with(turn3):
            beforeTurn = 0
            box.set_velocity(0, 25)
        elif boxType == 0:
            beforeTurn = 0
            box.set_velocity(25, 0)
    if box.overlaps_with(stop1) or (box.overlaps_with(stop2) or (box.overlaps_with(stop3) or box.overlaps_with(stop4))):
        box.set_velocity(0, 0)
        resetBox()
forever(on_forever)

namespace SpriteKind {
    export const package = SpriteKind.create()
    export const button = SpriteKind.create()
    export const errorBin = SpriteKind.create()
    export const cheerioBin = SpriteKind.create()
    export const upBin = SpriteKind.create()
    export const downBin = SpriteKind.create()
    export const sideBin = SpriteKind.create()
    export const unknownBin = SpriteKind.create()
}
// Pause the game, click reset to restart the game and bring back the box
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    pause2 = !(pause2)
    if (true) {
        box.setVelocity(0, 0)
        box.setFlag(SpriteFlag.Ghost, true)
        box.setFlag(SpriteFlag.Invisible, true)
    } else {
        box.setFlag(SpriteFlag.Ghost, false)
        box.setFlag(SpriteFlag.Invisible, false)
        resetBox()
    }
    scene.cameraFollowSprite(monkey)
})
// Reset to initial conditions with new box and parameters for type and dimensions
function resetBox () {
    _type = randint(0, 2)
    if (_type == 0) {
        boxLength = 10
        boxWidth = 10
        boxHeight = 30
        objectMaterial = "Rubber"
        objectWeight = 1
    } else if (_type == 1) {
        boxLength = 20
        boxWidth = 20
        boxHeight = 20
        orientation = randint(0, 1)
        objectMaterial = "Porcelain"
        objectWeight = 0.2
    } else {
        boxLength = randint(10, 20)
        boxWidth = randint(10, 20)
        boxHeight = randint(10, 30)
        objectMaterial = "Unknown"
        objectWeight = randint(0, 2)
    }
    console.log(_type)
    pinkButton.setFlag(SpriteFlag.Ghost, false)
    blueButton.setFlag(SpriteFlag.Ghost, false)
    box.setFlag(SpriteFlag.Invisible, true)
    pause(500)
    tiles.placeOnTile(box, tiles.getTileLocation(0, 7))
    box.setFlag(SpriteFlag.Invisible, false)
    pause(200)
    box.setVelocity(25, 0)
}
// Create and place game map and objects
let beforeTurn = 0
let height = ""
let width = ""
let length = ""
let weight = ""
let boxWeight = 0
let boxType = 0
let onButton2 = 0
let onButton1 = 0
let orientation = 0
let objectWeight = 0
let objectMaterial = ""
let boxHeight = 0
let boxWidth = 0
let boxLength = 0
let _type = 0
let pinkButton: Sprite = null
let blueButton: Sprite = null
let box: Sprite = null
let monkey: Sprite = null
let pause2 = false
tiles.setTilemap(tiles.createTilemap(hex`1000100004040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040704040404040704040404040404080105010901090106010901030404040404040402040204040402040404040404040404030403040404030404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404040404`, img`
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
    `, [myTiles.transparency16,sprites.vehicle.roadHorizontal,sprites.vehicle.roadVertical,sprites.dungeon.chestClosed,sprites.dungeon.floorLight2,sprites.dungeon.buttonPink,sprites.dungeon.buttonTeal,myTiles.tile1,sprites.dungeon.chestOpen,myTiles.tile2], TileScale.Sixteen))
pause2 = false
monkey = sprites.create(img`
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
    `, SpriteKind.Player)
monkey.setFlag(SpriteFlag.ShowPhysics, true)
scene.cameraFollowSprite(monkey)
controller.moveSprite(monkey, 100, 100)
tiles.placeOnTile(monkey, tiles.getTileLocation(5, 7))
box = sprites.create(img`
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
    `, SpriteKind.package)
blueButton = sprites.create(img`
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
    `, SpriteKind.button)
tiles.placeOnTile(blueButton, tiles.getTileLocation(8, 7))
pinkButton = sprites.create(img`
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
    `, SpriteKind.button)
tiles.placeOnTile(pinkButton, tiles.getTileLocation(2, 7))
let unknown = sprites.create(img`
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
    `, SpriteKind.unknownBin)
tiles.placeOnTile(unknown, tiles.getTileLocation(4, 9))
let cheerio = sprites.create(img`
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
    `, SpriteKind.cheerioBin)
tiles.placeOnTile(cheerio, tiles.getTileLocation(6, 9))
let upOrientation = sprites.create(img`
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
    `, SpriteKind.upBin)
tiles.placeOnTile(upOrientation, tiles.getTileLocation(12, 7))
let sideOrientation = sprites.create(img`
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
    `, SpriteKind.sideBin)
tiles.placeOnTile(sideOrientation, tiles.getTileLocation(10, 9))
let turn1 = sprites.create(img`
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
    `, SpriteKind.button)
tiles.placeOnTile(turn1, tiles.getTileLocation(4, 7))
let turn2 = sprites.create(img`
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
    `, SpriteKind.button)
tiles.placeOnTile(turn2, tiles.getTileLocation(6, 7))
let turn3 = sprites.create(img`
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
    `, SpriteKind.button)
tiles.placeOnTile(turn3, tiles.getTileLocation(10, 7))
let stop1 = sprites.create(img`
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
    `, SpriteKind.button)
tiles.placeOnTile(stop1, tiles.getTileLocation(4, 10))
let stop2 = sprites.create(img`
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
    `, SpriteKind.button)
tiles.placeOnTile(stop2, tiles.getTileLocation(6, 10))
let stop3 = sprites.create(img`
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
    `, SpriteKind.button)
tiles.placeOnTile(stop3, tiles.getTileLocation(10, 10))
let stop4 = sprites.create(img`
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
    `, SpriteKind.button)
tiles.placeOnTile(stop4, tiles.getTileLocation(12, 7))
resetBox()
forever(function () {
    if (!(box.overlapsWith(pinkButton)) && !(box.overlapsWith(blueButton))) {
        onButton1 = 1
        onButton2 = 1
    }
    if (box.overlapsWith(pinkButton) && onButton1) {
        box.setVelocity(0, 0)
        if (objectMaterial == "Rubber") {
            boxType = 2
            boxWeight = 1
            weight = convertToText(boxWeight)
            length = convertToText(boxLength)
            width = convertToText(boxWidth)
            height = convertToText(boxHeight)
            game.showLongText("Weight: " + weight + "\\nLength: " + length + "\\nHeight: " + width + "\\nHeight: " + height + "\\nMaterial: " + objectMaterial, DialogLayout.Top)
        } else if (objectMaterial == "Porcelain") {
            boxType = 0
            boxWeight = 0.2
            weight = convertToText(boxWeight)
            length = convertToText(boxLength)
            width = convertToText(boxWidth)
            height = convertToText(boxHeight)
            game.showLongText("Weight: " + weight + "\\nLength: " + length + "\\nHeight: " + width + "\\nHeight: " + height + "\\nMaterial: " + objectMaterial, DialogLayout.Top)
        } else {
            boxType = 1
            length = convertToText(boxLength)
            width = convertToText(boxWidth)
            height = convertToText(boxHeight)
            game.showLongText("Weight: Unknown" + "\\nLength: " + length + "\\nWidth: " + width + "\\nHeight: " + height + "\\nMaterial: Unknown", DialogLayout.Top)
        }
        if (controller.A.isPressed()) {
            onButton1 = 0
            beforeTurn = 1
            box.setVelocity(25, 0)
        }
    }
    if (box.overlapsWith(blueButton) && onButton2) {
        box.setVelocity(0, 0)
        if (orientation == 0) {
            boxType = 0
            game.showLongText("Orientation: Upright", DialogLayout.Top)
        } else {
            boxType = 3
            game.showLongText("Orientation: Side", DialogLayout.Top)
        }
        if (controller.A.isPressed()) {
            onButton2 = 0
            beforeTurn = 1
            box.setVelocity(25, 0)
        }
    }
    if (beforeTurn) {
        if (boxType == 1 && box.overlapsWith(turn1)) {
            beforeTurn = 0
            box.setVelocity(0, 25)
        } else if (boxType == 2 && box.overlapsWith(turn2)) {
            beforeTurn = 0
            box.setVelocity(0, 25)
        } else if (boxType == 3 && box.overlapsWith(turn3)) {
            beforeTurn = 0
            box.setVelocity(0, 25)
        } else if (boxType == 0) {
            beforeTurn = 0
            box.setVelocity(25, 0)
        }
    }
    if (box.overlapsWith(stop1) || (box.overlapsWith(stop2) || (box.overlapsWith(stop3) || box.overlapsWith(stop4)))) {
        box.setVelocity(0, 0)
        resetBox()
    }
})

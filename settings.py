import pygame

width  = 480
height = 480

fps = 60

size = 24

color = {
    "page_background":(248, 249, 250),
    "wall":(52, 58, 64),
    "snake":(32, 201, 151),
    "food":(240, 62, 62)
}

page = {
    "home":[
        {
            "img":pygame.image.load("./resources/img/menu/text/play.png"),
            "coordinate":(80,161),
            "size":(135,25)
        },
        {
            "img":pygame.image.load("./resources/img/menu/text/settings.png"),
            "coordinate":(80,220),
            "size":(224,27)
        },
        {
            "img":pygame.image.load("./resources/img/menu/text/exit.png"),
            "coordinate":(80,283),
            "size":(97,25)
        },
        {
            "img":pygame.image.load("./resources/img/menu/component/snake-box.png"),
            "coordinate":(360,40),
            "size":(80,400)
        }
    ],
    "settings":[
        {
            "img":pygame.image.load("./resources/img/menu/text/map.png"),
            "coordinate":(80,158),
            "size":(87,25)
        },
        {
            "img":pygame.image.load("./resources/img/menu/text/speed.png"),
            "coordinate":(80,222),
            "size":(87,25)
        },
        {
            "img":pygame.image.load("./resources/img/menu/text/sound.png"),
            "coordinate":(80,286),
            "size":(160,27)
        },
        {
            "img":pygame.image.load("./resources/img/menu/component/snake-box.png"),
            "coordinate":(360,40),
            "size":(80,400)
        }
    ],
    "map":[
        {
            "img":pygame.image.load("./resources/img/menu/component/select-button.png"),
            "coordinate":(120,289),
            "size":(239,65)
        },
        {
            "img":pygame.image.load("./resources/img/menu/arrow/left.png"),
            "coordinate":(88,156),
            "size":(64,64)
        },
        {
            "img":pygame.image.load("./resources/img/menu/arrow/right.png"),
            "coordinate":(328,156),
            "size":(64,64)
        },
    ],
    "speed":[
        {
            "img":pygame.image.load("./resources/img/menu/component/select-button.png"),
            "coordinate":(120,289),
            "size":(239,65)
        },
        {
            "img":pygame.image.load("./resources/img/menu/arrow/left.png"),
            "coordinate":(95,161),
            "size":(64,64)
        },
        {
            "img":pygame.image.load("./resources/img/menu/arrow/right.png"),
            "coordinate":(321,161),
            "size":(64,64)
        },

    ],
    "sound":[
        {
            "img":pygame.image.load("./resources/img/menu/component/select-button.png"),
            "coordinate":(120,289),
            "size":(239,65)
        },
        {
            "img":pygame.image.load("./resources/img/menu/arrow/left.png"),
            "coordinate":(95,161),
            "size":(64,64)
        },
        {
            "img":pygame.image.load("./resources/img/menu/arrow/right.png"),
            "coordinate":(321,161),
            "size":(64,64)
        }
    ],
    "game":[
        {
            "img":pygame.image.load("./resources/img/menu/background/game-popup.png"),
            "coordinate":(130,180),
            "size":(240,120)
        }
    ]
}

speed_image = [
    {
        "img":pygame.image.load("./resources/img/menu/text/slow.png"),
        "coordinate":(195,182)
    },
    {
        "img":pygame.image.load("./resources/img/menu/text/medium.png"),
        "coordinate":(175,182)
    },
    {
        "img":pygame.image.load("./resources/img/menu/text/fast.png"),
        "coordinate":(200,182)
    },
]

sound_image = [
    {
        "img":pygame.image.load("./resources/img/menu/text/low.png"),
        "coordinate":(204,182)
    },
    {
        "img":pygame.image.load("./resources/img/menu/text/medium.png"),
        "coordinate":(169,182)
    },
    {
        "img":pygame.image.load("./resources/img/menu/text/high.png"),
        "coordinate":(197,182)
    },
]

arrow_info = {
    "img":pygame.image.load("./resources/img/menu/arrow/small.png"),
    "size":(240,120)
}

MAP = {
    0 : [
        "00000000000000000000",
        "0                  0",
        "0                  0",
        "0    P             0",
        "0                  0",
        "0                  0",
        "0                  0",
        "0                  0",
        "0                  0",
        "0                  0",
        "0                  0",
        "0                  0",
        "0                  0",
        "0                  0",
        "0             F    0",
        "0                  0",
        "0                  0",
        "0                  0",
        "0                  0",
        "0                  0",
        "00000000000000000000"
    ],
    1 : [
        "00000000000000000000",
        "0                  0",
        "0                  0",
        "0     P            0",
        "0                  0",
        "0                  0",
        "0                  0",
        "0                  0",
        "0                  0",
        "0        00        0",
        "0        00        0",
        "0                  0",
        "0                  0",
        "0                  0",
        "0              F   0",
        "0                  0",
        "0                  0",
        "0                  0",
        "0                  0",
        "00000000000000000000",
    ]  
} 

map_image = [
    pygame.image.load("./resources/img/menu/map/map-1.png"),
    pygame.image.load("./resources/img/menu/map/map-2.png")
]
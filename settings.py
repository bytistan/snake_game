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
        },
        {
            "img":pygame.image.load("./resources/img/menu/text/settings.png"),
            "coordinate":(80,220)
        },
        {
            "img":pygame.image.load("./resources/img/menu/text/exit.png"),
            "coordinate":(80,283)
        },
        {
            "img":pygame.image.load("./resources/img/menu/component/snake-box.png"),
            "coordinate":(360,40)
        }
    ],
    "settings":[
        {
            "img":pygame.image.load("./resources/img/menu/text/map.png"),
            "coordinate":(80,158)
        },
        {
            "img":pygame.image.load("./resources/img/menu/text/speed.png"),
            "coordinate":(80,222)
        },
        {
            "img":pygame.image.load("./resources/img/menu/text/sound.png"),
            "coordinate":(80,286)
        },
        {
            "img":pygame.image.load("./resources/img/menu/component/snake-box.png"),
            "coordinate":(360,40)
        }
    ],
    "map":[
        {
            "img":pygame.image.load("./resources/img/menu/component/select-button.png"),
            "coordinate":(120,289)
        },
        {
            "img":pygame.image.load("./resources/img/menu/arrow/left.png"),
            "coordinate":(88,156)
        },
        {
            "img":pygame.image.load("./resources/img/menu/arrow/right.png"),
            "coordinate":(328,156)
        },
    ],
    "speed":[
        {
            "img":pygame.image.load("./resources/img/menu/component/select-button.png"),
            "coordinate":(120,289)
        },
        {
            "img":pygame.image.load("./resources/img/menu/arrow/left.png"),
            "coordinate":(95,161)
        },
        {
            "img":pygame.image.load("./resources/img/menu/arrow/right.png"),
            "coordinate":(321,161)
        },

    ],
    "sound":[
        {
            "img":pygame.image.load("./resources/img/menu/component/select-button.png"),
            "coordinate":(120,289)
        },
        {
            "img":pygame.image.load("./resources/img/menu/arrow/left.png"),
            "coordinate":(95,161)
        },
        {
            "img":pygame.image.load("./resources/img/menu/arrow/right.png"),
            "coordinate":(321,161)
        }
    ],
    "pause":[
        {
            "img":pygame.image.load("./resources/img/menu/background/game-popup.png"),
            "coordinate":(130,180)
        },
        {
            "img":pygame.image.load("./resources/img/menu/text/continue.png"),
            "coordinate":(180,212)
        },
        {
            "img":pygame.image.load("./resources/img/menu/text/main-menu.png"),
            "coordinate":(180,250)
        },

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
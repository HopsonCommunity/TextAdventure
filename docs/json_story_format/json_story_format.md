# JSON story format

Story format is a way to describe the story to the engine.
A few files are needed and most of them can be splitted up into multiple ones apart from config and stats file.
Example:

```
./
    config.json
    items/
        weapons.json
        misc.json
    assets/
        mine.json
        canyon.json
        road.json
    scenes/
        mine/
            entrance.json
            big_room.json
        town/
            house.json
    stats.json
```

If there is more than one layer of folders, folder names will be added before a name which is used to access it, for example: `mine_big_room`
All files are written in json format

### [Config](./config.md)

Describes main game setup, for example: game name, description. It also links all other files.

### [Scene](./scene.md)

Defines a scene with all variables, requirements and actions that can be taken inside.

### [Assets](./assets.md)

Links all the assets files e.g. music, backgrounds, fonts.

### [Items](./items.md)

Defines all items in a game, so they can be used in a scene. It provides their name, description

### [Stats](./stats.md)

Defines all player statistics, their max/min value etc. It also describes classes e.g. "murderer"
# Config

A config file is a main file of a story. It configures engine behaviour and links all other files. Inside a file there should be an JSON object with following fields:

## Misc

```json
"misc": {
    "name": "The Wild West",
    "description": "A game about the story of a man who left everything to find an adventure",
    "version": "1.2.1",

    "starting_scene": "train_station"
}
```

`starting_scene` - first scene of the game. Player will appear there
`version` - used in player save fileé

## Meta

```json
"meta": {
    "author" : "me",
    "url" : "me.example.com",
    "email" : "me@example.com"
}
```

## Links

```json
"resources": {
    "items": "./items/",
    "assets": "./assets/",
    "scenes": "./scenes/",

    "stats": "./stats.json"
}
```

Links directories containing appropriate files

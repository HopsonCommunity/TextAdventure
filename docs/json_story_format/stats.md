# Stats
Stats file describes all the player traits and classes. Inside there are two fields: `traits`, `classes`
## Traits
```json
"traits": {
    "shooting": {
        "name": "Shooting",
        "description": "Being a great shooter"
    },

    "courage": {
        "name": "Courage",
        "description": "Ability to do something that frightens one"
    },
}
```

Each trait is an integer which can be changed after taking a specific action. Those values can be later used in conditionals

## Classes
```json
"classes": {
    "revolver-man": {
        "shooting": 20,
        "courage": 10
    },
    "coward": {
        "shooting": 5,
        "courage": 0
    }
}
```

Player chooses a class at the game beginning.
If there is a trait not supplied in a class it will be set to 0.
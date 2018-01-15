# Scene

Scene is a single JSON object that fully describes single scene a.k.a. state.

## Example

```json
"mine_entrance": {
    "name": "Mine entrance",
    "description": "You see a big mine entrance with wooden supports. There is a torch lying on a ground",
    "assets": "mine_entrance",
    "end": false,

    "gotos": [
        {
            "label": "Go inside the mine",
            "scene": "mine",

            "required": {
                "items": {
                    "lighted_torch": 1
                },

                "history": {
                    "talked_with_mine_owner": true
                },

                "stats": {
                    "courage": 10
                }
            },

            "acquired": {
                "history": {
                    "been_in_mine": true
                },

                "stats": {
                    "courage": 20
                }
            }
        },

        {

            "label": "Light a torch",
            "scene": "mine_entrance",

            "required": {
                "items": {
                    "lighted_torch": 0,
                    "torch": 1,
                    "fuel": 1
                }
            },

            "acquired": {
                "items": {
                    "lighted_torch": 1,
                    "torch": -1,
                    "fuel": -1
                }
            }
        },

        {
            "label": "Pick up a torch",
            "scene": "mine_entrance",

            "acquired": {
                "items": {
                    "torch": 1
                }
            }
        },

        {
            "label": "Give up and go back to the village",
            "scene": "village",

            "required": {
                "stats": {
                    "cowardice": 10
                }
            }
        }
    ]
}
```

## Misc data

`name` - name of scene shown to the player
`description` - description of a scene. It should provide everything that story author wants to show to the player
`assets` - links assets from asset file to the scene
`end` - if set to true, entering this scene ends a game. If not supplied it is default false

## Gotos

Gotos are action that player can take inside a scene. There can be multiple and they are stored in `gotos` vector.

`scene` - destination scene. Player goes to this scene after taking this action. When not supplied player ends up in the same room.

If player doesn't meet all of the requirements action will not be shown
Lists of requirements:
`items` - equal or bigger number of items
`history` - equal type and value
`stats` - equal or bigger number

After picking an goto player can acquire:
`history` - overrides a previous value or creates a new field
`items` - adds supplied number to number of owned items
`stats` - adds suplied number to statistic

If the stats used is an antonym, it means to be inferior or equal of the stat. i.e. `"cowardice" : 10` means `courage <= 10`.
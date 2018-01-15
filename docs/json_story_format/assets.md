# Assets
This type of file contains json objects which links all scenery assets
## Example
```json
"mine": {
    "music": "scary.wav",
    "background": "mine.jpg",
    "sprites": [
        {
            "file": "miner.jpg",
            "position": [200, 400],
            "size": 1
        },

        {
            "file": "gold_cart.jpg",
            "position": [700, 400],
            "size": 2
        },
    ]
}
```
 * `music` - played when inside the room. If the last room had the same music it won't start from the beginning
 * `background` - background image showed to the player
 * `sprites` - rendered over the background. Can be used to display characters etc. which are shown in a few different places
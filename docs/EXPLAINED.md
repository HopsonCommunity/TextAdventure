# Engine Explained

The engine follows the logic of text adventures, especially those appearing in form of so called gamebooks around 90s.

The story is built from states, that allow the players some options, each option moving them into further states and potentially having other side-effects (item pickup, stats change, …).

The engine reads those stories from archives called books, that contain the story formatted into a common storage format known as JSON, as well as it's assets. The whole story comes to the player in form of this single book file.

The player is then presented with various states and options as described by the story in the book they loaded.

## More in depth explanation including some special uses useful for creating new stories

![flow](https://imgur.com/ggmYiZS.png)

Diagram describing the flow between different scenes inside the engine.

Each scene has a number of options that user may choose in order to progress to the next or previous scenes.

![dialogue](https://imgur.com/TsTGrXH.png)

This basic concept allows you to not only describe the movement of the player in the physical realm but also to represent dialogue trees and fight scenes.

![item_pickup](https://imgur.com/4WViyOA.png)

This image shows a method of acquiring items using loopbacks to the same scene.

You are in the left state called "Dungeon" and are presented with two choices.

* Pick up sword
* Go left

Upon selecting "Pick up sword", the engine will add the sword to your player and effectively reload the scene.

This time when the scene is presented, the "Pick up sword" option is no longer displayed because it only displays if a condition is met, the condition being: you must have no swords on your person.

The user only has one remaining choice and that is to continue on, as shown in the box on the right side of the diagram.
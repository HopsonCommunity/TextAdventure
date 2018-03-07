# Contributing Guidelines & Contributor Info

Welcome to Contributing Guidelines for Hopson's Community Text Adventure project.

First and foremost, if you consider doing more than few simple edits, please join us at the [Discord Server](https://discord.gg/F6WF7Dm) and request a Community Project role.

Project has several parts as documented in the [README](../README.md). Project is developed in Python 3.

See also [Engine Explained](EXPLAINED.md).

## Programming:

* [Style](https://www.python.org/dev/peps/pep-0008/)
* 4 spaces indentation level
* 2 empty lines before functions
* [Git branching](http://nvie.com/posts/a-successful-git-branching-model/)
* [Git commit messages](https://chris.beams.io/posts/git-commit/)
* In GitHub, fork your own copy of the repo you plan to work on, and use feature branches in the fork to PR back.

### Story Editor:

* [TkInter](https://wiki.python.org/moin/TkInter)?
* [GTK+](http://www.pygtk.org/)?
* [Kivy](https://kivy.org/)?

Select a directory for all assets (music, background, …)

Use placeholder, instead of referring the path, to make future change easier

### Story Engine:

* Data storage
* Interpreting story files
* Inventory       
* Player stats
* State transition / map stuff

**Potential pseudocode of state:** (not final)

```
enter_state: 
    draw bg
    play music
    print title
    print text
    for each opt from options
        if opt.all_requires_ok
            print opt
        else if not opt.hide
            print opt in disable mode
    wait until click on option
        goto option.next_state
```

#### Data:

* Custom format for storing stories ("gamebooks"), common archive (zip?) with custom extension (book?)
* Entry file for each story
* Story define as json file
* Recursively walk the directory and load everything into a single dict.
* Alternatively a single json.

**Example story structure:** (not final)

```
adventure.book (zip archive)
	config.json
	Village
		Townhall
			state1.json
			state2.json
		Bank
			Entrance.json
			Vault.json
```

**Example state code:** (not final, short examples showing specific uses)

```json
"entrance": {
    "text": "You're at the haunted house entrance.",
    "gotos": [
        {"description": "Pick the Key", "state": "entrance", "requirements": {"rusty key": 0}, "acquire": {"rusty key": 1}},
        {"description": "Open the Door", "state": "inside", "requirements": {"rusty key": 1}, "hide": {"rusty key": 1}}
    ]
},
"inside": {
    "text": "The ghosts spook this place.",
    "gotos": […]
}
```

```json
"outside-pub" : {
	"text": "You're outside pub, Jack's sitting on the bench.",
	"gotos": [
		{"description": "Talk to Jack", "state": "introduction-jack", "requirements": {"knows Jack": false}},
		{"description": "Talk to Jack", "state": "chatter-jack", "requirements": {"knows Jack": true}}
	]
},
"introduction-jack": {
    "text": "Hi, I'm Jack, who are you?",
    "gotos": [
        {"description": "Hey, I'm Eremiell!", "state": "chatter-jack", "acquire": {"knows Jack": true}}
    ]
},
"chatter-jack": {
    "text": "How can I help you today?",
    "gotos": [
        {"description": "I need some help with Python", "state": "python-hax-jack"},
        {"description": "Fancy a glass of whiskey?", "state": "whiskey-with-jack"},
        {"description": "Ah, not really. Still nice to see you.", "state": "outside-pub"}
    ]
}
```

[Longer, more complex example](example.json)

### Graphics engine:

* **Graphical library** - [pyglet](https://bitbucket.org/pyglet/pyglet/wiki/Home)

### Programming reference:

* [Python 3](https://docs.python.org/3/)
* [Pyglet](https://pyglet.readthedocs.io/en/pyglet-1.3-maintenance/)
* [PEP-8](https://www.python.org/dev/peps/pep-0008/)
* [PEP-257](https://www.python.org/dev/peps/pep-0257/)
* [JSON](http://json.org/)

### Other:

#### Sounds:

* Play sounds upon entering a state.
* Play sounds when selecting an option.

## Art:

### Visual Art reference:

* [westerando_big](http://games.gameshed.com/westerando_big.jpg)
* [cowboy-with-rifle](https://opengameart.org/content/cowboy-with-rifle)
* [cowboy-with-revolver](https://opengameart.org/content/cowboy-with-revolver)
* [cowboy](https://opengameart.org/content/cowboy)
* [fistful-of-gun](https://gamejolt.com/games/fistful-of-gun/16749)
* [cowboy-game-sprites](https://opengameart.org/content/cowboy-game-sprites)

### Audio Art reference:

* [Ennio Morricone](https://www.youtube.com/watch?v=9dpNQFpeo6U)
* [8-bit Western](https://www.youtube.com/watch?v=a3AlfkiVeIM)
* [Fastest Gun in 8-bit West](https://www.youtube.com/watch?v=WDdZLk7pRfI)
* [The Haunted West](https://www.youtube.com/watch?v=prT7PCMF8_Q)
* [Summertime Cowboy](https://www.youtube.com/watch?v=nu-261SVh-c)
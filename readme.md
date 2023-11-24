# A - Scoreboard

Simple Scoreboard for my streams.

## Table of Contents

- [Introduction](#introduction)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Simple Scoreboard for my streams and competitions. Uses Flask and Python.

### Prerequisites

- Python 3.11
    - In directory with `ChatSelector.py`, run `pip install -r requirements.txt`
- A web browser

### Installation

1. Clone this repository: `git clone https://github.com/theawkwardgamer133/scoreboard.git`
2. Navigate to the project directory: `cd scoreboard`
3. In directory with `ChatSelector.py`, run `pip install -r requirements.txt`

## Usage
- Starting the program
    1. When you start `scoreboard.py`, launch the webpage <a href="http://127.0.0.1:5000">http://127.0.0.1:5000</a> 
    2. If you're using OBS or any broadcasting software, add a browser source and add that link into the address bar.
- Default Key Bindings
    - <b>ALL keybindings can be changed in scoreboard.py.</b>
    -  <b>F21</b> - Add a point to player/team one.
    - <b>F22</b> - Remove a point from player/team one.
    - <b>F23</b> - Add a point to player/team two.
    - <b>F24</b> - Remove a point from player/team two.
    - <b>End</b> - Fades the scores out.
    - <b>Delete</b> - Resets Scores
    - <b>Page Down</b>  - Fades Scores back in.

- Default Usage
    - <b> REFRESHING THE WEBPAGE WILL NOT RESET THE SCORES. PRESS DELETE TO RESET SCORES.</b>
    - When starting the webpage, scores will fade in. 
    - <b> Recommended: </b> Fade scores out before resetting.
    - After a key press, code waits for 0.5 seconds. This prevents score going up twice just from pressing the button.
    - By default, the webpage on OBS will not have a background. If you want a background edit `style.css` and uncomment `"background-color: rgb(110, 110, 110);` in the `.container` class.


## Contributing

This isn't gonna be worked on at all. This is simplistic stuff for my streams. Feel free to fork it and mess with it though. Nothing will be accepted however.

## License

This project is free to use for your own use and development.

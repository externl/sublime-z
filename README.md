# Z Directory Jumping for Sublime Text

The Z plugin adds [z](https://github.com/rupa/z) directory jumping to Sublime Text; quickly open directories that you frequent on the command line.

A valid z installation is required.

## Installation

### Manually

Clone this repo as `Z` into Sublime Text's `Packages` directory. (Preferences > Browse packages...)

```
git clone https://github.com/externl/sublime-z Z
```

## What is z?

From the [z GitHub page](https://github.com/rupa/z):
> z tracks the directories you visit. With a combination of frequency and recency, it enables you to jump to the directory in mind.

## Settings

```json
  // Shell executable: "/bin/bash", "/usr/bin/zsh", "/usr/local/bin/fish"...
  // If empty then environment variable $SHELL is used.
  "shell": "",

  // Choices are:
  // 'best_match' — best match is used (z --echo <dirRegex>, no search)
  // 'list'       — list matches to choose from (z --list <dirRegex>, then search)
  // 'list_all'   — search list of directories based on 'frecency'. (z --list, then search)
  "mode": "list"
```

## Usage

Open the command palate and search `Z: Jump to directory` and press enter. Depending on the `mode` setting you can either enter a directory RegEx or search a list of frequently and recently visited directories from command line `z` installation.

### Keybindings

<kbd>cmd/ctrl</kbd> + <kbd>shift</kbd> + <kbd>o</kbd>: jump to directory using selected `mode` setting.



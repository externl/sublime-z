# Z Directory Jumping for Sublime Text

> [z](https://github.com/rupa/z) tracks the directories you visit. With a combination of frequency and recency, it enables you to jump to the directory in mind.

The Z plugin adds [z](https://github.com/rupa/z) directory jumping to Sublime Text. Quickly open directories that you frequent on the command line.

A valid z installation is required.

## Installation

### Manually

Clone this repo as `Z` into Sublime Text's `Packages` directory. (Preferences > Browse packages...)

```
git clone https://github.com/externl/sublime-z Z
```

## Settings

```json
  // Shell executable: "/bin/bash", "/bin/sh", "/usr/bin/zsh"...
  // If empty then environment variable $SHELL is used.
  "shell": "",

  // Choices are:
  // 'best_match' — best match is used (z --echo <dirRegex>, no search)
  // 'list'       — list matches to choose from (z --list <dirRegex>, then search)
  // 'list_all'   — search list of directories based on 'frecency'. (z --list, then search)
  "mode": "list"
```

## Usage

Open the command palate and search 'Z: Jump to directory'. Press enter and `z` jump to directory using seleceted `mode` setting.

## Keybindings

*  <kbd>cmd/ctrl</kbd> + <kbd>shift</kbd> + <kbd>j</kbd>: jump to directory using selected `mode` setting.



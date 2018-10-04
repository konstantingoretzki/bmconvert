# bmconvert

![bmconvert](https://i.imgur.com/acOvY1O.png)

## What is bmconvert?

bmconvert is a small utility for all Blackmagic Davinci Resolve Linux (Lite) users, who also have to deal with video incomaptibility issues using their raw video data.
With the help of the script you can easily convert your videos beforehand, and use it without problems in Davinci Resolve afterwards :)

## Features

- Simple python script - run and forget!
- Convert multiple source files at once!
- No incomaptibility issues due to the DNxHR codec!

## Usage

You can use the script in SINGLE or MASS mode:

### SINGLE

Define a single source & output file to convert to. You can use a path or just the filename if you're already inside the directory. Please note that you do not have to define the format of the output file, the script will do so automatically.

```
python bmconvert.py single /path/to/source.mov /path/to/output
```

### MASS

All video files in a directory of your choice will be converted and put in the same directory, with "_ENCODED" appended to the original file name. The default setting uses your current directory, if you want to change the directory you have to provide the `--path [path-to-files]` option.

```
python bmconvert.py mass --path /path/to/videofiles
```

## What about the quality?

The script defaults to the "sq" quality preset of the codec. If you prefer another one, you can easily change that with an additional parameter:

```
python bmconvert.py single /path/to/source.mov /path/to/output --quality=lb
```

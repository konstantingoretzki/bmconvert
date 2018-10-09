#!/usr/bin/env python3
import sys 
import os
import click
import ffmpeg


def settings():
    # TODO: Add easy way to switch codecs and alter bitrate
    pass

videoFormats = ['avi', 'mov', 'mp4', 'wmv', 'mkv', 'gif', 'gifv', 'webm', 'mpeg', 'm4v', 'flv', 'mts']

def convert(source, output, quality):
    """Convert videofile to DNxHR"""
    # Check if file extension is a compatible format to convert
    # prevent mismatch errors with x.lower() e.g. .MOV and .mov
    fileExtension = os.path.splitext(source)[1][1:]
    if fileExtension.lower() in videoFormats:
        outputName = output+'.mov'
        profile = 'dnxhr_'+quality
        try:
            # alternative: use prores --> huge files
            stream = ffmpeg.input(source)
            stream = ffmpeg.output(stream, outputName, f='mov', vcodec='dnxhd', 
                    vprofile=profile, acodec='pcm_s16le')
            ffmpeg.run(stream)
        except Exception as e:
            click.echo(click.style("\n[-] Error: {}".format(e), fg='red'))
    else:
        click.echo(click.style("\n[-] Error: '{}' is not a valid videofile - skipping".format(source), fg='red'))


def massConvert(path, quality):
    """Loop function: calls function convert() to convert multiple files"""
    os.chdir(path)
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    counter = 1
    for videofile in files:
        click.echo(click.style("\n\n[+] Converting file: {}".format(counter), fg='green'))
        videoName = os.path.splitext(videofile)[0]
        convert(videofile,(videoName+'_ENCODED'), quality)
        counter += 1        

@click.group()
def main():
    """Convert videos into
    DaVinci Resolve (Linux) compatible formats.
    """
    pass

@main.command()
# TODO: Optional output to log file
# @click.option('--log', default=False, help="Log the conversion")
# @click.option('--filenames', help="use real filenames instead of 'output'", default=True)
@click.option('--path', help='path to the files', default='.')
@click.option('--quality', help="""Switch between DNxHR modes:
'lb','sq', 'hq', 'hqx', '444'""", default='sq')
def mass(path, quality):
    """Convert all files in dir."""
    click.echo("Mass mode activated!")
    click.echo("Converting all files inside directory.")
    currentPath = os.getcwd()
    massConvert(path, quality)
    os.chdir(currentPath)
    # click.echo(path)

@main.command()
@click.argument('source')
@click.argument('output')
@click.option('--quality', help="""Switch between DNxHR modes:
'lb','sq', 'hq', 'hqx', '444'""", default='sq')
def single(source, output, quality):
    """Needs file to convert and new name."""
    click.echo("Single mode activated!")
    click.echo(click.style("\n[+] Converting file: {}".format(source), fg='green'))
    convert(source, output, quality)
    click.echo(click.style("\n[+] Conversion finished", fg='green'))


if __name__ == '__main__':
    main()

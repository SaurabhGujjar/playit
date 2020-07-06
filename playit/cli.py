import click
from pygame import mixer 
import os
from mutagen.mp3 import MP3
from tqdm import tqdm 
import time 
from pyfiglet import Figlet



@click.group()
@click.version_option(version='0.01', prog_name='playit')
def main():
    """Playit"""
    pass

@main.command()
def playlist():
    tracks = os.listdir()
    for track in tracks:
        if track.endswith('.mp3'):
            click.secho(track, fg='green')

@main.command()
@click.option('--auto', '-a', type=bool, help="plays all the songs automatically. ex:- playit play --auto true")
@click.option('--trck', '-t',  help='plays a specific song. ex:- playit play --trck "path/ to/ trackname.mp3" ')
def play(auto, trck):
    """In default mode you have all the controls while in auto mode it plays all songs one by one. You can also play a specific audio."""
    f = Figlet(font='slant')
    click.secho(f.renderText('Play it'), fg='red')
    if auto:
        mixer.init()
        tracks = []
        for audio in os.listdir():
            if audio.endswith('.mp3') or audio.endswith('.wav') or audio.endswith('.ogg'):
                tracks.append(audio)

        mixer.music.set_volume(0.5)
        for track in tracks:
            try:
                click.secho(track, fg='yellow')
                mixer.music.load(track)
                song = MP3(track)
                songLength = song.info.length
                mixer.music.play()
                click.secho('playing...' + '[AUTO]', fg='yellow')
                click.echo('press ctrl + c or ctrl + z to stop immediatly.')
                for i in tqdm (range (int(songLength)), ascii=False, ncols=100): 
                    time.sleep(1) 
            except:
                continue

                         # ELIF PART
    elif trck:
        mixer.init()
        mixer.music.set_volume(0.5)
        try:
            click.secho(trck, fg='yellow')
            mixer.music.load(trck)
            song = MP3(trck)
            songLength = song.info.length
            mixer.music.play()
            click.secho('playing...'+ '[SPECIFIC]', fg='yellow')
            click.echo('press ctrl + c or ctrl + z to stop immediatly.')
            for i in tqdm (range (int(songLength)), ascii=False, ncols=100): 
                time.sleep(1) 
        except:
            click.secho('Unsupported Format', fg="red")


                    # ELSE PART

    else:
        mixer.init()
        tracks = []
        for audio in os.listdir():
            if audio.endswith('.mp3') or audio.endswith('.wav') or audio.endswith('.ogg'):
                tracks.append(audio)

        def plybck():
            while mixer.music.get_busy():
                click.secho('Commands to control player\n========================================\nPress and hit ENTER ', fg='blue')
                click.secho('p ==> pause'+ '  ||   '+'r ==> resume\nn ==> next song'+ '  ||   '+'re ==> rewind\n+ ==> increase volume '+ '  ||   '+'- ==> decrease volume', fg='blue')
                query = input("") 
                if query == 'p' or query == 'P':
                    mixer.music.pause()	 
                    click.secho('paused!', fg="red")

                elif query == 'r' or query == 'R': 
                    mixer.music.unpause()
                    click.secho('resumed!', fg="red")

                elif query == 're' or query == 'Re':
                    mixer.music.rewind() 
                    click.secho('rewinded!', fg="red")

                elif query == 'n' or query == 'N': 
                    mixer.music.stop() 
                    click.secho('playing next...', fg="red")
                    break
                
                elif query == '+' or query == '-':
                    vol = mixer.music.get_volume()
                    if query == '+':
                        mixer.music.set_volume(vol+0.1)
                    elif query == '-':
                        mixer.music.set_volume(vol-0.1)
                    click.secho('VOL:' + ' ' + str(round(mixer.music.get_volume()*10)), fg='green')
                


        mixer.music.set_volume(0.5)
        for track in tracks:
            try:
                
                mixer.music.load(track)
                song = MP3(track)
                songLength = song.info.length
                click.secho(track, fg='yellow')
                mixer.music.play()
                click.secho('playing...'+ '[MANUAL]', fg='yellow')
                click.echo('press ctrl + c or ctrl + z to stop immediatly.')
                plybck()
            except:
                continue




@main.command()
def info():
    f = Figlet(font='slant')
    click.secho(f.renderText('Play it'), fg='red')
    click.secho('INFO--', fg='blue', bg="red")
    click.secho("Playit is a command line music player.\nIt support many audio formats like wav, ogg, mp3 etc.\nIn default mode you have all the controls while in auto mode it plays all songs one by one.", fg='green')
    click.secho('Sometimes it does not support some mp3 files. You can try other audio files:)', fg='red')
    



if __name__ == "__main__":
    main()
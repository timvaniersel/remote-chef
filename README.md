# Remote chef

Internet of Knives device. Control an chef's knife from anywhere over the internet.

![Remote chef keukenmes](https://github.com/timvaniersel/remote-chef/blob/main/assets/rpi-chef.jpg?raw=true)


## Setup
- Raspberry Pi 4
- Raspberry Pi Motor HAT
- NEMA 17 stepper motor
- NEMA 17 stepper motor bracket
- NEMA 17 Cork Dampers
- Raspberry Pi Camera
- Gate fitting
- Cutting board
- Shaft coupling 5mm
- 2 Springs
- Screws
- 2 wooden cubes 6x6x6 cm
- wiring
- Universal AC - DC adapter

## Installation

Install [FFMPEG](https://gist.github.com/wildrun0/86a890585857a36c90110cee275c45fd) on the Raspberry Pi (could take a while)

## TODO
- Add requirements.txt
- Test Flask
- Auto start Flask app
- Configure router to forward requests to Flask
- Add button to website


## Start application

#### Youtube livestream
```
raspivid -o - -t 0 -vf -hf -fps 60 -b 12000000 -rot 180 | ffmpeg -re -ar 44100 -ac 2 -acodec pcm_s16le -f s16le -ac 2 -i /dev/zero -i - -vcodec copy -acodec aac -ab 384k -g 17 -strict experimental -f flv rtmp://a.rtmp.youtube.com/live2/<code>
```
#### Flask
// TODO

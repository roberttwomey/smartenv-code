Shortcuts:
- [Usage](#usage)
- [Setup as Service](#setup-as-service)
- [Install](#install)

# Overview

<img src="https://user-images.githubusercontent.com/1598545/159357064-20d85d2e-73c4-4a31-8e3b-705abb57b1c5.png" width=600>

Waveshare 5.83inch e-Paper V2. 648x480 pixels, black and white. ([link](https://www.waveshare.com/5.83inch-e-Paper.htm))


# Usage

## Display Text
Use the p5 [mqttPublisher](https://editor.p5js.org/robert.twomey/full/CEXVmsCBS) ([code](https://editor.p5js.org/robert.twomey/sketches/CEXVmsCBS)) to control the e-ink display. Either send a text to display, or send a control signal.

topic: `/smartenv/eink`

contents: Type the text you want to send into the text box. For now, the text will be displayed as raw text.

<img width="400" alt="image" src="https://user-images.githubusercontent.com/1598545/159355224-c5c44b6b-7bd8-4f49-b820-eb147826e720.png">

result: 

<kbd><img src="https://user-images.githubusercontent.com/1598545/159356401-4ce6f5f7-20c3-48b7-a156-64ba038e0577.png" width=400></kbd>

## Display Image

Create an image (or series of images) that is 648 pixels wide by 480 pixels tall, black and white. (.jpg or .png) 

Use the p5 [mqttPublisher](https://editor.p5js.org/robert.twomey/full/CEXVmsCBS) ([code](https://editor.p5js.org/robert.twomey/sketches/CEXVmsCBS)) to tell it a filename to load.

topic: `/smartenv/eink2/image`

contents: name of the file you want to load `anniew01.jpg`
<img width="640" alt="image" src="https://user-images.githubusercontent.com/1598545/161072876-05e53ec0-be5c-4e05-a7c0-d11250c5baab.png">


### setup: 

```
cd smartenv-code/eink 
sudo systemctl stop eink
python epaperMqtt_image.py
```


## Other controls

~NOT YET IMPLEMENTED)~
~`clear` - erases the screen~


# Setup as Service

__Hardware__

Raspberry Pi 3, preferrably with wired ethernet connection connected to HDTV in portrait mode (vertical orientation)

__OS__

Install recent [Raspbian Bullseye lite]

__Set Up Persistent Service__

1. Create a service file like the following, _eink.service_:
```
[Unit]
Description=Runs eink mqtt listener after boot
After=multi-user.target

[Service]
Type=forking
ExecStart=/home/pi/smartenv-code/eink/launch_eink.sh
WorkingDirectory=/home/pi/smartenv-code/eink
User=pi

[Install]
WantedBy=multi-user.target
```

2. copy the service file to _/lib/systemd/_:

```console
sudo cp eink.service /lib/systemd/system
```

3. enable at boot

```console
sudo systemctl enable eink.service
sudo systemctl start eink.service
```

4. stop
```console
sudo systemctl stop eink.service
```

# Install
## eink setup for 5.83" display

[TK]


# Leftovers

## eink setup for 8 inch display

from https://www.waveshare.com/wiki/6inch_HD_e-Paper_HAT

Open terminal of Raspberry Pi, and install bcm2835 libraries
```
wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.62.tar.gz
tar zxvf bcm2835-1.62.tar.gz
cd bcm2835-1.62
./configure
make
sudo make check
sudo make install
```

Enable SPI interface
`sudo raspi-config`

Choose Interfacing Options ->SPI->Yes

Download demo codes and compile it
```
git clone https://github.com/waveshare/IT8951-ePaper.git
cd IT8951-ePaper/Raspberry
sudo make clean
sudo make -j4```

Check the VCOM value on the FPC

# Artworks
- Tim Schwartz [Escapism](https://www.timschwartz.org/escapism/), [eScape 50](https://www.timschwartz.org/escape-50/)
x]]]

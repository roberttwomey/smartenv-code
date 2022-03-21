# Overview

We have two e-Paper displays.

# Usage

## Display Text
Use the p5 [mqttPublisher](https://editor.p5js.org/robert.twomey/full/CEXVmsCBS) ([code](https://editor.p5js.org/robert.twomey/sketches/CEXVmsCBS)) to control the e-ink display. Either send a text to display, or send a control signal.

<img width="400" alt="image" src="https://user-images.githubusercontent.com/1598545/159355224-c5c44b6b-7bd8-4f49-b820-eb147826e720.png">

Subscribes to topic: `/smartenv/eink`

Any message you send will be displayed as raw text.

~Control messages (NOT YET IMPLEMENTED):~
~- `clear` - erases the screen~


# Setup
## eink setup for 5.83" display

[TK]

# eInk Service

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

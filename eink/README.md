# Overview

We have two e-Paper displays.

# Usage

## Display Text
Use the p5 [mqttPublisher](https://editor.p5js.org/robert.twomey/full/CEXVmsCBS) ([code](https://editor.p5js.org/robert.twomey/sketches/CEXVmsCBS)) to control the e-ink display. Either send a text to display, or send a control signal.

Subscribes to topic: `/smartenv/eink`

Any message you send will be displayed as raw text.

Control messages (NOT YET IMPLEMENTED):
- `clear` - erases the screen


# Setup
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

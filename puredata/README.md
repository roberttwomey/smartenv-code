# Puredata and smart environment stuff via MQTT
[TK Overview]

# Setup
1. Install tge appropriate version of **purr-data** from [here](https://agraef.github.io/purr-data/)
2. Download a release of `mqtt-client` from [here](https://github.com/njazz/mqtt-client-object/releases/tag/0.0.2)
3. Unzip the file. Rename the resulting folder to `mqtt-client`. Copy to `~/Library/Pd-l2ork`. Make that folder if it does not exist. 
4. Start puredata. You should be able to use the mqtt-client. 

# Patches

## Simple subscribe / publish example
[mqtt-simple.pd](mqtt-simple.pd)

<img width="500" alt="image" src="https://user-images.githubusercontent.com/1598545/155996928-d008fb7b-5e71-4e50-90da-53fb21a37663.png">


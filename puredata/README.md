# Puredata and smart environment stuff via MQTT
[TK Overview]

# Setup
1. Install tge appropriate version of **purr-data** from [here](https://agraef.github.io/purr-data/)
2. Download a release of `mqtt-client` from [here](https://github.com/njazz/mqtt-client-object/releases/tag/0.0.2)
3. Unzip the file. Rename the resulting folder to `mqtt-client`. Copy to `~/Library/Pd-l2ork`. Make that folder if it does not exist. 
4. Start puredata. You should be able to use the mqtt-client. 

# Patches

## Simple subscribe / publish example
[mqtt-simple.pd](mqtt-simple.pd) - sends messages to particle photon

<img width="500" alt="image" src="https://user-images.githubusercontent.com/1598545/155999095-829369ac-802a-4625-93a8-6510f3d61ae0.png">

[speechSubscribe.pd](speechSubscribe.pd) - controls lights on respeaker and also listens for speech transcriptions

<img width="500" alt="image" src="https://user-images.githubusercontent.com/1598545/156007366-073a9345-7ce2-4891-a589-6cb1e823307c.png">

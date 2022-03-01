# Puredata and smart environment stuff via MQTT
[TK Overview]

# Setup
1. Install the appropriate version of **purr-data** from the downloads [link](https://agraef.github.io/purr-data/)
2. Download a release of the `mqtt-client` object from [here](https://github.com/njazz/mqtt-client-object/releases/tag/0.0.2). This should work on Windws, Mac, Linux, with MaxMSP or Puredata. Choose the appropriate verson for your system.
3. Unzip the file. Rename the resulting folder to `mqtt-client` (i.e. lose the last parts of the folder name). Copy the file to your externals folder for puredata. On Mac, this is `~/Library/Pd-l2ork`. Make that folder if it does not exist. More info [here](https://puredata.info/docs/faq/how-do-i-install-externals-and-help-files) about installing externals with pd.
4. Start puredata. You should be able to use the mqtt-client within a patch, or load one of the patches below.

# Patches

## Simple subscribe / publish example
[mqtt-simple.pd](mqtt-simple.pd) - sends messages to particle photon

<img width="500" alt="image" src="https://user-images.githubusercontent.com/1598545/155999095-829369ac-802a-4625-93a8-6510f3d61ae0.png">

[speechSubscribe.pd](speechSubscribe.pd) - controls lights on respeaker and also listens for speech transcriptions

<img width="500" alt="image" src="https://user-images.githubusercontent.com/1598545/156007366-073a9345-7ce2-4891-a589-6cb1e823307c.png">

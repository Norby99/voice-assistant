# voice-assistant
This is my voice assistant Patric!

You can add can add commands and even modify his name

---

# Indice

- [How to use](##How-to-use)
- [Installation guide](##Installation-guide)

## How to use

You just need to follow the installation guide and than open the main.py file and run it.
If you want to customize the assistant you just need to open the `libraries/audio.py` file and modify the first few lines. You can even change the language from there!
> NOTE: Maybe in the future I'll implement all of this in a json file

## Installation guide

For the assistant only, run:

    $ python3 -m pip install -r requirements.txt
    
 If you want to connect it to an arduino, you will need a custom setup. I'll leave mine as ana example. It uses a [library](https://github.com/danny-source/Arduino_DY_IRDaikin), that allows it to comunicate with my daikin conditioner.

I would like to thank [DannySTW](https://github.com/danny-source) for his arduino [library](https://github.com/danny-source/Arduino_DY_IRDaikin) that helped me using the conditioner.

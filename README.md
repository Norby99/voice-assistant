# voice-assistant
This is my voice assistant Patrick!

You can add commands and even modify his name

---

# Indice

- [How to use](#How-to-use)
- [Installation guide](#Installation-guide)

## How to use

You just need to follow the installation guide by running the main.py file.
If you want to customize the assistant you just need to open the `setup.json` file and modify it.
I'll leave an example setup. Note that all the voice commands must be lowercase and the last element of the array is a list containing the output.
If you want to add your own module, follow the example below:

```json
"conditioner" : {
        "enabled" : "true",
        "features" : {
            "coldAir" : [["ho caldo", "fa caldo", "aria fredda"], ["conditioner", "cold"]],
            "hotAir" : [["ho freddo", "fa freddo", "aria calda"], ["conditioner", "hot"]],
            "conditionerPowerOff" : [["spegni il condizionatore", "spegni l'aria condizionata", "stacca il condizionatore", "stacca l'aria condizionata"], ["conditioner", "off"]]
        },
        "library" : "Conditioner.conditioner"
}
```

In this module there is name "conditioner", that can be enabled or not. The features are composed by a name (i.e. coldAir) that contains a list of lists: one for the activation strings and one for the output strings (which are composed by the module name and the output). Finally there is a library argument that can be "null" or a python path that indicates a library.

> NOTE: The module must be in a directory and the class name must have the same name of the directory.
> There must be a method in the class called execute(someString)

## Installation guide

For the assistant only, run:

    $ python3 -m pip install -r requirements.txt

 If you want to connect it to an arduino, you will need a custom setup. I'll leave mine as an example. It uses a [library](https://github.com/danny-source/Arduino_DY_IRDaikin), that allows to comunicate with my daikin conditioner.

I would like to thank [DannySTW](https://github.com/danny-source) for his arduino [library](https://github.com/danny-source/Arduino_DY_IRDaikin) that helped me using the conditioner.

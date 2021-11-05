# voice-assistant
This is my voice assistant Patric!

You can add can add commands and even modify his name

---

# Indice

- [How to use](#How-to-use)
- [Installation guide](#Installation-guide)

## How to use

You just need to follow the installation guide and than open the main.py file and run it.
If you want to customize the assistant you just need to open the `setup.json` file and modify it.
I'll leave an exemple setup. Note that all the voice commands must be lowercase and the last element of the array is a list containing the output.

```json
"conditioner" : {
        "enabled" : "true",
        "coldAir" : ["ho caldo", "fa caldo", "aria fredda", ["conditioner", "cold"]]
}
```

In this case "ho caldo", "fa caldo", "aria fredda" are the expected voice inputs and '["conditioner", "cold"]' is the output.

## Installation guide

For the assistant only, run:

    $ python3 -m pip install -r requirements.txt
    
 If you want to connect it to an arduino, you will need a custom setup. I'll leave mine as an example. It uses a [library](https://github.com/danny-source/Arduino_DY_IRDaikin), that allows to comunicate with my daikin conditioner.

I would like to thank [DannySTW](https://github.com/danny-source) for his arduino [library](https://github.com/danny-source/Arduino_DY_IRDaikin) that helped me using the conditioner.

This repository contains source code for outdoor air quality control.
Sensor is not calibrated for now so we can report just raw values.
However it's already useful to track gas concentration dynamics.

live chart: http://dkurt.github.io/nino_h2s

## Setup

In my experiment, there are
* MQ-136 Hydrogen Sulfide (H2S) sensor
* Arduino Nano (to read analog output from sensor)
* Raspberry Pi 3 board with Wi-Fi module

```
python -m pip install -r requirements.txt
nohup python run.py --token xxxx --port /dev/ttyUSB0 &
```
(specify private GitHub token and connected Arduino serial port)

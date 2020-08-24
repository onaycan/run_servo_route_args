# run_servo_route_args

## Preperation

Start with installing RPi.GPIO:

```bash
sudo pip3 install RPi.GPIO
```

Grab a micro servo engine and hope that it can carry the heavy weight of the stereo camera. If not, you may need to think about external power supply for the engine, which should not be a big deal. For this, i took Microservo 99 SG90, which is extra cheap. 

![Image 1](./readme_pics/inventory_and_connections.png?raw=true "Inventory")

As suggested in [https://tutorials-raspberrypi.de/raspberry-pi-servo-motor-steuerung/](https://tutorials-raspberrypi.de/raspberry-pi-servo-motor-steuerung/), perform the following connections: 

- Black cable –  GND (Pin 6)
- Red cable – 3V3 (Pin 1)
- Yellow cable – free GPIO Pin (GPIO17 in this case)

This website provides a nice drawing of the labels of GPIO:

[https://www.elektronik-kompendium.de/sites/raspberry-pi/1907101.htm](https://www.elektronik-kompendium.de/sites/raspberry-pi/1907101.htm)

![Image 2](./readme_pics/connections_gpio_pi.png?raw=true "Connections")


## Dependencies

You will need the following modules for this:
- RPi.GPIO
- flask
- clask_cors
- time


## Couple of workds for the code

- the root route is in this case fully obsolete, but in the future it will be meaningfull
- the route servo_socket gets the request argument from the url, the key is "angle"
- RPi.GPIO is fetched via apt-install, pwm, srvopin and all related variables are difned as global on the header.
- The start angle is 90 degrees, which coresponds to 2.5 duty cycle. Reason:
    - SG90 rotates in between 0 and 180. I need to position the head ahead 90 degrees so that the head can rotate in full in left as well as to right.


## Usage

Assuming you use your certificates created previously: 

```python
can@canrasp:~/workspace/run_serevo_route_args$ sudo python3 run_servo_route_args.py
```

If you send the angle via argument, you will see that the servo rotates. The return of teh route servo_socket gives assures you that there is no error is alerted until return.

![Image 3](./readme_pics/url_usage.png?raw=true "url_usage")
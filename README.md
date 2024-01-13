# temperature-and-humidity-sensor

## Description

This is a simple project to read temperature and humidity from a DHT11 sensor and send it to a MQTT broker. The MQTT broker is running on a Raspberry Pi 3B+.

I made this project to gain experience configuring, running code, and interfacing with peripherals (such as a DHT11 sensor) on lightweight computers (such as a Raspberry Pi). I also wanted to learn how to use MQTT to send data from a device to a server.

## Hardware

- Raspberry Pi 3B+
- DHT11 sensor with breakout board
- 3 jumper wires

## Software

Coming soon...

## Installation

### Hardware

#### Connecting the DHT11 sensor to the Raspberry Pi

I used a DHT11 sensor with a breakout board. The breakout board has 3 pins: VCC, GROUND and DATA, marked with +, - and out respectively. Each pin is connected to a pin on the Raspberry Pi by a jumper wire: the VCC pin is connected to the 3.3V pin, the GROUND pin is connected to a GND pin, and the DATA pin is connected to any available GPIO pin. I used the following connections:

- VCC to pin 1 (3.3V)
- GROUND to pin 6 (GND)
- DATA to pin 11 (GPIO 17)

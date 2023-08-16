# picoRGB library

A simple RGB LED library for Micropython, tested on Raspberry Pi Pico.

## Usage

Define RGBLed object, pin order is RGB.
Supports common cathode or anode.

```python
led = RGBLed(15,14,13,RGBLed.Cathode)
```

Turn off LED:

```python
led.off()
```

Set custom color:

```python
led.setColor(120,50,75)
```

Set custom color slowly:

```python
led.slowSet(10,200,195)     
```

Show LED information:

```python
led.show()                    
```

Set LED to white:

```python
led.white()        
```

Set LED to yellow:

```python
led.yellow()
```

## About

This project was originally forked from [sonmezarda](https://github.com/sonmezarda/RGB-LED-Library).

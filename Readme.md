# Hogwarts magical portraits

## Brief story

Impressed by the work [mona_lisa_eyes](https://github.com/emilyxxie/mona_lisa_eyes)
by Emily Xie I started my own project.
 
In Emily's project Mona Lisa's eyes will follow you as you move around the room.

I remembered about old tablet gathering dust in the back of the pantry. And I 
wanted to realise the same idea. wanted to realise the same idea. 
I decided to hang the tablet on the wall in the corridor and showing in it live photos like
Hogwarts magical portraits. 

## Project structure

### Animate portrait
1. Select the portrait you want to make magical.
1. Make several animated pictures with 
[First Order Motion Model for Image Animation](https://github.com/AliaksandrSiarohin/first-order-model):
    - Pictures that must be corresponding the position of the person in front of magic portrait.
    - Make long time gif tha showing when not people in front of portrait.

### Predict picture
1. Bring your old unnecessary tablet from the pantry. 
1. Use tablet camera and [BlazeFace](https://github.com/hollance/BlazeFace-PyTorch) to detect
people in front of it.
1. According predicted position of person in front of tablet's camera show picture on tablet's display.

### Deployment
1. 
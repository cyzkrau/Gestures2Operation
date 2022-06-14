# Gestures2Operation

It's our Computer Graphics final project. There are 5 applications of gesture-operation. Here is [video](https://www.bilibili.com/video/BV1tT41157Kq?pop_share=1&vd_source=c567eb8bca008ec5fd0020973414e9c4). 

All codes are based on x86 Python. Run
```bash
pip install requirements.txt
```
to install dependencies. 

## Mediapipe

Our detection part is made in use of `mediapipe`, a frame work to dect human working of google.

Its data is like this.(the data: hand).

```python
[
    {'lmList': [[478, 523, 0],      #[x, y, z]
                [553, 517, -17], 
                [612, 494, -17], 
                [648, 453, -17], 
                [675, 421, -17], 
                [595, 419, 12], 
                [631, 371, 5], 
                [649, 340, -4], 
                [664, 312, -12], 
                [563, 401, 12], 
                [589, 342, 7], 
                [604, 305, -6], 
                [617, 275, -16], 
                [528, 393, 9], 
                [548, 338, 0], 
                [563, 302, -11],
                [576, 275, -19], 
                [488, 393, 3], 
                [503, 349, -6], 
                [513, 320, -12], 
                [525, 294, -15]
               ], 
     'bbox': (478, 275, 197, 248), 
     'center': (576, 399), 
     'type': 'Left'
    }
]
```



​	And its map is (in the 'lmList:'), where its axis is [x,y,z], and x is left to right; y is up to the down, and z is inside screen out.

![](./img/data-info.png)

![](./img/example.png)

### demos

There are 5 demos

- [Virtual Keyboard](1-virtual_keyboard)
- [Virtual Draw](2-virtual_draw)
- [Virtual Blocks](3-virtual_blocks)
- [Control 2048 Game](4-2048Game)
- [Play Skier Game](5-skierGames)

See more details in their own `README.md` and report in `./report/report.pdf`. 
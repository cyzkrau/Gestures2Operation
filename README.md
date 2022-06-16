# Gestures2Operation

It's our Computer Graphics final project. There are 5 applications of gesture-operation. 

- [Virtual Keyboard](1-virtual_keyboard)
- [Virtual Draw](2-virtual_draw)
- [Virtual Blocks](3-virtual_blocks)
- [Control 2048 Game](4-2048Game)
- [Play Skier Game](5-skierGames)

Some of them are referenced in the [cvzone tutorial](https://www.computervision.zone/courses/advance-computer-vision-with-python/). They are all based on mediapipe and camera of computer. Here is [final video](https://www.bilibili.com/video/BV1tT41157Kq?pop_share=1&vd_source=c567eb8bca008ec5fd0020973414e9c4). 

All codes are based on x86 Python. Run
```bash
pip install requirements.txt
```
to install all dependencies. 

## Mediapipe

Our detection part is made in use of `mediapipe`, a frame work to dect human working of google.

Its data is like this.(the data: hand).

```python
[
    {'lmList': [
            [478, 523, 0],      #[x, y, z]
            ...
            [525, 294, -15], 
        ], 
     'bbox': (478, 275, 197, 248), 
     'center': (576, 399), 
     'type': 'Left'
    }
]
```

Key point locations are stored as `[x, y, z]` of Hand Landmark Model in `lmList`. The sequence of key points is shown in the figure. 

![](./img/data-info.png)

Here's an example. 

![](./img/example.png)

See more details of demos in their own `README.md` and `./report/report.pdf`
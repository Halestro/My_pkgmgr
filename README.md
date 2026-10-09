# retro-banner

A small, dependency-free Python package for generating framed terminal banners.

## Install

```bash
python -m pip install .
```

## Command line

```console
$ retro-banner "Hello, world!"
╔═════════════════╗
│ Hello, world!   │
╚═════════════════╝
```

Choose another frame, padding, or fixed interior width:

```bash
retro-banner --border star --padding 2 "RETRO MODE"
printf 'MULTI\nLINE' | retro-banner --border single
retro-banner --border none --width 24 "centered"
```

## Python API

```python
from retro_banner import banner, render

print(banner("Hello, world!"))
print(render("Line one\nLine two", border="single", padding=2))
```

`render` accepts `double`, `single`, `star`, and `none` borders. For a fixed
interior width, pass `width`; text that does not fit raises `ValueError`.

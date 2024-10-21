# 🐒 bebeziana
A small package to serve all your pre- and post-sweeping needs...

## Description

![MONKE](./monke.gif)

## Features

- [x] Data reader
- [x] Dictionary flattener


## Getting started

```python
import bebeziana
from pathlib import Path

data = bebeziana.read(Path("./outputs/2023-07-11/"), ["setup.yaml", "results.yaml"])
```

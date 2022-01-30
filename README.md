# CTF Flag Generator

A CTF leet flag generator

## Install

```
pip install flag-gen
```

## Usage

To translate alpha characters to leet string:

```
flag-gen 'this is your flag' 
````

And output maybe:

```
TH1S_i5_yOUr_fL@6
Entropy: 20.92 bits
```

You can use it in your code:

```python
import flag_gen

print(flag_gen.leet('this is your flag'))
# ('7H1s_1$_youR_fL46', 20.92481250360578)
```

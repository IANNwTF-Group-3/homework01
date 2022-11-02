# Homework 01

## Create virutal environment with conda

```bash
conda create -name iannwtf
conda activate iannwtf
```

## Install dependencies

```bash
conda install tensorflow
conda install matplotlib
```

## Run the code

```bash
python kittyconcert.py
```

# 3 Math

A sigmoid function is just a function with s shape, we can use $arctan(x)$

derivation of $arctan(x) = \frac{1}{1+x^2}$

logstic sigmoid function is $\frac{1}{1+e^{-x}}$, derivation is $\frac{e^{-x}}{(1+e^{-x})^2}$

$f(x, z, a, b) = (4ax^2 + a) + 3 + \sigma(z) + (\sigma(b)^2)$

assuming $\sigma(x) = \frac{1}{1+e^{-x}}$
derive $f(x, z, a, b)$ with respect to $x$, $z$, $a$, $b$

- $\frac{d}{dx} = 8ax$
- $\frac{d}{dz} = \frac{e^{-z}}{(1+e^{-z})^2}$
- $\frac{d}{da} = 4x^2 + 1$
- $\frac{d}{db} = \frac{2e^{-b}}{(1+e^{-b})^3}$

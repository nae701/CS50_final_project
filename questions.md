# Questions

## What's `stdint.h`?

A header fiel that includes definitions of other integer types that contain specific widths

## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?

Allows for greater flexibility, as well as an increase in data storage optimization. For instance, if one knows that a certain value will always be positive, one can use an unsigned integer rather than a signed integer in order to store a greater range of valid values.

## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

1,4,4,2 bytes respectively 

## What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be? Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."

In ASCII, BM 

## What's the difference between `bfSize` and `biSize`?

'bfSize' is the size of the bitmap file in bytes whereas 'biSize' is the number of bytes required by the structure 

## What does it mean if `biHeight` is negative?

It means that the bitmap is then top-down

## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?

biBitCount is the structure which determines the number of bits per pixel and thus the number of colors in the bitmap

## Why might `fopen` return `NULL` in lines 24 and 32 of `copy.c`?

If the file 'fopen' is trying open does not exist, it will return a null pointer

## Why is the third argument to `fread` always `1` in our code? (For example, see lines 40, 44, and 75.)

It is because we are iterating over each pixel

## What value does line 63 of `copy.c` assign to `padding` if `bi.biWidth` is `3`?

if 'bi.biWidth' = 3, then padding is assigned the value of 3

## What does `fseek` do?

It lets us change the offset of a pointe

## What is `SEEK_CUR`?

The current position of the file pointer

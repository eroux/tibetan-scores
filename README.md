Tiny Tibetan score pdf renderer
============================

This repository contains scripts and TeX styles to typeset Tibetan text-only
scores (no fancy yangyig).

## Mechanism ##

A file with `.tabc` extension contains the description of the score, in unicode
with a defined syntax (see hereafter), transforms it into a .tex file describing
the score, that you can include from another global tex file.

## Syntax ##

The syntax is very simple and as follow:

 * `<1:foo>` : foo is a meaningful syllable
 * `<2:foo>` : foo is afixed-shape intercalary syllables
 * `<3:foo>` : foo is a variable-shape intercalary syllable
 * `<4:foo>` : foo is an opener
 * `<5:foo>` : foo is a prolonger

Drum signs (࿁ or ࿀) under a syllable are put before the ending tsheg(་) of this
syllable.

Example: `<1:ཀ࿁་དྲ࿁་བའི࿀།> <4:ཨེ࿁་>(kgkhy) <1:དམར࿁་>()`

## Parsing tabc file ##

Once your `.tabc` file is finished, you can compile it with the `compile-score.py`
script. It will compile it into a `.tex` file with the same base name. See
example score in the repository.

## Using your .tex file ##

The obtained `.tex` file only contains the data for the score, so you cannot
compile it raw. Instead, include it in another `.tex` file where you define
the layout you want. See `example.tex` for an example of such a file.

This main file must include the `tibetanscore` LaTeX package of this repository.

## Dependencies ##

The python script has been tested only with Python3.

The example file depends on the [upecha](https://github.com/eroux/upecha), for
which you will need LuaTeX and also need an updated version of
[gloss-tibetan.ldf](https://github.com/eroux/polyglossia/blob/master/tex/gloss-tibetan.ldf).
You can also use a regular LaTeX class, though it won't look like a Tibetan pecha.

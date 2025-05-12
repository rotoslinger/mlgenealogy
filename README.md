# mlgenealogy
ML repo aimed at researching handwriting recognition for digitizing historical census records.

## Install with terminal command:
```
source .mlgenealogy/bin/activate         
pip install -r requirements.txt
```
### Purpose
The goal is train a simple model to recognize and transcribe text of any font. Eventually this will be extended to recognize hand written characters.

The model needs to be completely unsupervised. Even handwritten text will be converted into fonts that will be randomly generated and tagged simultaneously.

The idea is very simplistic. Output random chars in random fonts, with random letter groupings, and spaces, record these letters and their x/y locations as data, produce an image of said data, and use this to train within a certain probability.

This will be a checkpoint

A second stage will be be used to distort data and possibly scramble it

This will be a checkpoint


At no time will spelling or style be statically considered as these change over the ages. Nor will neighboring letter or nearest neighbor relationships. Otherwise multiple datasets would need to be considered.

This is meant to transcribe and should have no bias from spelling or reasoning of any sort. No human error what so ever. When handwritten language is finally considered, fonts will be chosen and segmented on a letter by letter bases and generated this way.
# Sample Problem

In order to make meaningful headway, it can be quite nice to have a toy problem to solve first in order to validate premises. For this architecture, we are starting with the problem of learning how to parse arbitrarily long, simple arithmetic statements.

## Language Specs

One of the larger notions to explore, which must be answered in order to understand the requirements of strong intelligence, is whether or not human languages are equivalent to, or a consequence of an underlying system for formal languages embedded in the human brain. Thus we shall specify the formal languages that we are aware of, when relevant.

The valid strings of the language used for this sample problem can be roughly captured by the below:

Well Formed Formulas = -?[0-9]*([+|-|*|/]-?[0-9]*)*\\n
while not a proper reg expr, it can be vaguely read as refering to any string of numbers joined together by simple arithmetic operators

Alphabet = 8-bit ASCII characters (though most of ascii won't be used, it lays the framework for future work)
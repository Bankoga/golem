# Sample Problem

In order to make meaningful headway, it can be quite nice to have a toy problem to solve first in order to validate premises. For this architecture, we are starting with the problem of learning how to parse arbitrarily long, simple arithmetic statements.

## Problem Definition

Given a 3 part statement in the selected formal alphabet
When it is a valid arithmetic statment
Then return the result alongside system confidence percentage in answer
Else return a flag to indicate invalid input alongside system considence percentage in answer

> Note on statement size: Large statements that cannot be consumed at once require focus, world composition, and decision making abilities. Memory can probably be tested with both so it's best to start with the less complex case.

## Problem Overview

In short, an overview of what we are trying to get the system to learn. Furthermore, it can be thought of as testing whether or not the system learns, or gets adapted to an environment.

> Plan: We want to train a system to be able to correctly parse any real number that is split into multiple components or turn an arithmetic statement into one of it's corresponding real number equivalents.
> Success Expansion: If we are successful at doing simple maths, then we will attempt to train a system to generate equivalent arithmetic statements from real numbers.

The system will not have any internal representations of the contents of each parameter set in it's input or output streams after initialization. Those will only be adapted during operation. For input, the system is given a static set of 3 distinct variables (8-char number, 1-char operator, 8-character number) broken across the internal token size (8-bit/stack) into 17 input tokens.

Do we start with the system being able to see the whole pattern? This would limit the design of the architecture in a way that lets us avoid dealing with storing inputs processing time by removing the need for external input storage. Thus, we can simply train to reduce the number of timesteps required for a valid response without an altered input state. Altered input state would then be indistinguishable from a new query.

## Language Specs

One of the larger notions to explore, which must be answered in order to understand the requirements of strong intelligence, is whether or not human languages are equivalent to, or a consequence of an underlying system for formal languages embedded in the human brain. Thus we shall specify the formal languages that we are aware of, when relevant.

### Input Strings

The valid strings of the language used as inputs for this sample problem can be roughly captured by the below:

Well Formed Formulas = -?[0-9]*([,|.|+|-|*|/]-?[0-9]*)*\\n
while not a proper reg expr, it can be vaguely read as refering to any string of real numbers joined together by simple arithmetic operators

Token Types

- Number : a fundamental unit
- Operator : connects numbers together according to an unique rule

> Should the WFF be prefixed by the ASCII code for start of text, and postfixed by the ASCII code for end of text?

Alphabet = 8-bit ASCII characters (though most of ascii won't be used, it lays the framework for future work)

### Output String

The valid strings that can be created as outputs from spikes for this sample problem are below:

- Status Code : 8-bit ASCII code for query processing and result state info
  - When it recognizes a new query, this should equal ASCII:6 (acknowledge)
  - When it can't answer the query, this should equal ASCII:7 (bell)
  - When it is outputting an answer to a query, this should equal ASCII:0 (null)
  - When it has finished answering a query, this should equal ASCII:3 (end of text)
- Response Value : chunk of a full statement to return

Do we want the system to read each word in character by character, or token by token? It has to be able to do both equally well. Characters in an alphabet can be tokens or substrings of tokens within valid strings in some corresponding dictionary

Do we want an output 1 character at a time, or 1 token at a time?

> IMPORTANT: For this problem, the system isn't learning how to build a new spike to number format method. Rather, it is learning how (or being adapted) to use (or fit) a pre-existing spike to number format method/language.
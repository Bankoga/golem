# Configs

Golem processing matrices are defined via module function configs.

## Properties

Each config has the following properties

- Name: The primary id, and semantic label for the module
- Purpose: A description of what the module does at a high level within the cognitive matrix
- Pipeline: The processing streams that run through the module
- ProcCycle: Each module goes through a templated processing cycle which is composed of stages, and groups

- InputMelds: A list of all melds that serve as input to the module
- ShapeDictList: Defines the list of output shapes generated in the form of a dictionary using field type as key with the value as a string of inputs by id along with preprocessing to be evaluated. Shapes are resource type agnostic, and the same shapes are used for all resource type specific processing.
- OutputMelds: The primary output key value tuples
- LinkMelds: The alternate output key value tuples
- LinksDefined: Templated connections for outputting to the module, that can be used to determine the number of channels in this module during initialization
- Channels: Each layer template function initialized within a module is a distinct channel?

### Melds

Every data bearing connection between two modules is a Meld. All melds have the same format except for link rule specifiying input melds. The formats are:

- Default: Module_key-subdest,Resource_type,Field_shape
- Links: Link_key,Resource_type

Each link type can have it's own field shape that needs to be accounted for, and each link must be counted separately so we have to dynamically generate all link input and output melds



- LayerBases: The function template that the module uses for processing inputs. Layers process resources using Nodes. Defines the layer set to use which is used for operating on layer resource shapes (internal module shapes).
- LayerParameters: The node properties of the template. Contains the Node specific resource details.

### Proc Cycles

A proc cycle is the series of transformations that are performed internally while filling the external output shapes. Each distinct type of matrix module has it's own proc cycle. Here are some example processing cyles:

#### Coders

The type of matrix modules used for bringing data into or out of the matrix.

| Property Name | Config Location | Purpose | Example |
| --- | --- | --- | --- |
| --- | Proc Cyle | --- | --- |
| ProcGroupDetails | Module | Used to store population level details for modules that represent large groups of nodes. Not really used for coders which require framework level hook support | N |

#### DecisionControlledLogosEncapsulators

The type of matrix modules used for performing operations that can be interferred with by the decision making system.

| Property Name | Config Location | Purpose | Example |
| --- | --- | --- | --- |
| --- | Proc Cyle | --- | --- |
| ProcGroupDetails | Module | --- | GroupId: NodeDetails,OutputMelds |

#### AgnosticLogosEncapsulators

Corresponds to the type of matrix modules used for bringing data into or out of the matrix.

| Property Name | Config Location | Purpose | Example |
| --- | --- | --- | --- |
| --- | Proc Cyle | --- | --- |
| ProcGroupDetails | Module | --- | [GroupId: {NodeDetails,OutputMelds}] |
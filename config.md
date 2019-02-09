# Configs

Golem processing matrices are defined via module function configs.

## Properties

Each config has the following properties

- Name: The primary id, and semantic label for the module
- Purpose: A description of what the module does at a high level within the cognitive matrix
- Pipeline: The processing streams that run through the module
- ProcType: Each module goes through a templated processing cycle or function which is composed of stages, and groups. Though could conceivably be reduced to a stagegroupsdict placeholder because all of the other details appear to be specific to each module. Stages are mostly for useage by the nodes to identify shapes by key, and groups are the different factors of the function or process.
- InputMelds: A list of all melds that serve as input to the module. Eventually, we could get rid of input melds with just the module shape coupled to an automatic linking and rebase system, for some parts maybe. For others, it's definitely necessary to distinguish. Forcing the cognitive architects to hard code the correspondence between all inputs, and outputs seems useful though when it can be applied. This can only be applied to input-output meld pairs of the same level in the same module. The two levels are Proc-Proc or Module-Module.
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

### Proc Func

A proc func (or cycle) is the series of transformations that are performed internally while filling the external output shapes. Each distinct type of matrix module has it's own proc cycle. Here are some example processing cyles:

#### Coders (CDR)

The type of matrix modules used for bringing data into or out of the matrix.

| Property Name | Config Location | Purpose | Example |
| --- | --- | --- | --- |
| ProcType | Both | --- | --- |
| ProcComposition | ProcType | --- | --- |
| ProcStageGroupsDict | ProcType | --- | --- |
| ProcStageShape | Module | Used to indicate the shape of the groups in the stage. | N || *:InputShapeId || ? |
| ProcGroupInputMelds | Module | --- | --- |
| ProcGroupDetails | Module | Used to store population level details for modules that represent large groups of nodes. Not really used for coders which require framework level hook support | N |
| ProcGroupOutputMelds | Module | --- | --- |
| ProcOutputMelds | Module | --- | --- |

#### DecisionControlledLogosEncapsulators (DCLE)

The type of matrix modules used for performing operations that can be interferred with by the decision making system.

| Property Name | Config Location | Purpose | Example |
| --- | --- | --- | --- |
| ProcType | Both | --- | --- |
| ProcComposition | ProcType | --- | --- |
| ProcStageGroupsDict | ProcType | --- | --- |
| ProcStageShape | Module | Used to indicate the shape of the groups in the stage. | N || *:InputShapeId || ? |
| ProcGroupInputMelds | Module | --- | --- |
| ProcGroupDetails | Module | --- | GroupId: {[NodeDetails],node_count} |
| ProcGroupOutputMelds | Module | --- | --- |
| ProcOutputMelds | Module | --- | --- |

#### AgnosticLogosEncapsulators (ALE)

Corresponds to the type of matrix modules used for bringing data into or out of the matrix.

| Property Name | Config Location | Purpose | Example |
| --- | --- | --- | --- |
| ProcType | Both | --- | --- |
| ProcComposition | ProcType | --- | --- |
| ProcStageGroupsDict | ProcType | --- | --- |
| ProcStageShape | Module | Used to indicate the shape of the groups in the stage. | N || *:InputShapeId || ? |
| ProcGroupInputMelds | Module | --- | --- |
| ProcGroupDetails | Module | --- | GroupId: {[NodeDetails],node_count} |
| ProcGroupOutputMelds | Module | --- | --- |
| ProcOutputMelds | Module | --- | --- |
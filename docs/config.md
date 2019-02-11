# Configs

Golems configs are based on a composable field component grouping system where each piece can be eventually subjected to an evolutionary algorithm for architecture design, or multi-golem architecture combining. Ultimately however, there are two types of configs that define a type of golem.

- Module Configs: Golem processing matrix components (groups) and their interconnections are defined via module function configs. A module config determines the internal properties of object, sans Links
- Golem Configs: Each type of golem corresponds to a specific set of interconnected functions. Each function is defined via a key that corresponds to some module config, with the connections between modules largely being defined here.
- ProcType Configs: Each functional part of a module corresponds to some specific group within a processing cycle. Each proc cycle consists of a number of groups which are the subdestinations of datapack addressess.

## Properties

Each Golem config has the following properties:

- Id: The primary type id of the golem. THIS IS NOT THE CONTAINER OR INSTANCE ID.
- Name: The semantic label of the type of golem. THIS IS NOT THE CONTAINER OR INSTANCE NAME.
- Purpose: A description of what the module does at a high level within the cognitive matrix
- Modules: The list of processing containers that define the skeletion of the cognitive matrix of the golem
  - ShapeToGroupsDict: Used to indicate the shape of the groups in the stage. | N || *:InputShapeId || ? |
  - ProcGroupComposition: Used to determine how the different members of the group work together to produce the output!
  - ProcOutputMelds | Module | --- | --- |
  - InputMelds: A list of all Golem type specific melds that serve as input to the module. These use specific group ids in order to be distributed.
  - OutputMelds: The primary output key value tuples. Defines the total sets of shapes used by each processing group as outputs. These use specific group ids in order to be distributed.
- Parameters: A dictionary of matrix settings that are golem type specific

Each Module config has the following properties:

- Name: The primary id, and semantic label for the module
- Purpose: A description of what the module does at a high level within the cognitive matrix
- ProcType: Each module goes through a templated processing cycle or function which is composed of stages, and groups. Though could conceivably be reduced to a stagegroupsdict placeholder because all of the other details appear to be specific to each module. Stages are mostly for useage by the nodes to identify shapes by key, and groups are the different factors of the function or process.
- ProcGroupDetails: Used to store population level details for modules that represent large groups of nodes. Example = GroupId: {[NodeDetails],total_node_count,[hooks]}
- Links: The list of link rules to use for modifying the inputs, outputs, and shape composition by hook. In essence, the list of interconnections that modify processing within this module which it may reciprocally affect.
- LinksRooted: The list of links that are are defined by this module or rooted to this module.
- Channels: Each layer template function initialized within a module is a distinct channel?

## Connections

There are two types of melds between modules: full, and link. All connection descriptions, are used to produce the datapacks used during runtime. Descriptions are only designed for use during initialization at present. Each datapack consists of an unique set of address, resource type, and shape. Thus all connections produce the same full format with several definitional formats.

One of the most important distinctions between a link and a full meld, is that a link only touches the pieces which have the appropriate hooks.
A meld is a pattern for describing one or more data_packs which have a static address, resource type, and shape. They show up in all properties that use melds.
A link is a pattern for describing changes to the shape_composition function that corresponds to a group or meld based on hooks. Links can introduce new datapacks into the inputs, and outputs of a module as well as affect the number of regions in the module. They only show up in ProcGroup I/O melds.

- Full: Modulekey-subdestkey,Resource_type,Field_shape,hooks
- Link: Linkkey || Linkkey_i

Each non-itemized (bucket defining) link key can help set a statically determined number of regions for the defining module, and the number of shapes to break the output of connected modules into.
Each itemized link helps to dynamically determine the number of regions for the defining module.

Each link type can have it's own field shape that needs to be accounted for, and each link must be counted separately so we have to dynamically generate all link input and output melds

### Links

Links are golem specific changes to the inputs and outputs of specifically interconnected processing groups. Essentially, they are templated connections for outputting to or from the module to other connected modules. Some can be used to determine the number of channels in this module during initialization?

Links require hooks to use, which are applied to proc group melds. Hooks are paired -In/-Out, and somewhere with a -Out builds a datapack to be used EVERYWHERE the corresponding -In exists.

## Proc Func

A proc func (or cycle) is the series of transformations that are performed internally while filling the external output shapes. Each distinct type of matrix module has it's own proc cycle. Here are some example processing cyles:

| Property Name | Config Location | Purpose | Example |
| --- | --- | --- | --- |
| ProcType | Both | --- | --- |
| ProcComposition | ProcType | --- | --- |
| StageToGroupsDict | ProcType | Used to determine the number of proc groups, and their positions relative to each other. Must use valid link or field ids as keys. All valid fields are defined WHERE? | --- |
| ProcGroupInputMelds | ProcType | --- | GroupId: {[FullMelds],[LinkMelds]} |
| ProcGroupOutputMelds | ProcType | --- | GroupId: {[FullMelds],[LinkMelds]} |

- Coders (CDR): The type of matrix modules used for bringing data into or out of the matrix
- DecisionControlledLogosEncapsulatorsGroup (DCLEG): The type of matrix modules used for performing operations that can be interferred with by the decision making system.
- AgnosticLogosEncapsulators (ALEG): Corresponds to the type of matrix modules used for bringing data into or out of the matrix.

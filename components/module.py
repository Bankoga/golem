class Module():

    def __init__(self):
        # once fully initialized, a module has very few aggregate properties to consider during operation
        self.prevActivationShapes=dict()
        self.processingGroups=dict()

    def operate(self,inputShapes):
        outputShapes = prepareBlankOutputShapes()
        for group in self.processingGroups:
            # group.transform  needs to handle calculating its own activation shape which it adds to the outputShape to be processed by the primary dispatcher
            outputs = group.transform(inputShapes)
            for outputShape in outputs:
                outputShapes[outputShape.key]+=outputShape.value
                # If this is the last group, after adding the value, throw each point through a ReLU
        return outputShapes

    def compose_functions(self,inputMelds,funcType,procStageGroupsDict,procStageShape,procGroupInputMelds,procGroupDetails,procGroupOutputMelds,procOutputMelds,shapeComposition,outputMelds,linkMelds,linksDefined):
        # just preparing a nice battery of for loops for all the looping that's gunna be done
        for inMeld in inputMelds:
        for outMeld in outputMelds:
        for linkMeld in linkMelds:
        for link in linksDefined:
        for fType in funcType:
        for stage in procStageGroupsDict:
        for stageShape in procStageShape:
        for groupInMeld in procGroupInputMelds:
        for groupDetailSet in procGroupDetails:
        for groupOutMeld in procGroupOutputMelds:
        for procOutMeld in procOutputMelds:
        for shapeComposition in shapeComposition:
        """
        at the lowest level of granularity, we have the actual functions
        It does not matter if these are cells, synapses, chemical interactions, processing groups, etc... because, whatever the lowest the level, that is where we combine all the pieces together.
        Currently, we are going with processing group level functions, however this could be turned into a object type property at some point.
        Preparation for processing, thus occurs in several steps
        1) Converting all the input,output,and link melds into a dictionary that the processing groups can leverage for 
        2) 
        ?) 
        """
    return "lol"
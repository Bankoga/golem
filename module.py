class Module():

    def __init__(self):
        pass

    def compose_function(self,inputMelds,funcType,procStageGroupsDict,procStageShape,procGroupInputMelds,procGroupDetails,procGroupOutputMelds,procOutputMelds,shapeComposition,outputMelds,linkMelds,linksDefined):
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

# the golem core class. Needs to be extracted from the golem class
class Core:
    TODO: Migrate core construction, manipulation, and operation code into core class
    def __init__():


TODO: should each module have a uniquely defined list of input shapes, or should we use a dynamic approach?
def activateModule(inputShapes, assocShape, contextShape):
    """
    The reach of a node type is defined by the number of convolutions it uses along with their shapes, and input sources
    During each time step we do the following
    """
    Shapes = {
        'Layers':dict(),
        'NodeTypes':dict(),
        'Outputs':dict()
    }

    for layer in the module we calculate its cumulative effects on the output field activation shapes for the current module (which always start out empty)
        for each i
            for each j in the internal shape we calculate whether or not it will be active in the next timestep by doing the below
            An i,j corresponds to a Pod
            shapes['NodeTypes']
            for each node in module.Pods[i][j]:
                If !active in the last timestep
                    read the activity of the output fields from the past timestep for the local resource points within reach by multiplying each point by the corresponding likelihood of activation impact weight. Which is NxN matrix where N=the number of different probability effect groups based on the i,j diff
                    read the activity of each input field to the local resources within reach by multiplying each point by the corresponding likelihood of activation impact weight
                    Multiply each activity field by the corresponding likelihood of impace weight
                    sum the two activity fields
                    if the sum of both forms of activity is above the activation % chance threshhold, then activate the node
                    shapes['NodeTypes'][node.type] += sum
                Else
                    then it was just active, and thus has an immutable 0% chance of being active in the next timestep



A major question about plasticity that has been around is do we track the weight that was activated, time since active, or something other flag for use when calculating weight changes?
The answer may be that instead of tracking the past N timesteps worth of port activation data, why not clear ports on activation and have each port self-clear after N timesteps
Thus only activated ports would have a counter in memory, and we can use the difference between the remaining count and the port storage duration limit to determine the related plasticity strengths!

A port has several properties that need to be considered

current growth factor (incoming, outgoing). I.E. the degree to which each side can currently change, and which side to change (transient, permanent)
channel sizes (incoming, outgoing)
intersection address (each port occurs at an intersection of unbound reading and writing edges)

Only the active reap the benifits of local timestep plasticity modulated by resource concentrations
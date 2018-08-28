# Externalities

In order for a problem graph to be useful, we need to have external points of interaction.

## Sensory Streams

We want to have several different types of senses supported for a variety of use cases.

List of desired input encoders

- Video Stream (camera)
  - to allow for real world interactivity
- Audo Stream (mic)
  - so that we can have systems which process external sound
- Screen Stream (monitor)
  - necessary for some types of agents that leverage pc capabilities
- Speaker Stream (default pc audio)
  - necessary to pick up on audio played on a pc that an agent is leveraging
- Session Timer or Maintenance Countdown
  - so the system can intuitively know how long till the next maintenance cycle
- File stream
  - to provide for the ability to read a file without a monitor, or while using the available screens for other tasks

## Output Streams

In order for a problem graph to do things, it needs to have dedicated decoders points that take spikes, and convert them into other types of data.

List of desired output decoders

- Eye Position
  - Controls visual input filter size, and positiong
- Cursor Position
  - either the direct position, or some trajectory/mouse input
- Mouse buttons
  - so that it can act as a normal user
- Keyboard input
  - converts spikes to keys on a keyboard
  - simulates typing
- Audio Stream
  - Must support different streams like speakers, and mic
  - to convert spikes to sounds
- File buffer
  - to enable writing to a file directly without mediation through other output streams

## Potential Pitfalls

If we give an exploratory process control over the system, there are things to be aware of that could lead to it's untimely demise. For instance, without safeguards it is possible for it to shut down the computer it is running on thus terminating itself without saving. Or it could kill it's own process via admin terminals, and task managers.
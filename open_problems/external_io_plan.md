# Externalities

In order for a cell map to be useful, we need to have external points of interaction.

## Sensory Streams

We want to have several different types of senses supported for a variety of use cases.

List of desired input encoders

- Video Stream (camera)
- Audo Stream (mic)
- Screen Stream (monitor)
- Speaker Stream (default pc audio)
- Session Timer or Maintenance Countdown
  - so the system can intuitively know how long till the next maintenance cycle

## Output Streams

In order for a cell map to do things, it needs to have dedicated decoders points that take spikes, and convert them into other types of data.

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

## Potential Pitfalls

If we give an exploratory process control over the system, there are things to be aware of that could lead to it's untimely demise. For instance, without safeguards it is possible for it to shut down the computer it is running on thus terminating itself without saving. Or it could kill it's own process via admin terminals, and task managers.
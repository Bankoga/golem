TODO: Optim: use cell consts for the static properties that remain the same for all cells to minimize memory usage
# need to determine acceptable depolarization rates
self.depolarization_rate = 25
self.resting_potential = 0
# need a min polarity in order to limit the depression of the cell
self.polarity_min = -25
# number of timesteps for the cooldown
self.cooldown_duration = 3
# num timesteps to track history for
self.stdp_window = 20
class UsageLimits():
    def __init__(self, capacity, cost, recharge):
        # primary props
        self.max_capacity = capacity # 300
        self.curr_capacity = capacity
        self.activation_cost = cost # 8
        self.capacity_recharge = recharge # 1
        # the following are for stats calcs
        self.ts = 1000
        self.adjusted_activation_cost = cost - recharge
        self.time_till_depletion = capacity/self.adjusted_activation_cost
        self.raw_time_to_full = capacity/recharge
        self.recharge_one_activation = cost / recharge
        self.max_init_freq = (self.time_till_depletion + ((self.ts-self.time_till_depletion) / (self.recharge_one_activation)))
        self.max_sustained_freq = capacity/self.recharge_one_activation * self.ts/capacity
        # self.console.log('num steps till depletion: ' + time_till_depletion + '\nsteps till full: ' + raw_time_to_full + '\nmax_init_freq: ' + max_init_freq + '\nmax_sustained_freq: ' + max_sustained_freq)
        """activity Counters
        simplistically, we could check frequency at intervals of N*time_period_of_interest but is doing so necessary?
        let's say that we are watching a section of a conveyor belt through a window
        upon said belt we can always see 10 buckets
        every time step, the bucket on the right disappears, while a new bucket on the left appears
        Each bucket has some probability of being filled with water, or having no water
        We want to count the number of buckets that currently have water as efficiently as possible in real time, as opposed to by time sampled frequency(?) (what?
        This is so that we can regulate the probability of seeing a full bucket in order to keep it within a range of values that we deem acceptable
        That being said, it seems like these rate limits could be a result of the dynamics of the system instead of explicitly enforced
        So it seems like counting the rate should be unnecessary
        If each full bucket has a resource cost, we have a max resource capacity, and we regain resources at fixed rate
            then the frequency should naturally have an upper limit based on some func of those parameters
        these params lead to max_init_freq of 162.5
            with max_freq of 125
    # baseline_activation_rate = 0
    # session_activation_rate = 0
    # st_activation_rate = 0
        activation_rate_boundaries # methinks that ARB will need to vary for cells in different locations, and for different types of cells.
        activation rate no longer seems necessary, and can be replaced with an activation_capacity, where each activation costs X resources, which it regains at a fixed rate.
        """
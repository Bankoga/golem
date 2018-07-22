var IOrganism = {
    // internal variables shared across all types of organisms
    //sexual vs asexual// mutation chance
    details: {
        type,
        mutateRate
    },
    sleep: function(){},
    eat: function(IFud){
        // takes in any type of fud, computes the affects of the fud on the organism based on IFud physical characteristic/attributes and organism specific attributes
    },
    reproduce: function(IOrganism) {
        // the iOrg can be self or other
        // returns a new entity borked or otherwise
    },
};
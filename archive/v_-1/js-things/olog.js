var olog = {
	// this object represents the basics of an olog
	// each olog is an emergent thing which I should build from the cell level?
	// every olog is a set of things
	// it is a category, a database of all the relations, and associations with other things in the brain
	// 1 step max. This step can cross any distance

	// inputs is a layer of cells that output from other ologs to this olog
	"Inputs" : [],
	// objects is a network of cells that take data from inputs, and map it to other ologs or accepts more data from other ologs, then passes it on to the next layer
	"Objects": [],
	"": [],
	// outputs is a layer of cells that accept data from the other layers, and triggers sub cortical output, or the next logical ologs in the current chain
	// the number, and types of outputs are determined by the number of output destinations, and the requirements of said destinations
	"Outputs": [],
	// the chain is the database of olog paths that lead to the next Layer of the Olog
	// each top level olog leads to the next ologs for the following areas
	//, and this is the ologs local information about the chain
	// Chain data is used to construct processing paths, and for peer positioning in the P2P network
	// the chaincell hash is like the thalamic relay cell for a cortical column
	"ChainCell": {
		// source of data for the chain to which data is returned if it exists as well as flowing on
		"Parent": "",
		// Chain Node type determines it's B+ tree info. Note that this B+ tree is going to have each level be a Linked List
		"Type": "",
		// list of child nodes in the B+ tree used by the P2P network
		// we are going to use a B+ tree of order
		"Children": []
	}
};
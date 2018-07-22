var cell = {
	// this represents the basic unit of processing in the system
	// the chain is the database of cells, and this is the cells local information about the chain
	// Chain data is used to construct processing paths, and for peer positioning in the P2P network
	// the chaincell hash is like a the thalamic relay cell for a cortical column
	// we are going to use SOMEONE ELSEs implementation of B+ trees
	"ChainCell": {
		// source of data for the chain to which data is returned if it exists as well as flowing on
		"Parent": "",
		// Chain Node type determines it's B+ tree info. Note that this B+ tree is going to have each level be a Linked List
		"Type": "",
		// list of child nodes in the B+ tree used by the P2P network
		// we are going to use a B+ tree of order
		"Children": []
	}
}

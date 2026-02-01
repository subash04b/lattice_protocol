# Lattice Protocol: Canonical Laws (v1.0.0)

### Law I: Persistence of Anchored State
> *Requirement:* Any `ContextNode` generated as a child of a `ParentNode` must perform a deep-copy of all strings residing in `payload.anchored_terms`. 
> *Violation:* Failure to persist terms results in a **State-Orphan** error.

### Law II: Logic-Gate Divergence
> *Requirement:* If an LLM output contradicts an existing `Claim` or `Constraint` in the parent state, the system must fork the state into a new `node_id`.
> *Violation:* "Smoothing over" contradictions is classified as a **Hallucination Event**.

### Law III: Human-Verified Synthesis (Manuality)
> *Requirement:* Moving data from a high-altitude branch back to the "Ground Truth" (Altitude 0) requires a `user_signature`.
> *Violation:* Automated merging of conflicting branches is prohibited.

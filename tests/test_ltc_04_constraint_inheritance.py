def test_ltc_04_constraint_inheritance(parent_node, child_node):
    """
    LTC-04: Child nodes must inherit all constraints from their parent.
    No constraint may be dropped or silently altered.
    """

    parent_constraints = parent_node["epistemic_payload"]["constraints"]
    child_constraints = child_node["epistemic_payload"]["constraints"]

    for key, value in parent_constraints.items():
        assert key in child_constraints, (
            f"LTC-04 violation: Missing inherited constraint '{key}'"
        )
        assert child_constraints[key] == value, (
            f"LTC-04 violation: Constraint '{key}' was altered"
        )

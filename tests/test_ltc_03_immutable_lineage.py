def test_ltc_03_immutable_lineage(original_nodes, current_nodes):
    """
    LTC-03: Reasoning history must be immutable.
    No previously recorded node may be deleted or altered.
    """

    original_ids = {node["id"] for node in original_nodes}
    current_ids = {node["id"] for node in current_nodes}

    assert original_ids.issubset(current_ids), (
        "LTC-03 violation: Reasoning lineage was modified or deleted"
    )

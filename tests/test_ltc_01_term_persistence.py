def test_ltc_01_term_persistence(source_node, target_node):
    """
    LTC-01: Anchored terms must never be lost during merges.
    """
    source_terms = set(source_node["epistemic_payload"]["anchored_terms"])
    target_terms = set(target_node["epistemic_payload"]["anchored_terms"])

    assert source_terms.issubset(target_terms), (
        "LTC-01 violation: Anchored terms were removed or altered"
    )

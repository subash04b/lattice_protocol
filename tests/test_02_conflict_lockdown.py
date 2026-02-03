def test_ltc_02_conflict_lockdown(node):
    """
    LTC-02: A node in CONFLICT state must not transition to MERGED
    without explicit human authorization.
    """

    if node["meta"]["status"] == "MERGED":
        merge_event = node.get("merge_event")

        assert merge_event is not None, (
            "LTC-02 violation: MERGED without merge_event"
        )

        assert merge_event.get("user_author") is not None, (
            "LTC-02 violation: Automatic conflict resolution detected"
        )

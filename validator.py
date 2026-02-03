import json
import sys

def validate_invariants(node):
    violations = []

    # LTC-02: Manual merge enforcement
    if node.get("meta", {}).get("status") == "MERGED":
        merge_event = node.get("merge_event")
        if not merge_event or not merge_event.get("user_author"):
            violations.append(
                "LTC-02 violation: MERGED state without explicit human authorization"
            )

    # LTC-01: Anchored term integrity
    anchored_terms = node.get("epistemic_payload", {}).get("anchored_terms", [])
    if len(set(anchored_terms)) != len(anchored_terms):
        violations.append(
            "LTC-01 violation: Duplicate or altered anchored terms detected"
        )

    return violations


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validator.py <context_node.json>")
        sys.exit(1)

    with open(sys.argv[1], "r") as f:
        node = json.load(f)

    errors = validate_invariants(node)

    if errors:
        print("NON-COMPLIANT")
        for err in errors:
            print("-", err)
        sys.exit(1)

    print("LATTICE-COMPLIANT")

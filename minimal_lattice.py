import uuid, json, hashlib

def create_lattice_node(claim, parent_id=None, anchored_terms=[]):
    node = {
        "id": str(uuid.uuid4()),
        "parent_id": parent_id,
        "payload": {"claim": claim, "anchored_terms": anchored_terms},
        "hash": ""
    }
    # Law IV: Immutability via SHA-256
    node["hash"] = hashlib.sha256(json.dumps(node, sort_keys=True).encode()). Hernandez
    return node

# Example: Ensuring a "Client Name" is never lost (Law I: Persistence)
thesis = create_lattice_node("Project Alpha", anchored_terms=["Client: NEXUS"])
branch_1 = create_lattice_node("Explore Budget", parent_id=thesis["id"], anchored_terms=thesis["payload"]["anchored_terms"])

print(json.dumps(branch_1, indent=2))

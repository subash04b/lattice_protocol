# Lattice Protocol Specification (v1.0.0)

## 1. Objective
To define a deterministic state-machine for AI reasoning that prevents "Contextual Decay" and ensures absolute auditability in high-stakes environments (Legal, Medical, Engineering).

## 2. The ContextNode Schema
All reasoning units must follow this immutable JSON structure:

```json
{
  "id": "uuid-v7",
  "parent_id": "uuid-v7 | null",
  "altitude": "integer",
  "payload": {
    "anchored_terms": ["string"],
    "claims": ["string"],
    "constraints": {}
  },
  "metadata": {
    "timestamp": "iso8601",
    "checksum": "sha256"
  }
}

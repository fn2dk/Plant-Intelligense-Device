# Architecture

## Core idea

The platform is not a PDF viewer. It is an Engineering Knowledge Graph builder.

All document types follow the same generic pipeline:

1. Document ingestion
2. Page classification
3. Legend extraction
4. OCR and tag extraction
5. Symbol detection
6. Connection tracing
7. Graph generation
8. Interactive overlay
9. Engineering actions

## Diagram profiles

The core must stay generic. P&ID, SLD and electrical diagrams are implemented as diagram profiles.

A profile defines:

- Object types
- Symbol rules
- Line styles
- Connection rules
- Safety rules
- Validation rules
- Engineering actions

## Initial profiles

### P&ID

Objects: pipes, valves, pumps, tanks, filters, instruments, drains, vents.

Actions: flow trace, component isolation, affected components.

### Electrical

Objects: cables, breakers, fuses, terminals, motors, relays, panels, IO points.

Actions: feeder trace, electrical isolation, terminal path, PLC signal path.

## AI orchestration

AI must be modular. No single model should own the whole process.

Engines:

- Document Engine
- Legend Engine
- OCR Engine
- Symbol Engine
- Connection Engine
- Graph Engine
- Isolation Engine
- Excel Engine
- Validation Engine


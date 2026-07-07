# Isolation Engine

Generates engineering isolation proposals from the graph.

The output must always be treated as a proposal requiring qualified human verification.

Initial P&ID isolation logic:

1. Select component.
2. Traverse connected process lines.
3. Find nearest credible isolation valves.
4. Identify drains and vents.
5. Mark affected components.
6. Report uncertainty.

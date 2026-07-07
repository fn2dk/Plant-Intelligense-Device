# Connection Engine

Responsible for tracing engineering connections between detected components.

P&ID examples:

- pipe connects valve to pump
- instrument line connects transmitter to controller
- flow direction defines upstream and downstream

Electrical examples:

- breaker feeds cable
- cable connects terminal to motor
- relay contact controls coil or input

The first implementation will use geometry and graph rules. Later versions will combine OpenCV, OCR, learned symbols and LLM validation.

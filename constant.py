
# States
N_MASK = 0
N_OPEN = 1
N_QUARANTINE = 2
IF_SHUTDOWN = 3
IF_MOVE_CONTROL = 4
N_GOLD = 5

# Action
TRADE_MASK = 0
SET_OPEN = 1
SET_OPEN2 = 2
DEC_OPEN = 3
SWITCH_SHUTDOWN = 4
SWITCH_MOVE_CONTROL = 5
NO_ACTION = 6

ACTIONS = {
    0: 'TRADE MASK',
    1: 'SET OPEN',
    2: 'SET OPEN2',
    3: 'DEC OPEN',
    4: 'S/ SHUT',
    5: 'S/ MOVE',
    6: 'NO ACTION',
}
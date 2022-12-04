import networkx
import fairpy


def algorithm1(agents: list, rooms: list, evaluation: dict, rent: int, budget: dict) -> (int, dict):
    """
    "Fair Rent Division on a Budget", by Procaccia, A., Velez, R., & Yu, D. (2018), https://doi.org/10.1609/aaai.v32i1.11465
    The algorithm calculates Maximum-rent envy-free allocation in a fully connected economy, or in simple words,
    calculates a fair rent division under budget constraints.

    Algorithm 1: Accepts 5 inputs -
                      - N agents
                      - M rooms
                      - Evaluation of each room by agent
                      - Total rent
                      - Each agent's budget
                 Returns:
                      - The rent after calculations
                      - Dictionary of how much each agent has to pay for his room.
    Programmers: Asif Rot & Daniel Sela

    Example 1: positive numbers
    >>> algorithm1(2,3,4)
    9
    Example 2: positive and negative numbers
    >>> x=2
    >>> y=3
    >>> z=-4
    >>> algorithm1(x,y,z)
    1
    """
    return 0  # Empty implementation


def algorithm2(agents: list, rooms: list, evaluation: dict, rent: int, budget: dict) -> (int, dict):
    """
    "Fair Rent Division on a Budget", by Procaccia, A., Velez, R., & Yu, D. (2018), https://doi.org/10.1609/aaai.v32i1.11465
    The algorithm calculates fair rent division with optimal envy-free allocation subject to budget constraints.

    Algorithm 2: Accepts 5 inputs -
                      - N agents
                      - M rooms
                      - Evaluation of each room by agent
                      - Total rent
                      - Each agent's budget
                 Returns:
                      - The rent after calculations
                      - Dictionary of how much each agent has to pay for his room.
    Programmers: Asif Rot & Daniel Sela

    Example 1: positive numbers
    >>> algorithm1(2,3,4)
    9
    Example 2: positive and negative numbers
    >>> x=2
    >>> y=3
    >>> z=-4
    >>> algorithm1(x,y,z)
    1
    """
    return 0  # Empty implementation
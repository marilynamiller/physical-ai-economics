# robot_cost.py
#
# First-pass, transparent cost model for deploying and operating a
# robot / physical-AI system. Intended to be combined later with
# labor_cost.py in a scenario and NPV analysis.
#
# All figures in ROBOT_COST_ASSUMPTIONS are ILLUSTRATIVE PLACEHOLDERS
# and must eventually be replaced with sourced estimates.

from assumptions import ROBOT_COST_ASSUMPTIONS


def calculate_total_upfront_capex(assumptions):
    """Total Year-0 capital outlay for the fleet: (equipment +
    deployment/integration) x robot_fleet_size.

    Kept as its own figure (not spread over time) because the later
    NPV model must treat this as a single Year 0 cash outflow.
    """
    per_unit_capex = (
        assumptions["upfront_equipment_cost"]
        + assumptions["deployment_integration_cost"]
    )
    return per_unit_capex * assumptions["robot_fleet_size"]


def calculate_annualized_capital_cost(total_upfront_capex, useful_life_years):
    """Illustrative annualized capital-cost estimate (straight-line).

    This is total_upfront_capex / useful_life_years. It is a simple
    way to express the upfront cost on a per-year basis for a quick
    annual comparison against operating costs.

    It is NOT an actual annual cash payment (there is no financing
    or amortization schedule here) and it is NOT a tax depreciation
    schedule (no MACRS, Section 179, or tax treatment is modeled).
    The real cash flow is the full upfront amount in Year 0, which
    calculate_total_upfront_capex() reports separately.
    """
    return total_upfront_capex / useful_life_years


def calculate_annual_operating_cost(assumptions):
    """Total annual operating cost for the fleet: (maintenance +
    software/cloud + energy + insurance/support) x robot_fleet_size.
    """
    per_unit_operating_cost = (
        assumptions["annual_maintenance_cost"]
        + assumptions["annual_software_cloud_cost"]
        + assumptions["annual_energy_cost"]
        + assumptions["annual_insurance_support_cost"]
    )
    return per_unit_operating_cost * assumptions["robot_fleet_size"]


def calculate_total_annual_robot_cost(annualized_capital_cost, annual_operating_cost):
    """Total annual robot cost for a simple annual comparison.

    Combines the illustrative annualized capital-cost estimate with
    the total annual operating cost. This figure is for a rough
    annual side-by-side comparison only, not a cash-flow statement.
    """
    return annualized_capital_cost + annual_operating_cost


def print_summary(
    robot_fleet_size,
    total_upfront_capex,
    annualized_capital_cost,
    annual_operating_cost,
    total_annual_robot_cost,
):
    """Print a clean, dollar-formatted summary of the robot cost model."""
    print(f"Robot fleet size (user-specified input): {robot_fleet_size}")
    print(f"Total upfront capital expenditure:      ${total_upfront_capex:,.2f}")
    print(f"Illustrative annualized capital-cost estimate: ${annualized_capital_cost:,.2f}")
    print(f"Total annual operating cost:             ${annual_operating_cost:,.2f}")
    print(f"Total annual robot cost (for comparison): ${total_annual_robot_cost:,.2f}")


def calculate_totals(assumptions=ROBOT_COST_ASSUMPTIONS):
    """Run the full calculation chain and return results as a dict,
    so other modules (e.g. compare.py) can import these figures
    directly instead of re-deriving them.
    """
    total_upfront_capex = calculate_total_upfront_capex(assumptions)
    annualized_capital_cost = calculate_annualized_capital_cost(
        total_upfront_capex, assumptions["useful_life_years"]
    )
    annual_operating_cost = calculate_annual_operating_cost(assumptions)
    total_annual_robot_cost = calculate_total_annual_robot_cost(
        annualized_capital_cost, annual_operating_cost
    )
    return {
        "robot_fleet_size": assumptions["robot_fleet_size"],
        "total_upfront_capex": total_upfront_capex,
        "annualized_capital_cost": annualized_capital_cost,
        "annual_operating_cost": annual_operating_cost,
        "total_annual_robot_cost": total_annual_robot_cost,
    }


def main():
    totals = calculate_totals()
    print_summary(
        totals["robot_fleet_size"],
        totals["total_upfront_capex"],
        totals["annualized_capital_cost"],
        totals["annual_operating_cost"],
        totals["total_annual_robot_cost"],
    )


if __name__ == "__main__":
    main()

# compare.py
#
# Illustrative, same-year cost comparison between labor_cost.py and
# robot_cost.py.
#
# labor_cost.py states the scale of the labor operation directly
# (workers_per_shift, shifts_per_day, etc.). robot_cost.py states its
# own scale the same way, via robot_fleet_size -- a USER-SPECIFIED
# illustrative input, not derived from workload, capacity, or labor
# displacement. This script does not claim workforce replacement,
# labor savings, or equivalent output between the labor operation and
# the robot fleet. The result below is an ILLUSTRATIVE ANNUAL COST
# DIFFERENCE only, reported before any workload validation.
#
# This is also a same-year comparison only: no discounting, no
# multi-year cash flow, no NPV. The robot fleet's upfront capex is
# annualized here (straight-line, via robot_cost.py) for a same-year
# comparison, not treated as a Year 0 outflow -- that treatment
# belongs to the future NPV model.

import labor_cost
import robot_cost


def calculate_illustrative_annual_cost_difference(annual_labor_cost, total_annual_robot_cost):
    """Illustrative annual cost difference: labor_cost.py's annual
    labor cost minus robot_cost.py's total annual robot fleet cost.

    This is NOT realized savings and NOT a deployable business case.
    robot_cost.py's robot_fleet_size is a user-specified illustrative
    input, not derived from workload, capacity, or labor
    displacement, so this difference does not imply workforce
    replacement or equivalent output.
    """
    return annual_labor_cost - total_annual_robot_cost


def print_summary(annual_labor_cost, total_annual_robot_cost, illustrative_annual_cost_difference):
    """Print a clean, dollar-formatted, explicitly-labeled summary."""
    print(f"Annual labor cost:                     ${annual_labor_cost:,.2f}")
    print(f"Annual robot fleet cost:               ${total_annual_robot_cost:,.2f}")
    print(f"Illustrative annual cost difference:   ${illustrative_annual_cost_difference:,.2f}")
    print()
    print("Note: robot_cost.py's robot_fleet_size is a user-specified")
    print("illustrative input, not derived from workload, capacity, or")
    print("labor displacement. This is an illustrative annual cost")
    print("difference before workload validation -- not realized savings,")
    print("workforce replacement, or equivalent output, and not a")
    print("deployable business case.")


def main():
    total_annual_robot_cost = robot_cost.calculate_totals()["total_annual_robot_cost"]

    illustrative_annual_cost_difference = calculate_illustrative_annual_cost_difference(
        labor_cost.annual_labor_cost, total_annual_robot_cost
    )

    print_summary(
        labor_cost.annual_labor_cost,
        total_annual_robot_cost,
        illustrative_annual_cost_difference,
    )


if __name__ == "__main__":
    main()

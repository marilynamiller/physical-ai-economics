# npv.py
#
# Illustrative multi-year NPV comparison between two scenarios:
# continuing with manual labor, or deploying the robot fleet.
#
# Each scenario gets its own cash flow track and its own NPV, then
# the delta between them is reported. Cash flows are negative
# (money going out): the labor-only scenario has no Year-0 outlay
# (no equipment to buy) but pays annual_labor_cost every year; the
# robot-fleet scenario pays the fleet's full upfront capex once at
# Year 0 (robot_cost.py's total_upfront_capex) and its ongoing
# annual_operating_cost every year after. robot_cost.py's
# annualized_capital_cost (a smoothed, non-cash estimate) is
# deliberately NOT used here -- using it alongside the Year-0 lump
# sum would double-count capex.
#
# This inherits every caveat from compare.py: robot_fleet_size is a
# user-specified illustrative input, not derived from workload,
# capacity, or labor displacement. The results below are
# ILLUSTRATIVE NET PRESENT VALUES only -- not a validated business
# case, and not proof of workforce equivalence.
#
# Not modeled: taxes, depreciation (MACRS/Section 179), financing,
# residual/salvage value, inflation or cost escalation. Cash flows
# are held flat across the horizon.

import assumptions
import labor_cost
import robot_cost


def calculate_labor_scenario_cash_flows(annual_labor_cost, analysis_horizon_years):
    """Labor-only scenario: no Year-0 outlay (nothing to buy), then
    annual_labor_cost as a cash outflow (negative) every year.
    """
    return [0] + [-annual_labor_cost] * analysis_horizon_years


def calculate_robot_scenario_cash_flows(
    total_upfront_capex, annual_operating_cost, analysis_horizon_years
):
    """Robot-fleet scenario: the full upfront capex as a single
    Year-0 outflow, then annual_operating_cost as a cash outflow
    every year after.
    """
    return [-total_upfront_capex] + [-annual_operating_cost] * analysis_horizon_years


def calculate_npv(cash_flows, discount_rate):
    """Net present value: each cash flow discounted back to Year 0
    at discount_rate, then summed. cash_flows[0] is the Year-0 flow
    (undiscounted, since it already occurs at t=0).
    """
    return sum(
        cash_flow / (1 + discount_rate) ** year
        for year, cash_flow in enumerate(cash_flows)
    )


def print_summary(labor_cash_flows, robot_cash_flows, discount_rate, labor_npv, robot_npv, npv_delta):
    """Print a clean, dollar-formatted side-by-side cash flow table
    plus each scenario's NPV and the delta between them.
    """
    print(f"Discount rate (illustrative input): {discount_rate:.1%}")
    print()
    print(f"{'Year':<6}{'Labor-only':>18}{'Robot fleet':>18}")
    for year, (labor_cf, robot_cf) in enumerate(zip(labor_cash_flows, robot_cash_flows)):
        print(f"{year:<6}{labor_cf:>18,.2f}{robot_cf:>18,.2f}")
    print()
    print(f"Labor-only scenario NPV:       ${labor_npv:,.2f}")
    print(f"Robot fleet scenario NPV:      ${robot_npv:,.2f}")
    print(f"NPV delta (robot minus labor): ${npv_delta:,.2f}")
    print()
    print("Note: cash flows and NPVs above are costs shown as negative.")
    print("A less negative NPV is the less costly scenario in present-")
    print("value terms; a positive delta means the robot fleet scenario")
    print("costs less than continuing with manual labor. This is an")
    print("illustrative NPV, not a validated business case.")
    print("robot_fleet_size is a user-specified illustrative input, not")
    print("derived from workload, capacity, or labor displacement.")
    print("Taxes, depreciation, financing, residual value, and inflation")
    print("are not modeled; cash flows are held flat across the horizon.")


def main():
    robot_totals = robot_cost.calculate_totals()
    analysis_horizon_years = assumptions.NPV_ASSUMPTIONS["analysis_horizon_years"]
    discount_rate = assumptions.NPV_ASSUMPTIONS["discount_rate"]

    labor_cash_flows = calculate_labor_scenario_cash_flows(
        labor_cost.annual_labor_cost, analysis_horizon_years
    )

    robot_cash_flows = calculate_robot_scenario_cash_flows(
        robot_totals["total_upfront_capex"],
        robot_totals["annual_operating_cost"],
        analysis_horizon_years,
    )

    labor_npv = calculate_npv(labor_cash_flows, discount_rate)
    robot_npv = calculate_npv(robot_cash_flows, discount_rate)
    npv_delta = robot_npv - labor_npv

    print_summary(
        labor_cash_flows, robot_cash_flows, discount_rate, labor_npv, robot_npv, npv_delta
    )


if __name__ == "__main__":
    main()

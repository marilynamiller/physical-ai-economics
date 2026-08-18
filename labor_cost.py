# labor_cost.py

from assumptions import LABOR_ASSUMPTIONS, STANDARD_ANNUAL_HOURS_PER_FTE

# --- Assumptions (from assumptions.py) ---
workers_per_shift = LABOR_ASSUMPTIONS["workers_per_shift"]
shifts_per_day = LABOR_ASSUMPTIONS["shifts_per_day"]
hours_per_shift = LABOR_ASSUMPTIONS["hours_per_shift"]
operating_days_per_year = LABOR_ASSUMPTIONS["operating_days_per_year"]
loaded_hourly_wage = LABOR_ASSUMPTIONS["loaded_hourly_wage"]


# --- Calculation functions ---
def calculate_annual_labor_hours(
    workers_per_shift, shifts_per_day, hours_per_shift, operating_days_per_year
):
    return (
        workers_per_shift
        * shifts_per_day
        * hours_per_shift
        * operating_days_per_year
    )


def calculate_annual_labor_cost(annual_labor_hours, loaded_hourly_wage):
    return annual_labor_hours * loaded_hourly_wage


def calculate_implied_fte_requirement(annual_labor_hours, standard_annual_hours_per_fte):
    return annual_labor_hours / standard_annual_hours_per_fte


# --- Calculations ---
annual_labor_hours = calculate_annual_labor_hours(
    workers_per_shift, shifts_per_day, hours_per_shift, operating_days_per_year
)

annual_labor_cost = calculate_annual_labor_cost(annual_labor_hours, loaded_hourly_wage)

implied_fte_requirement = calculate_implied_fte_requirement(
    annual_labor_hours, STANDARD_ANNUAL_HOURS_PER_FTE
)


# --- Output ---
def main():
    print(f"Annual labor hours:  {annual_labor_hours:,.0f}")
    print(f"Annual labor cost:   ${annual_labor_cost:,.2f}")
    print(f"Implied FTE requirement: {implied_fte_requirement:,.2f}")


if __name__ == "__main__":
    main()

# labor_cost.py

# --- Assumptions ---
workers_per_shift = 4
shifts_per_day = 3
hours_per_shift = 8
operating_days_per_year = 365
loaded_hourly_wage = 38.50

STANDARD_ANNUAL_HOURS_PER_FTE = 2080

# --- Calculations ---
annual_labor_hours = (
    workers_per_shift
    * shifts_per_day
    * hours_per_shift
    * operating_days_per_year
)

annual_labor_cost = annual_labor_hours * loaded_hourly_wage

implied_fte_requirement = annual_labor_hours / STANDARD_ANNUAL_HOURS_PER_FTE

# --- Output ---
print(f"Annual labor hours:  {annual_labor_hours:,.0f}")
print(f"Annual labor cost:   ${annual_labor_cost:,.2f}")
print(f"Implied FTE requirement: {implied_fte_requirement:,.2f}")

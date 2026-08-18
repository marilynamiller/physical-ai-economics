# assumptions.py
#
# Central store for the illustrative v1 assumptions used across
# labor_cost.py, robot_cost.py, and (later) an NPV/scenario model.
# All values are illustrative placeholders and must eventually be
# replaced with sourced estimates.
#
# One dict per model, matching the calling convention robot_cost.py
# already uses (a function takes "an assumptions table" as input).
# This shape is what lets a future scenario model swap in a different
# table (e.g. an "aggressive" version) without changing any
# calculation function.

# --- Labor assumptions (labor_cost.py) ---
LABOR_ASSUMPTIONS = {
    "workers_per_shift": 4,
    "shifts_per_day": 3,
    "hours_per_shift": 8,
    "operating_days_per_year": 365,
    "loaded_hourly_wage": 38.50,
}

# Conversion constant, not a business assumption -- kept separate
# from LABOR_ASSUMPTIONS for the same reason it was originally
# written in ALL_CAPS: it's a fixed unit conversion (40hr/wk x
# 52wk), not something the model varies.
STANDARD_ANNUAL_HOURS_PER_FTE = 2080

# --- Robot cost assumptions (robot_cost.py) ---
ROBOT_COST_ASSUMPTIONS = {
    "upfront_equipment_cost": 150_000,          # robot/equipment acquisition, $ per unit
    "deployment_integration_cost": 25_000,      # install/integration, $ per unit
    "useful_life_years": 5,                     # years, for annualizing capex only
    "annual_maintenance_cost": 12_000,          # $/year per unit
    "annual_software_cloud_cost": 6_000,        # $/year per unit (licenses, cloud, subscriptions)
    "annual_energy_cost": 3_000,                # $/year per unit
    "annual_insurance_support_cost": 4_000,     # $/year per unit (insurance, support contracts, etc.)
    # USER-SPECIFIED illustrative input. NOT derived from workload,
    # capacity, or labor displacement. All per-unit cost lines above
    # are scaled uniformly by this fleet size (v1 simplification --
    # does not distinguish fixed/shared costs from per-unit costs).
    "robot_fleet_size": 4,
}

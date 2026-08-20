# assumptions.py
#
# Central store for the v1 assumptions used across labor_cost.py,
# robot_cost.py, and npv.py.
#
# Cost figures below are sourced to public market data where noted
# (see each inline comment; full citations in README.md). Scenario-
# shape assumptions -- shift structure, fleet size -- are illustrative
# choices describing the modeled scenario, not market prices, and are
# labeled as such. See README.md for the real-world scenario this
# data is sourced against (a 3PL/fulfillment center automating
# intra-facility pallet/tote transport with transport-class AMRs).
#
# One dict per model, matching the calling convention robot_cost.py
# already uses (a function takes "an assumptions table" as input).
# This shape is what lets a future scenario model swap in a different
# table (e.g. an "aggressive" version) without changing any
# calculation function.

# --- Labor assumptions (labor_cost.py) ---
LABOR_ASSUMPTIONS = {
    # Scenario shape, not a market price: a 4-person transport team per shift.
    "workers_per_shift": 4,
    "shifts_per_day": 3,               # scenario shape: 24/7 coverage
    "hours_per_shift": 8,              # scenario shape
    "operating_days_per_year": 365,    # scenario shape: continuous operation
    # Sourced: BLS median base wage for laborers/material movers,
    # $18.12/hr (May 2024), loaded ~55% for benefits, payroll taxes,
    # and night-shift differential across a 3-shift rotation.
    "loaded_hourly_wage": 28.00,
}

# Conversion constant, not a business assumption -- kept separate
# from LABOR_ASSUMPTIONS for the same reason it was originally
# written in ALL_CAPS: it's a fixed unit conversion (40hr/wk x
# 52wk), not something the model varies.
STANDARD_ANNUAL_HOURS_PER_FTE = 2080

# --- Robot cost assumptions (robot_cost.py) ---
ROBOT_COST_ASSUMPTIONS = {
    # Sourced: transport-class AMR (500-1,500kg payload), $30k-$80k
    # market range; $ per unit.
    "upfront_equipment_cost": 50_000,
    # Sourced: integration typically adds 40-60% of unit price; $ per unit.
    "deployment_integration_cost": 25_000,
    # Sourced: US tax law robotics depreciation class (5yr); AMR-specific
    # depreciation commonly 3-5yr. Years, for annualizing capex only.
    "useful_life_years": 5,
    # Sourced: warehouse AMR maintenance, 6-10% of purchase price; $/year per unit.
    "annual_maintenance_cost": 4_000,
    # NOT independently sourced -- vendors bundle this into all-in RaaS
    # pricing, so a software-only figure isn't cleanly observable.
    # Low-confidence placeholder; $/year per unit.
    "annual_software_cloud_cost": 6_000,
    # Sourced: AMR charging electricity, $300-$1,500/year range; $/year per unit.
    "annual_energy_cost": 900,
    # Sourced: robot property insurance, $500-$5,000/year per unit
    # (support cost bundled in here, not independently sourced).
    "annual_insurance_support_cost": 4_000,
    # USER-SPECIFIED illustrative input. NOT derived from workload,
    # capacity, or labor displacement. All per-unit cost lines above
    # are scaled uniformly by this fleet size (v1 simplification --
    # does not distinguish fixed/shared costs from per-unit costs).
    "robot_fleet_size": 4,
}

# --- NPV assumptions (npv.py) ---
NPV_ASSUMPTIONS = {
    # Sourced: median US mature-company cost of capital, ~8.35%
    # (Damodaran, 2025 data), rounded.
    "discount_rate": 0.08,
    "analysis_horizon_years": 5,    # years projected; independent of useful_life_years above,
                                     # defaulted to match it for v1
}

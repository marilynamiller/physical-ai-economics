# Physical AI Economics

A Python-based scenario model comparing the deployment economics of
a hypothetical autonomous robot fleet against continuing with manual
human labor.

## Status

v1 complete: labor cost, robot fleet cost, and a multi-year NPV
comparison between the two scenarios, with cost assumptions sourced
to public market data (see Scenario and Data Sources below).

Known limitations: robot fleet size is a user-specified input, not
derived from workload or capacity data, so the model does not
establish that the robot fleet and labor operation perform
equivalent work. Taxes, depreciation, financing, residual value, and
inflation are not modeled. Two cost line items (software/cloud,
bundled insurance/support) could not be independently sourced. No
automated tests exist.

## Scenario

The v1 assumptions in `assumptions.py` are sourced against a
real-world example: a mid-size third-party logistics (3PL) or
e-commerce fulfillment center automating intra-facility pallet/tote
transport. A team of 4 workers per shift currently moves pallets and
totes between receiving, storage, and pick/pack/ship zones using
pallet jacks and tuggers, across 3 shifts, 24/7/365. The model
compares that labor cost against deploying a fleet of transport-class
autonomous mobile robots (AMRs, 500-1,500kg payload) sized to cover
the same work.

Shift structure and fleet size (`workers_per_shift`, `shifts_per_day`,
`robot_fleet_size`, etc.) describe this scenario and are illustrative
choices, not sourced market data. Cost figures (wages, robot pricing,
maintenance, energy, insurance, discount rate) are sourced to public
market data as of August 2026; see Data Sources below.

## Data Sources

- [Fully Burdened Labor Rate: Calculate Your True Labor Costs](https://smartbarrel.io/blog/fully-burdened-labor-rate/)
- [Hand Laborers and Material Movers : Occupational Outlook Handbook (BLS)](https://www.bls.gov/ooh/transportation-and-material-moving/hand-laborers-and-material-movers.htm)
- [How Much Does an AMR Cost in 2026? Price Guide (Mesh Automation)](https://meshautomationinc.com/amr-cost-2026/)
- [Warehouse robot cost in 2026: AMR, AGV, and RaaS ranges (PickTheRobot)](https://picktherobot.com/blog/warehouse-robot-cost-2026)
- [How Much Does It Cost to Automate a Warehouse? (Axelent)](https://www.axelent.com/us/safety-hub/automated-warehouse-solutions/how-much-does-it-cost-to-automate-a-warehouse)
- [Warehouse Automation Budget Guide: From $50K Pilots to $5M Deployments (Robotomated)](https://robotomated.com/learn/cost/warehouse-automation-budget-guide)
- [Autonomous Mobile Robots: Costs, ROI and Potential Savings (Knapp)](https://www.knapp.com/en/insights/blog/autonomous-mobile-robots-costs-roi-potential-savings/)
- [Annual Robot Maintenance Costs: What to Budget Beyond the Purchase Price (Robotomated)](https://robotomated.com/learn/cost/robot-maintenance-cost-annual)
- [Robotics-as-a-Service (RaaS) Business Models (TechTimes)](https://www.techtimes.com/articles/314939/20260304/robotics-service-raas-business-models-how-subscription-robotics-transforming-industries.htm)
- [AGV & AMR Charging: Complete Guide to Warehouse Robot Chargers](https://www.stchargers.com/news/agv-amr-charging-complete-guide-to-warehouse-robot-chargers/)
- [Insurance for Robotics (Branco Insurance Group)](https://brancoinsurancegroup.com/insurance-for-robotics/)
- [Data Update 6 for 2025: The Hurdle Rate Question (Damodaran)](https://aswathdamodaran.blogspot.com/2025/02/data-update-6-for-2025-from-macro-to.html)

Note: cost figures are directional estimates from vendor and industry
publications, not audited or contractually binding quotes. Several
line items (software/cloud cost, bundled insurance and support) could
not be independently sourced and remain lower-confidence placeholders
-- see inline comments in `assumptions.py`.
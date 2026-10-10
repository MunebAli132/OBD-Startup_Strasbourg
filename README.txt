OBD SmartCare mock CSV dataset
=================================
All records are fictional and for software development/testing only.
No live OBD-II data was collected. No real customer identifiers are included.
VIN and registration number fields are intentionally blank.

Files:
- garages.csv: demo garage tenants
- customers.csv: fictional customer records
- vehicles.csv: fictional vehicles
- dtc_reference.csv: sample generic powertrain code definitions
- diagnostic_reports.csv: sample report headers
- report_codes.csv: fault codes linked to reports
- obd_smartcare_master.csv: flattened table for quick demo/import

Important:
- Code descriptions are generic; consult authoritative vehicle-specific service information.
- A fault code does not prove that a particular component has failed.
- All finding_status values are unverified in this sample.
- IDs are synthetic. Adapt column names and types to your Django models before importing.

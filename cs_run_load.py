""""Load cs_run.py on ArcGIS virtual machine."""

import imp


cs_run = imp.load_source(
    "cs_run", 
    "F:\\cs-workspace\\cs_testing\\cs-test-cli\\cs_run.py")

# cs_run.main(cs_config_file)

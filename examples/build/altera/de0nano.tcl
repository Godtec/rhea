#
#
# Quartus II implementation script
# created: Fri, 01 Apr 2016 02:14:53 +0000
# by: ex_de0nano.py
#
#
# See also: http://www.altera.com/support/excamples/tcl/open_project.html
cd altera/
load_package flow
project_open de0nano
#set_global_assignment -name PROJECT_OUTPUT_DIRECTORY .
# Synopsys design constraints, .sdc must exist
# Quartus settings, .qsf, must exist (created from .qdf?)
# Extra pin assignments
#set_location_assignment -to clk PIN_BLA
# You can define multiple clocks with a fixed relation, (not here)
execute_flow -compile
project_close
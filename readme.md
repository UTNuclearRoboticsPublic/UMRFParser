# Purpose
The parser provided in this package is an implementation of the t5-small parser with language model head for conditional generation. 

The semantic parsing task:
converting natural language commands -> The Unified Meaning Representation (UMRF). This format powers the TeMoto2.0 packaged developed by the University of Tartu and University of Texas at Austin.

# How to Install
1) clone this repository into your <code> ~/catkin_ws/src </code>
2) Download the model and tokenizer from slwanna@utexas.edu 's google drive (please contact author of this git repo for access)
3) from <code> ~/catkin_ws/src/ROS1_UMRF_T5Parser/scripts</code> run <code>pip install -r requirements.txt</code> 
4) Extract the zip in your download then place the <code>saved_model</code> and <code>saved_tokenizer</code> at the same directory level as the <code>umrf_parser.py</code>

# How to Use
1) No <code>.launch</code> is included
2) source your workspace
3) start <code>roscore</code> in a terminal
4) navigate to <code>~/catkin_ws/src/ROS1_UMRF_T5Parser/scripts</code>
5) <code>python3 umrf_parser.py</code>

This will being running the node. The node listens to natural language commands on the <code>rostopic</code> : <code>umrf_parses</code>. The UMRF outputs are published on <code>umrf_parses_output</code>.

# Future Work
1) Provide a RoboFrameNet Parser
2) Implement online learning model for live UMRF corrections

Once the package is installed it can be called using command: 
greengraph
This will run the default settings of New York to Chicago with 20 
and will output a graph but will not save it. It can also be called 
with arguments:
-h             
--from "start"
--to "end"
--steps "steps"
--out "your file name"
An example call of this is:
greengraph --from London --to Oxford --steps 10 --out graph.png
This will, as well as displaying the graph, save it as graph.png to your
local directory.
Calling with -h will display the on screen help


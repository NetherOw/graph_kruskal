Kruskal's algowithm on adjacency lists and adjacency matrix on weighted undirected graphs
Search of a minimal spanning tree by looking at minimal unused edge weight, checking whether, if added, such edge creates a cycle. If no - add it.
This project is aimed to generate respective graphs, execute the algorithm, but, most importantly, to evaluate algorithms runtime difference between different graph representations.

List algorithm is executed via launching a single respective Python file, runtime results will be outputted to runtime.csv. Parameters can be changed in aforementioned  .py file.

Matrix algorithm is executed via launching longtimerunner.py file, where you can change node and density values that are checked. Runtime is calculated via taking 5 packages of 20 files, that are also outputted in real time to separate txt files while the script is running - changing amount of matrices generated/checked per amount of parameters is not supported. Maximum edge weight can be changed in generator.py. 
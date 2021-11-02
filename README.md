# MERCHANT-S-GUIDE-TO-THE-GALAXY
Test Framework: pytest. 

Test Input        ->    Test Output:

pish tegj glob glob   ->  42 

glob prok Silver      ->  68 Credits 

glob prok Gold        ->  57800 Credits  

glob prok Iron        ->  782 Credits  

glob glob glob glob   ->  invalid Value!

how much wood coulda woodchuck chuck if a woodchuck could chuck wood ?  ->  No idea what you are talking about


Main script: GUI.py

GUI.py imports converter.py

converter.py imports convert.py

converter.py contains Converter class. It is called by GUI.py. The class checks whether the input is galaxy currency or not. If it is galactic currency it calls convert.py. The class returns the converted currency.

convert.py contains all convertions steps

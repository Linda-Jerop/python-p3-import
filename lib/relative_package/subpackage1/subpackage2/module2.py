from .module1 import function1  # imports function1 from module1 in same directory
from .. import module3  # imports module3 from parent directory (subpackage1)

function1()  # calls function1 from module1
module3.function1()  # calls function1 from module3
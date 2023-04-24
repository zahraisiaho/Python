import module
module.nameit("James")

module.device("that")

y = module.details["age"]
print(y)

y = module.details["firstname"]
print(y)

#to rename a module:
import module as mymodules
mymodules.nameit("John")
import yaml 

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

if __name__ == '__main__':
    with open("foo.yaml", 'r') as stream:
        dictionary = yaml.load(stream, Loader=Loader)
        for key, value in dictionary.items():
            print (key + " : " + str(value))

#if  we are getting the attribute error.
# import yaml 

# try:
#     from yaml import CLoader as Loader
# except ImportError:
#     from yaml import Loader

# if __name__ == '__main__':
#     with open("foo.yaml", 'r') as stream:
#         dictionary = yaml.load(stream, Loader=Loader)
#         if dictionary is not None:
#             for key, value in dictionary.items():
#                 print (key + " : " + str(value))
#         else:
#             print("Error: The YAML data is empty or contains invalid syntax.")


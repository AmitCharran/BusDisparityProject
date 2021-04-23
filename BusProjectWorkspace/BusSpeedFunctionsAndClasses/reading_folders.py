import os

class reading_folder:
    def __init__(self, basepath = "No_input"):
        self.basepath = basepath
        self.answer_array = []

    def printfile(self, basepath = ""):
        if basepath == "":
            basepath = self.basepath
        if basepath == 'No_input':
            print("No input")
            return

        entries = os.listdir(basepath)
        for entry in entries:
            if os.path.isfile(os.path.join(basepath,entry)):
                if entry != '.DS_Store':
                    output = basepath + "/" + entry
                    # print(output + "\n")
                    self.answer_array.append(output)
            else :
                next = os.path.join(basepath,entry)
                self.printfile(next)




# basepath = '/Users/amitc/Desktop/BusDisparityProject'
# test = reading_folder(basepath)
# test.printfile()
#
# print(test.answer_array)

# basepath = '/Users/amitc/Desktop/BusDisparityProject/BusProjectWorkspace'
# entries = os.listdir(basepath)
# def printfile(basepath):
#     entries = os.listdir(basepath)
#     for entry in entries:
#         if os.path.isfile(os.path.join(basepath,entry)):
#             if entry != '.DS_Store':
#                 print (entry + "\n")
#         else :
#             next = os.path.join(basepath,entry)
#             printfile(next)
#
# printfile(basepath)
#
# def calculate_average_from_folder(self, folder_path):
#     f = []
#     for (dirpath, dirnames, filenames) in walk(folder_path):
#         f.extend(filenames)
#         break
#
#     answer_dictionary = {}
#
#     for filename in f:
#         if filename != '.DS_Store':
#             file_path = folder_path + '/' + filename
#             dictionary = self.calculate_average_from_file_return_dictionary(file_path)
#
#             answer_dictionary = self.average_dictionary_together(answer_dictionary, dictionary)
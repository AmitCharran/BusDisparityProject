def calculate_average_from_folder(self, folder_path):
    f = []
    for (dirpath, dirnames, filenames) in walk(folder_path):
        f.extend(filenames)
        break

    answer_dictionary = {}

    for filename in f:
        if filename != '.DS_Store':
            file_path = folder_path + '/' + filename
            dictionary = self.calculate_average_from_file_return_dictionary(file_path)

            answer_dictionary = self.average_dictionary_together(answer_dictionary, dictionary)
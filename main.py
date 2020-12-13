import os


class InvalidFilenameCorrecter:

    def __init__(self, path):
        self.path = path
        self.invalid_dir_count = 0
        self.invalid_file_count = 0
        self.files_in_invalid_dir = 0
        self.invalid_char_set = ('"', '*', ':', '<', '>', '\\' '?', '|')

    def invalid_characters(self, filename):
        """ This method returns True if invalid characters were detected """

        for c in self.invalid_char_set:
            if c in filename:
                return True

        return False

    def filename_correcter(self):
        """ This method ... """

        # Return all directories and files with os.walk
        full_directory = os.walk(self.path)

        # Iterate over all directories
        for directories in full_directory:
            filepath = directories[0]

            if self.invalid_characters(filepath):
                print('Invalid Directory Path: ', filepath)
                self.replace_invalid_characters(filepath)

                # increment counters
                self.invalid_dir_count += 1
                self.files_in_invalid_dir += len(directories[2])

                # Todo: rename

            # Iterate over all files in currently selected directory
            for filename in directories[2]:
                if self.invalid_characters(filename):

                    # increment counters
                    self.replace_invalid_characters(filename)
                    self.invalid_file_count += 1
                    print(filename)

                    # Todo: rename

    def get_result(self):
        print(self.invalid_dir_count, 'invalid directory names have been found.')
        print(self.invalid_file_count, 'invalid filenames have been found.')
        print(self.files_in_invalid_dir, 'files in invalid directories that might not be synced.')
        print('Total: ', self.invalid_file_count + self.invalid_dir_count + self.files_in_invalid_dir)

    def replace_invalid_characters(self, string):
        for c in self.invalid_char_set:
            if c in string:
                print(c)
                string.replace(c, '_')

        print('corrected: ', string)
        return string


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test = InvalidFilenameCorrecter('/Users/benediktkau/OneDrive - University College London')
    test.filename_correcter()
    test.get_result()

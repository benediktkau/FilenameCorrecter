import os


class InvalidFilenameCorrecter:

    def __init__(self, path):
        self.path = path
        self.invalid_dir_count = 0
        self.invalid_file_count = 0

    @staticmethod
    def invalid_characters(filename):
        """ This method returns True if invalid characters were detected """
        invalid_characters = ('"', '*', ':', '<', '>', '?', '|')

        for c in invalid_characters:
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
                self.invalid_dir_count += 1
            else:
                print('Directory: ', filepath)

            # Iterate over all files in currently selected directory
            for filename in directories[2]:
                if self.invalid_characters(filename):
                    self.invalid_file_count += 1
                    print(filename)

    def get_result(self):
        print(self.invalid_dir_count, 'invalid directory names have been found.')
        print(self.invalid_file_count, 'invalid filenames have been found.')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test = InvalidFilenameCorrecter('/Users/benediktkau/Google Drive')
    test.filename_correcter()
    test.get_result()

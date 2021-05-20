import os


class FindFiles:

    def find_all_file(self, work_path, option=0):
        work_path = work_path
        file_list = []

        if option==0:
            for (path, dir, files) in os.walk(work_path):
                for filename in dir:
                    file_list.append(filename)
                for filename in files:
                    file_list.append(filename)
        elif option == 1:
            for (path, dir, files) in os.walk(work_path):
                for filename in files:
                    file_list.append(filename)
        elif option == 2:
            for (path, dir, files) in os.walk(work_path):
                for filename in dir:
                    file_list.append(filename)
        else:
            return 'no option'

        return file_list

    def find_current_file(self, work_path, option=0):
        work_path = work_path
        file_list = []

        if option==0:
            file_list = os.listdir(work_path)
        elif option == 1:
            for entry in os.listdir(work_path):
                if os.path.isfile(os.path.join(work_path, entry)):
                    file_list.append(entry)
        elif option == 2:
            for entry in os.listdir(work_path):
                if os.path.isdir(os.path.join(work_path, entry)):
                    file_list.append(entry)
        else:
            return 'no option'

        return file_list

    def find_by_filename(self, work_path ,find ):
        work_path =work_path
        file_list = []

        for (path, dir, files) in os.walk(work_path):
            for filename in files:
                if filename.find(find)>-1:
                    file_list.append(filename)

        return file_list

    def find_by_type(self, work_path, filetype):
        work_path =work_path
        file_list = []

        for (path, dir, files) in os.walk(work_path):
            for filename in files:
                ext = os.path.splitext(filename)[-1]
                if ext[1:] == filetype:
                    file_list.append(filename)

        return file_list


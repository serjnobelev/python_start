
class Folder(object):
    _max_size = 7
    exist_files = []

    def __init__(self):
        self.folder_size = self._max_size

    def delete(self, file):
        if file.size <= self.free_space():
            self.exist_files.append(file)
            print('File deleted')
        else:
            print('No free space')

    def free_space(self):
        exist_size = 0
        for file in self.exist_files:
            exist_size += file.size
        return self.folder_size - exist_size


class Recycle(Folder):
    def __init__(self, folder_size):
        if folder_size:
            self.folder_size = folder_size
        else:
            self.folder_size = self._max_size


class File(object):
    def __init__(self, size):
        self.size = size

rec = Recycle(7)
file1 = File(3)
file2 = File(2)
file3 = File(3)

rec.delete(file1)
rec.delete(file2)
rec.delete(file3)

for file in rec.exist_files:
    print(file.size)
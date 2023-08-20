import os
import GenerateGames
import shutil


class DesktopCleaner:

    def __init__(self):
        self.desktop = "C:/Users/Conno/Desktop"

        self.files = {
            "mp3": "C:/Users/Conno/Desktop/Shortcuts/Music",
            "wav": "C:/Users/Conno/Desktop/Shortcuts/Music",
            "csv": "C:/Users/Conno/Desktop/Shortcuts/CSVs",
            "jpg": "C:/Users/Conno/Desktop/Shortcuts/Photos",
            "png": "C:/Users/Conno/Desktop/Shortcuts/Photos",
            "pptx": "C:/Users/Conno/Desktop/Shortcuts/Powerpoints",
            "txt": "C:/Users/Conno/Desktop/Shortcuts/Text",
            "url": "C:/Users/Conno/Desktop/Shortcuts/URLs",
            "mp4": "C:/Users/Conno/Desktop/Shortcuts/Videos",
            "mov": "C:/Users/Conno/Desktop/Shortcuts/Videos",
            "docx": "C:/Users/Conno/Desktop/Shortcuts/Word",
            "lnk": "C:/Users/Conno/Desktop/Shortcuts/Other"

        }

    # Returns the file extension
    def getFileExtension(self, file):
        return file[-3:]

    # Returns a set of the users game from the steam api
    def getGames(self):
        games = []

        GenerateGames.generateFile(76561198346676755)  # generates users steam games

        with open("steamgames.txt") as f:
            for line in f:
                line = line.rstrip("\n")
                games.append(line)

        return set(games)

    # Moves files to their correct location
    def moveFiles(self):
        for files in os.walk(self.desktop):
            if files[0] == self.desktop:

                for list in files:

                    for file in list:
                        cur_path = os.path.join(self.desktop, file)
                        file_extension = self.getFileExtension(file)
                        print(file, file[:-4])

                        if file_extension in self.files and file[:-4] not in self.getGames():
                            new_path = os.path.join(self.desktop, self.files[file_extension]) # Create a path from the desktop + the file extension path
                            shutil.move(cur_path, new_path)
                            print(f"Moved '{file}' to '{new_path}'")

                        elif file_extension in self.files and file[:-4] in self.getGames():
                            new_path = "C:/Users/Conno/Desktop/Shortcuts/Games"
                            shutil.move(cur_path, new_path)
                            print(f"Moved '{file}' to '{new_path}'")
                        elif len(file) >3 and file != "Shortcuts":
                            new_path = "C:/Users/Conno/Desktop/Shortcuts/Other"
                            shutil.move(cur_path, new_path)
                            print(f"Moved '{file}' to '{new_path}'")





d = DesktopCleaner()
d.moveFiles()

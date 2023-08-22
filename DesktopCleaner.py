import os
import GenerateGames
import shutil


class DesktopCleaner:

    def __init__(self):
        self.desktop = "C:/Users/Conno/Desktop"
        self.excludedFilesList = []
        self.gamesList = []

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

    # Sets files to be ignored by the cleaner
    def getExcludedFiles(self):

        with open("excludedFiles.txt") as excludedFiles:
            for line in excludedFiles:
                line = line.rstrip("\n")
                self.excludedFilesList.append(line)

            return set(self.excludedFilesList)

    # Returns a set of the users game from the steam api
    def getGames(self):
        games = []

        GenerateGames.generateFile(76561198346676755)  # generates users steam games

        with open("steamgames.txt") as gamesFile:
            for line in gamesFile:
                line = line.rstrip("\n")
                self.gamesList.append(line)

        return set(self.gamesList)

    # Moves files to their correct location
    def moveFiles(self):

        # Scan files on desktop
        for files in os.walk(self.desktop):
            if files[0] == self.desktop:

                # Iterate through list of files on desktop
                for filesList in files:

                    for file in filesList:
                        cur_path = os.path.join(self.desktop, file)
                        file_extension = self.getFileExtension(file)
                        fileName = file[:4]  # remove last 4 chars from string

                        # if extension in dict and filename not in games and file not excluded, add to correct file
                        if file_extension in self.files and fileName not in self.getGames() \
                                and file not in self.getExcludedFiles():

                            new_path = os.path.join(self.desktop, self.files[
                                file_extension])  # Create a path from the desktop + the file extension path
                            shutil.move(cur_path, new_path)
                            print(f"Moved '{file}' to '{new_path}'")

                        # If extension in dict, and filename in games list and file not excluded from cleaning, then add to 'games' folder
                        elif file_extension in self.files and fileName in self.getGames() \
                                and file not in self.getExcludedFiles():

                            new_path = "C:/Users/Conno/Desktop/Shortcuts/Games"
                            shutil.move(cur_path, new_path)
                            print(f"Moved '{file}' to '{new_path}'")

                        # If a file and not the shortcuts folder and file not excluded from cleaning, then add to 'other' folder
                        elif len(file) > 3 and file != "Shortcuts" and file not in self.getExcludedFiles():
                            new_path = "C:/Users/Conno/Desktop/Shortcuts/Other"
                            shutil.move(cur_path, new_path)
                            print(f"Moved '{file}' to '{new_path}'")


d = DesktopCleaner()
d.moveFiles()

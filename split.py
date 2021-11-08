import glob
import os
import os.path
import subprocess


class CUEtool:
    def __init__(self):
        self.starting_dir = os.getcwd()
        self.name = "%n %t"
        self.dirs = []

    def doubles(self):
        [self.dirs.append(t[0]) for t in os.walk(self.starting_dir)]
        for dir in self.dirs:
            os.chdir(dir)
            print(dir)
            cues = glob.glob('*.cue')
            if len(cues) > 1:
                print("There are more than 1 cue file in the directory")
                for cue_file in cues:
                    if glob.glob('*ISRC*.cue'):
                        isrc_cue = glob.glob('*ISRC*.cue')
                        for isrc in isrc_cue:
                            print(isrc)
                            print("Removing " + isrc)
                            subprocess.call(["rm", "-rf", isrc])
                            cues.remove(cue_file)
                if len(cues) > 1:
                    for cue_file in cues:
                        flac_file = cue_file.replace('.cue', '.flac')
                        directory = cue_file.replace('.cue', '')
                        os.mkdir(directory)
                        subprocess.call(["mv", cue_file, directory])
                        subprocess.call(["mv", flac_file, directory])
                        # new_dir = dir + "/" + directory
                        # self.dirs.append(new_dir)
                        self.dirs = []

    def run_app(self, com_exe):
        if not self.dirs:
            [self.dirs.append(t[0]) for t in os.walk(self.starting_dir)]
        # print(self.dirs)
        for dir in self.dirs:
            os.chdir(dir)
            print(dir)
            for cue in glob.glob('*.cue', recursive=True):
                print(cue)
                find_flac = cue.replace('.cue', '.flac')
                if com_exe == 'cue':
                    print("Looking for *.flac.cue files")
                    if glob.glob('*.flac.cue'):
                        cue_file = glob.glob('*.flac.cue')[0]
                        cue_file = cue_file.replace('.flac', '')
                        print("Fixing flac.cue files")
                        subprocess.call("mv *.flac.cue " + "'" + cue_file + "'", shell=True)
                if com_exe == 'split':
                    print("Splitting FLAC into separate tracks")
                    if os.path.isfile(find_flac):
                        print("A Pair CUE&FLAC has been found")
                        subprocess.run(["shnsplit", "-f", cue, "-t", self.name, "-o", "flac", find_flac, "-O", "always"])
                        subprocess.run(["rm", "-f", find_flac])
                elif com_exe == 'pregap':
                    if os.path.isfile('00 pregap.flac'):
                        print("Removing '00 pregap.flac file'")
                        subprocess.call("rm -f '00 pregap.flac'", shell=True)
                elif com_exe == 'tag':
                    if not os.path.isfile(find_flac):
                        print("Creating tags from the file: " + cue)
                        new_cue = cue.replace("'", " ")
                        if new_cue != cue:
                            subprocess.call(["mv", cue, new_cue])
                            cue = new_cue
                        subprocess.call("/usr/bin/cuetag " + "'" + cue + "'" + " *.flac", shell=True)
                        subprocess.run(["rm", "-f", cue])
                    else:
                        print("There is no cue+flac pair found, or these files have different names")


if __name__ == '__main__':
    run = CUEtool()
    run.doubles()
    comms = ['cue', 'split', 'pregap', 'tag']
    for com_exe in comms:
        run.run_app(com_exe)



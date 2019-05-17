import pathlib
import logging

import opensfm.commands.extract_metadata as em
import opensfm.commands.detect_features as df
import opensfm.commands.match_features as mf
import opensfm.commands.create_tracks as ct
import opensfm.commands.reconstruct as rec
import opensfm.commands.mesh as mesh
import opensfm.commands.undistort as udst
import opensfm.commands.compute_depthmaps as cd
from opensfm import log

log.setup()

class Arguments:
    dataset = ""
    interactive = None
    def __init__(self, directory_path):
        path = pathlib.Path(directory_path)
        if not path.is_dir(): raise IsADirectoryError("Это не директория")
        if not path.exists(): raise FileExistsError("Директория c фотографиями не найдена")
        self.dataset = path.absolute()

class osfm_api:
    
    def __init__(self, directory_path):
        self.args = Arguments(directory_path)

    def extract_metadata(self):
        command = em.Command()
        command.run(self.args)

    def detect_features(self):
        command = df.Command()
        command.run(self.args)

    def match_features(self):
        command = mf.Command()
        command.run(self.args)

    def create_tracks(self):
        command = ct.Command()
        command.run(self.args)

    def reconstruct(self):
        command = rec.Command()
        command.run(self.args)

    def mesh(self):
        command = mesh.Command()
        command.run(self.args)

    def undistort(self):
        command = udst.Command()
        command.run(self.args)

    def compute_depthmaps(self):
        command = cd.Command()
        command.run(self.args)

    def run(self):
        self.extract_metadata()
        self.detect_features()
        self.match_features()
        self.create_tracks()
        self.reconstruct()
        self.mesh()
        self.undistort()
        self.compute_depthmaps()


if __name__ == "__main__":
    app = osfm_api("./data/test_api")
    #app = osfm_api("./data/berlin")
    app.run()
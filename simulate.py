import os
from lxml import etree

import mujoco
import mujoco.viewer

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
URDF_PATH = os.path.join(SCRIPT_PATH, "resources/solo12.urdf")
SRDF_PATH = os.path.join(SCRIPT_PATH, "resources/solo12.srdf")

def load_descriptions():
    # Load URDF, modify "package://" URIs and add mesh path configuration:
    urdf = etree.parse(URDF_PATH)
    root = urdf.getroot()

    names = [l.get("name") for l in root.iter("link")]
    print(len(names), len(set(names)))
    # mj_options = etree.SubElement(root, "mujoco")
    # cmp_options = etree.SubElement(mj_options, "compiler")

    # cmp_options.set("strippath", "false")

    # rel_path = "resources/meshes/stl"
    # cmp_options.set("meshdir", os.path.join(SCRIPT_PATH, rel_path))

    # # Provide the path for each mesh relative to the stl/ directory:
    # for mesh in root.iter("mesh"):
    #     path = mesh.get("filename")
    #     mesh.set("filename", path[path.find(rel_path) + len(rel_path) + 1:])
    
    # return urdf.write(URDF_PATH + ".urdf")

if __name__ == "__main__":
    load_descriptions()
    # mujoco.viewer.launch()
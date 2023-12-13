import trimesh
from pathlib import Path

# This is a simple utility that discovers all .obj
# files under the current directory and counts the total
# number of vertices and faces.
if __name__ == "__main__":
    faces, verts = 0, 0
    for f in Path("./").rglob("*.obj"):
        print("Loading...", f)
        mesh = trimesh.load(f)
        
        faces += mesh.faces.shape[0]
        verts += mesh.vertices.shape[0]
        del mesh
       
    print()
    print("Verts: ", verts)
    print("Faces: ", faces)
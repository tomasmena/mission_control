import rhinoscriptsyntax as rs
from compas.utilities import geometric_key
from compas.datastructures import Mesh
from compas_rhino.artists.meshartist import MeshArtist


srfs = rs.ObjectsByLayer('Layer 01')

gk_dict = {}
for srf in srfs:
    pts = rs.SurfacePoints(srf)[:3]
    for pt in pts:
        gk = geometric_key(pt)
        gk_dict[gk] = pt

key_index = {k:i for i, k in enumerate(gk_dict)}

faces = []
for srf in srfs:
    pts = rs.SurfacePoints(srf)[:3]
    face = [key_index[geometric_key(pt)] for pt in pts]
    faces.append(face)

vertices = [gk_dict[k] for k in gk_dict]
mesh = Mesh.from_vertices_and_faces(vertices, faces)
mesh.to_json('mesh.json')

# draw mesh in rhino - - -
# v, f = mesh.to_vertices_and_faces()
# rs.AddMesh(vertices, faces)

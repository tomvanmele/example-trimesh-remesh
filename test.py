import compas
from math import radians
from compas.datastructures import Mesh
from compas.geometry import Point, Rotation, Scale, Translation
from compas.geometry import trimesh_remesh

before = Mesh.from_ply(compas.get_bunny())

before.cull_vertices()

T = Translation.from_vector(Point(0, 0, 0) - Point(* before.centroid()))
S = Scale.from_factors([100, 100, 100])
R = Rotation.from_axis_and_angle([1, 0, 0], radians(90))

before.transform(R * S * T)

L = sum(before.edge_length(*edge) for edge in before.edges()) / before.number_of_edges()

V, F = trimesh_remesh(before.to_vertices_and_faces(), 3 * L)
after = Mesh.from_vertices_and_faces(V, F)

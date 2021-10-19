import os
from compas.datastructures import Mesh
import plotly.graph_objects as go

def plot_mesh(mesh):

    vertices, faces = mesh.to_vertices_and_faces()
    edges = [[mesh.vertex_coordinates(u), mesh.vertex_coordinates(v)] for u,v in mesh.edges()]
    line_marker = dict(color='rgb(0,0,0)', width=1.5)
    lines = []
    x, y, z = [], [],  []
    for u, v in edges:
        x.extend([u[0], v[0], [None]])
        y.extend([u[1], v[1], [None]])
        z.extend([u[2], v[2], [None]])

    lines = [go.Scatter3d(x=x, y=y, z=z, mode='lines', line=line_marker)]
    triangles = []
    for face in faces:
        triangles.append(face[:3])
        if len(face) == 4:
            triangles.append([face[2], face[3], face[0]])
    
    i = [v[0] for v in triangles]
    j = [v[1] for v in triangles]
    k = [v[2] for v in triangles]

    x = [v[0] for v in vertices]
    y = [v[1] for v in vertices]
    z = [v[2] for v in vertices]


    data = []
    faces = [go.Mesh3d(x=x,
                        y=y,
                        z=z,
                        i=i,
                        j=j,
                        k=k,
                        opacity=1.,
                        # contour={'show':True},
                        # vertexcolor=vcolor,
                        colorbar_title='Amplitude',
                        colorbar_thickness=10,
                        colorscale= 'agsunset', # 'viridis'
                        # intensity=intensity_,
                        intensitymode='cell',
                        showscale=True,
            )]
    x, y, z = [], [], []
    for fk in mesh.faces():
        cpt = mesh.face_centroid(fk)
        x.append(cpt[0])
        y.append(cpt[1])
        z.append(cpt[2])

    centroids = [go.Scatter3d(x=x, y=y, z=z, mode='markers')]

    data.extend(lines)
    data.extend(faces)
    data.extend(centroids)
    layout = layout = go.Layout(title='Mesh from Rhino Surfaces')
    fig  = go.Figure(data=data, layout=layout)
    fig.show()


if __name__ == '__main__':
    
    here = os.path.dirname(__file__)
    mesh = Mesh.from_json(os.path.join(here, 'mesh.json'))
    plot_mesh(mesh)


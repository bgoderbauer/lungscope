"""A self-contained scene for checking VTK rendering in the browser."""

from trame.widgets import html, vtk
from vtkmodules.vtkFiltersSources import vtkConeSource


def add_demo_view() -> None:
    """Add a browser-rendered scene without reading simulation data."""
    cone = vtkConeSource()
    cone.SetResolution(48)
    cone.Update()

    with html.Div(style="height: 60vh; min-height: 240px;"):
        with vtk.VtkView():
            with vtk.VtkGeometryRepresentation():
                vtk.VtkMesh("demo_mesh", dataset=cone.GetOutput())

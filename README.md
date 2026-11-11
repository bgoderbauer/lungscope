# lungscope

Interactive visualization of reduced lung simulations and uncertainty studies with 4C, QUEENS, and trame.

## Getting started

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then run
the following from the repository root.

```sh
uv sync --locked
uv run --locked lungscope
```

Open the local URL printed by trame. The starter scene uses a generated VTK
cone so it can run before any simulation files are available. Drag to rotate
the scene and scroll to zoom.

The project uses Python 3.12 for development. A standard Python environment
also works with `python -m pip install -e .` followed by `lungscope`.

## Project

The goal is an extensible local browser application for inspecting reduced
lung studies. The first study connects a spatial random material field to
terminal-unit expansion, with spatial ensemble statistics and linked
time-series plots.

See the [project guide](docs/project-guide.md) for the code layout, data
requirements, and first implementation milestone.

## Software

- [4C-Multiphysics](https://www.4c-multiphysics.org/)
- [QUEENS](https://queens-py.github.io/queens/)
- [trame](https://kitware.github.io/trame/)

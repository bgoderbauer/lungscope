# Project guide

LungScope is a visualization project for uncertainty studies with reduced
lung simulations. Its first application is exploring terminal-unit expansion
in a small forward uncertainty study with a spatial random material field.

## Where the code belongs

| Location    | Responsibility                                                                                    |
| ----------- | ------------------------------------------------------------------------------------------------- |
| `data/`     | Read the study outputs and expose geometry, identifiers, times, fields, and sampled coefficients. |
| `analysis/` | Compute statistics from study data. Keep these functions independent of trame and rendering.      |
| `views/`    | Render the spatial scene and plots using the current entity, time, and realization selections.    |
| `app.py`    | Build the trame layout and coordinate selections between views.                                   |

These paths are under `src/lungscope/`. Start with ordinary Python functions
and explicit imports. Add shared abstractions when a second analysis or view
needs the same interface.

## First implementation milestone

Run one case using the supplied 4C/QUEENS setup. Identify the VTK output
series, physical times, persistent terminal-unit IDs, volume and reference
volume fields, and the metadata that links sampled coefficients to the
simulation output. Load that case and show the expansion history for a selected
terminal unit. The ratio of volume to reference volume defines expansion in
this project.

Then run a small ensemble on the same geometry and time grid. Join fields
using entity IDs and link runs to coefficient sets using explicit identifiers.
Display mean and standard deviation at a selected time. Selecting a terminal
unit should update its time series and ensemble spread.

Use the supplied random-field procedure to reconstruct the material field for
a selected realization. A quantile band and a histogram for the selected
entity and time are examples of how new analyses and views could be added.

## Local data

Keep simulation inputs, VTK output series, and generated study data outside
version control. The repository-local `data/` and `output/` directories are
ignored and can be created as needed.

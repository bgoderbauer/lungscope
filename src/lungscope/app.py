"""Entry point for the local LungScope application."""

from trame.app import get_server
from trame.ui.vuetify3 import SinglePageLayout
from trame.widgets import html

from lungscope.views.demo import add_demo_view


def main() -> None:
    """Start the browser application with the starter VTK scene."""
    server = get_server(client_type="vue3")

    with SinglePageLayout(server) as layout:
        layout.title.set_text("LungScope")

        with layout.content:
            with html.Main(classes="pa-6"):
                html.H2("Starter scene", classes="text-h6")
                html.P(
                    "Rotate or zoom the generated VTK geometry to check your setup.",
                    classes="text-body-2 mb-4",
                )
                add_demo_view()

    server.start()

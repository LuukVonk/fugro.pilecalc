from parapy.webgui import leaflet
from parapy.webgui.core import Component, NodeType, State


class MapOverview(Component):
    marker_position = State((52.2, 5.5))

    def render(self) -> NodeType:
        return (
            leaflet.MapContainer(
                center=(52.2, 5.5),
                zoom=7,
                style={'height': '100%'},
                eventHandlers={'click': self.update_marker_position}
            )[
                leaflet.TileLayer(
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
                    attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
                ),
                leaflet.Marker(
                    position=self.marker_position,
                    draggable=True,
                    eventHandlers={'move': self.update_marker_position}
                )
            ]
        )

    def update_marker_position(self, evt):
        self.marker_position = (evt.latlng.lat, evt.latlng.lng)
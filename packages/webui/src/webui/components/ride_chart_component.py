import streamlit as st
import plotly.graph_objects as go
from collections import defaultdict
from statistics import mean
from webui.schemas.ride_schema import RideSchema
from webui.services.ride_service import RideService
from webui.enums.ride_type import RideType

class RideChartComponent:
    @classmethod
    def render(cls) -> None:
        st.set_page_config(page_title="Cuida Caucaia", layout="wide")
        st.title("📊 Cuida Caucaia")
        st.markdown("### Análise do preço de viagem em relação ao tempo")

        rides: list[RideSchema] = RideService.get_all_rides()
        rides_by_type = defaultdict(list)

        for ride in rides:
            if ride.ride_type and ride.price is not None and ride.timestamp is not None:
                rides_by_type[ride.ride_type].append(ride)

        cols = st.columns(len(RideType))
        for i, ride_type in enumerate(RideType):
            ride_list = rides_by_type.get(ride_type, [])
            total = len(ride_list)
            avg_price = mean([r.price for r in ride_list]) if ride_list else 0

            with cols[i]:
                st.metric(
                    label=f"{ride_type.value}",
                    value=f"{total} viagens",
                    delta=f"R$ {avg_price:.2f} média"
                )

        fig = go.Figure()
        for ride_type, ride_list in rides_by_type.items():
            ride_list.sort(key=lambda r: r.timestamp)
            fig.add_trace(go.Scatter(
                x=[r.timestamp for r in ride_list],
                y=[r.price for r in ride_list],
                mode='lines+markers',
                name=ride_type.value
            ))

        fig.update_layout(
            xaxis_title="Hora do dia",
            yaxis_title="Preço (R$)",
            xaxis={
                "rangeselector": {
                    "buttons": [
                        {"count": 1, "label": "1h", "step": "hour", "stepmode": "backward"},
                        {"count": 6, "label": "6h", "step": "hour", "stepmode": "backward"},
                        {"step": "all"}
                    ]
                },
                "rangeslider": {"visible": True},
                "type": "date"
            },
            template="plotly_white"
        )

        st.plotly_chart(fig, use_container_width=True)

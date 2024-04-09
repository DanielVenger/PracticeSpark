import folium

def mostrar_mapa(ubicacion_usuario, ubicacion_telefono):
    mapa = folium.Map(location=ubicacion_usuario, zoom_start=12)
    
    # Marcador para la ubicación del usuario
    folium.Marker(location=ubicacion_usuario, popup='Tu ubicación', icon=folium.Icon(color='blue')).add_to(mapa)
    
    # Marcador para la ubicación del teléfono
    folium.Marker(location=ubicacion_telefono, popup='Ubicación del teléfono', icon=folium.Icon(color='red')).add_to(mapa)

    return mapa

# Ejemplo de uso
ubicacion_usuario = (40.7128, -74.0060)  # Latitud y longitud de la ubicación del usuario (ejemplo: Nueva York)
ubicacion_telefono = (40.7306, -73.9352)  # Latitud y longitud de la ubicación del teléfono (ejemplo: Brooklyn)
mapa = mostrar_mapa(ubicacion_usuario, ubicacion_telefono)
mapa.save('mapa.html')

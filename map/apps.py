from django.apps import AppConfig


class MapConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'map'
 
    def ready(self):
        # from .mqtt import start_mqtt_client
        # start_mqtt_client(id)
        from . import mqtt
        mqtt.client.loop_start()
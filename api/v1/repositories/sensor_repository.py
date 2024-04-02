from api.v1.schemas import SensorRequestSchema
from api.v1.utils import firebase_firestore


db=firebase_firestore()


class SensorRepository:
    
    @staticmethod
    def create_sensor(sensor_id : str, sensor_request : SensorRequestSchema):
        doc=db.collection(sensor_id).document("sensors")
        doc.set({
            "is_start" : sensor_request.is_start,
            "is_stop" : sensor_request.is_stop,
            "is_initialized" : sensor_request.is_initialized,
            "counter" : sensor_request.counter,
            "timer" : sensor_request.timer
        })
        return True
    
    
    @staticmethod
    def is_sensor_exists(sensor_id : str):
        collection=db.collection(sensor_id).get()
        return len(collection) == 0
    
    
    @staticmethod
    def get_sensor(sensor_id : str):
        pass
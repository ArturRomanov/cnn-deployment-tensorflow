import os
import logging
import tensorflow as tf
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

load_dotenv()

current_path = os.getcwd()

class Model:
    def __init__(self) -> None:
        self.model = tf.keras.models.load_model(
            current_path + os.getenv("MODEL_PATH")
            )
    
    def predict(self, tensor):
        predictions = self.model(tensor, training=False)
        logger.info(f"Predictions: {predictions}")
        return predictions
    
    def preprocess_image(
            self,
            image_bytes: bytes, 
            target_size: tuple[int, int] = (128, 128),
            scale_to: tuple[int, int] = (0, 1)
            ) -> tf.Tensor:
        
        logger.info("Preprocessing of image has started")

        image = tf.io.decode_image(
            image_bytes,
            channels=3,
            expand_animations=False,
            dtype=tf.uint8
        )

        image = tf.cast(image, tf.float32)

        image = tf.image.resize(
            image,
            size=target_size,
            method=tf.image.ResizeMethod.BICUBIC,
            preserve_aspect_ratio=False,
            antialias=True
        )

        min_val, max_val = scale_to

        if (min_val, max_val) == (0, 1):
            image = image / 255.0

        image = tf.expand_dims(image, axis=0)

        logger.info("Preprocessed image")

        return image
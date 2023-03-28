from .datasetA import DATASET as DATASET_A

DATASET = DATASET_A.clone()

DATASET.TYPE = "POINTCLOUD"
DATASET.CLASSES = ["chair", "bookshelf", "bathtub"]
DATASET.NUM_CLASSES = len(DATASET.CLASSES)
DATASET.DIRECTORY_PATH = "/home/whacky/datasets/point_clouds/ShapeNetV2"

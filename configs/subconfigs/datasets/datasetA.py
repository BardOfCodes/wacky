from wacky import CfgNode as CN

DATASET = CN()
DATASET.TYPE = "VOXEL"
DATASET.CLASSES = ["chair", "table", "sofa", "bed", "toilet",]
DATASET.NUM_CLASSES = len(DATASET.CLASSES)
DATASET.DIRECTORY_PATH = "/home/whacky/datasets/voxels/ShapeNetV2"

from wacky import CfgNode as CN, CfgNodeFactory as CNF

from configs.subconfigs.datasets.datasetA import DATASET as DATASET_A
from configs.subconfigs.datasets.datasetB import DATASET as DATASET_B
from configs.subconfigs.models.modelA import MODEL as MODEL_A
from configs.subconfigs.models.modelB import MODEL as MODEL_B


class BaseConfFactory(CNF):

    def __init__(self, dataset_type="A", model_type= "B"):

        super(BaseConfFactory, self).__init__()

        self.config = CN()

        if dataset_type == "A":
            self.config.DATASET = DATASET_A.clone()
        else:
            self.config.DATASET = DATASET_B.clone()
        if model_type == "A":
            self.config.MODEL = MODEL_A.clone()
        else:
            self.config.MODEL = MODEL_B.clone()

        self.config.TRAIN = CN()
        self.config.TRAIN.EPOCHS = 100
        self.config.TRAIN.LR = 0.001
        self.config.TRAIN.LOGGING_ITER = 50

        self.config.NOTIFICATION = CN()
        self.config.NOTIFICATION.ENABLE = False
        self.config.NOTIFICATION.CHANNEL = "aditya"
        
from wacky import CfgNode as CN
from configs.ablations.base_configuration import BaseConfFactory

class PhaseAFactory(BaseConfFactory):

    def __init__(self, 
                 training_mode = 0, 
                 dataset_type = "A",
                 model_type = "A",
                 ):
        super(PhaseAFactory, self).__init__(dataset_type, model_type)

        if training_mode == 0:
            self.config.TRAIN.EPOCHS = 1000
            self.config.TRAIN.LR_INITIAL = 0.0003
            self.config.TRAIN.OPTIM = CN()
            self.config.TRAIN.OPTIM.TYPE = "DEFAULT" # "ADAM_SPECIFIC"
            self.config.TRAIN.OPTIM.EPSILON = 1e-9
            self.config.TRAIN.RESUME_CHECKPOINT = True
        elif training_mode == 1:
            self.config.TRAIN.EPOCHS = 1000
            self.config.TRAIN.LR_INITIAL = 0.0005
            self.config.TRAIN.OPTIM = CN()
            self.config.TRAIN.OPTIM.TYPE = "ADAM_SPECIFIC"
            self.config.TRAIN.OPTIM.BETA_1 = 0.9
            self.config.TRAIN.OPTIM.BETA_2 = 0.98
            self.config.TRAIN.OPTIM.EPSILON = 1e-9
            self.config.TRAIN.RESUME_CHECKPOINT = True
            
from wacky import CfgNode as CN

MODEL = CN()
MODEL.TYPE = "Transformer"
MODEL.CNN_FIRST_STRIDE = 1
MODEL.POS_ENCODING_TYPE = "LEARNABLE" # "FIXED"
MODEL.OUTPUT_DIM = 512
MODEL.DROPOUT = 0.1
MODEL.INPUT_SEQ_LENGTH = 64
MODEL.OUTPUT_SEQ_LENGTH = 128
MODEL.NUM_ENC_LAYERS = 8
MODEL.NUM_DEC_LAYERS = 8
MODEL.NUM_HEADS = 16
MODEL.OUTPUT_TOKEN_COUNT = 75
MODEL.HIDDEN_DIM = 256

from .modelA import MODEL as MODEL_A

MODEL = MODEL_A.clone()
MODEL.TYPE = "RNN"
MODEL.CNN_FIRST_STRIDE = 2
MODEL.OUTPUT_DIM = 1024
MODEL.NUM_ENC_LAYERS = 8
MODEL.NUM_DEC_LAYERS = 8
MODEL.HIDDEN_DIM = 512

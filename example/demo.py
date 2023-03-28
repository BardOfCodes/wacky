
import argparse
from wacky import load_config_file
from procXD import SketchBuilder


if __name__ == '__main__':

    # Load the config
    test_arguments = [
        "--config-file", "configs/ablations/configurationA.py",
    ]
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--config-file', type=str, required=True)
    args, reminder_args = parser.parse_known_args(test_arguments)
    config = load_config_file(args.config_file, reminder_args)

    # check that original configuration
    assert config.DATASET.TYPE == "VOXEL"
    assert config.TRAIN.OPTIM.EPSILON == 1e-9
    
    test_arguments = [
        "--config-file", "configs/ablations/configurationA.py",
        "--dataset_type", "B",
        "--cfg.TRAIN.OPTIM.EPSILON", "0.1",
    ]
    args, reminder_args = parser.parse_known_args(test_arguments)
    config = load_config_file(args.config_file, reminder_args)

    # check that the config is updated properly.
    assert config.DATASET.TYPE == "POINTCLOUD"
    assert config.TRAIN.OPTIM.EPSILON == 0.1

    # Print the config
    print(config)

    # Visualize the config
    G = config.to_graph()
    SAVE_FILE = "example/xd_figures/configuration.excalidraw"
    sketch_builder = SketchBuilder(save_path=SAVE_FILE)
    sketch_builder.render_stack_sketch(G, stacking="vertical")
    sketch_builder.export_to_file()
    del sketch_builder

    # Now compare a variant configurations:
    test_arguments = [
        "--config-file", "configs/ablations/configurationA.py",
        "--dataset_type", "A",
        "--training_mode", "1",
        "--cfg.NOTIFICATION.CHANNEL", "DEMO",
    ]
    args, reminder_args = parser.parse_known_args(test_arguments)
    config_2 = load_config_file(args.config_file, reminder_args)

    config_dict = {
        "config": config.to_graph(),
        "variant_1": config_2.to_graph(),
    }
    SAVE_FILE = "example/xd_figures/config_comparison.excalidraw"
    sketch_builder = SketchBuilder(save_path=SAVE_FILE)
    sketch_builder.render_comparitive_stack_sketch(
        config_dict, base_config_name="config", stacking="vertical")
    sketch_builder.export_to_file()
    del sketch_builder

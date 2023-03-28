"""Just some helper functions for the wacky package."""
import importlib
import inspect
from typing import List
from yacs.config import CfgNode as YacsCfgNode
from .config_nodes import CfgNodeFactory


def load_config_file(config_file: str,
                     reminder_args: List[str]) -> YacsCfgNode:
    """
    Loads a configuration factory from the given file path, 
    instantiates it with arguments from reminder_args, 
    and finally updates the configuration with any matching arguments from reminder_args.

    Args:
        config_file (str)
        reminder_args (argparse.Namespace)
    Returns:
        (CfgNode)
    """

    # get the CfgNodeFactory from the config file
    spec = importlib.util.spec_from_file_location('FactoryFile', config_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    classes = inspect.getmembers(module, inspect.isclass)
    classes = [m for m in classes if m[1].__module__ == module.__name__]
    for cur_class in classes:
        if issubclass(cur_class[1], CfgNodeFactory):
            factory_class = cur_class[1]
            break
    parser = factory_class.get_argparser()
    factory_args, remaining = parser.parse_known_args(reminder_args)
    factory = factory_class(**vars(factory_args))
    config = factory.get_config()

    # Update the config with any remaining args
    config.update_config_from_arguments(remaining)

    return config

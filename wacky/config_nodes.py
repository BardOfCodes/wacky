"""Wacky is a library for managing configuration files and experiments."""
import argparse
import inspect
from typing import List
import networkx as nx
from yacs.config import CfgNode as CN


def cfg_to_graph(cfg: CN) -> nx.DiGraph:
    """A helper function to convert a yacs config to a networkx graph.

    Args:
        cfg (yacs.config.CfgNode)

    Returns:
        (networkx.Digraph)
    """
    nx_graph = nx.DiGraph()
    nodes_to_process = {"cfg": cfg}
    while nodes_to_process:
        current_name, current_node = nodes_to_process.popitem()
        content = [f'{current_name}.{k} = "{v}"' if isinstance(v, str) else
                   f'{current_name}.{k} = {v}' for k, v in current_node.items()
                   if not isinstance(v, CN)]
        nx_graph.add_node(current_name, label=current_name, content=content)
        for key, value in current_node.items():
            if isinstance(value, CN):
                child_name = f'{current_name}.{key}'
                nx_graph.add_edge(current_name, child_name)
                nodes_to_process[child_name] = value
    return nx_graph


class CfgNode(CN):
    """A wrapper around yacs.config.CfgNode to add some extra functionality."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def update_config_from_arguments(self, args: List[str]):
        """Update the given config with any matching arguments from remaining.

        Args:
            args (List[str]): 
            Note - it is assumed that the config is specified with a prefixed --cfg
        """
        parser = argparse.ArgumentParser()
        self.update_argparse(parser, prefix="cfg")
        configuration_args, _ = parser.parse_known_args(args)
        configuration_dict = vars(configuration_args)
        configuration_dict = {".".join(k.split('.')[1:]): v
                              for k, v in configuration_dict.items() if v is not None}
        config_list = []
        for key, value in configuration_dict.items():
            config_list.append(key)
            config_list.append(value)
        self.merge_from_list(config_list)

    def update_argparse(self, parser: argparse.ArgumentParser, prefix: str = ''):
        """ Recursively update an argparse parser with 
            the given config and its children configs.

        Args:
            parser (argparse.ArgumentParser):
            prefix (str, optional)
        """
        for key in self:
            value = self[key]
            full_key = f'{prefix}.{key}' if prefix else key

            if isinstance(value, CfgNode):
                value.update_argparse(parser, full_key)
            elif isinstance(value, (int, bool, str, float)):
                parser.add_argument(f'--{full_key}', type=type(value))
            elif isinstance(value, (list)):
                pass
                # print("Skipping", full_key, "because it is a list or dict")

    def to_graph(self):
        """Convert the config to a networkx graph.
        Returns:
            (networkx.DiGraph)
        """
        return cfg_to_graph(self)


class CfgNodeFactory:
    """A factory class for creating CfgNodes from a given configuration file."""
    def __init__(self, *args, **kwargs):
        self.config = None

    def get_config(self):
        """ Get the configuration for the given factory class."""
        return self.config

    @classmethod
    def get_argparser(cls):
        """Create an argparse parser for the given factory class.
        Returns:
            (argparse.ArgumentParser)
        """
        # parse the factory args and instantiate configuration
        params = inspect.signature(cls.__init__).parameters
        parser = argparse.ArgumentParser()
        for name, param in params.items():
            if name == "self":
                continue
            if param.default is not inspect.Parameter.empty:
                if isinstance(param.default, bool):
                    parser.add_argument(
                        f"--{name}", action="store_true", default=param.default)
                else:
                    parser.add_argument(
                        f"--{name}", type=type(param.default), default=param.default)
            else:
                parser.add_argument(name, type=type(param.default))
        return parser

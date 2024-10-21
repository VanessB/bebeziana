import pandas
import yaml

from collections import defaultdict
from collections.abc import MutableMapping
from pathlib import Path


def flatten_dict(dictionary: dict, parent_key='', separator='.') -> dict:
    """
    Flattens dictionary via composing existing keys.

    Parameters
    ----------
    dictionary : dict
        Dictionary to be flattened.
    parent_key : str, optional
        Parent key to be added to the beggining of other keys.
        Default value is empty string.
    separator : str, optional
        Separator used to join the keys.
        Default value is '.'

    Returns
    -------
    result : dict
        Flattened dictionary.
    """

    items = []
    for key, value in dictionary.items():
        new_key = parent_key + separator + key if parent_key else key
        if isinstance(value, MutableMapping):
            items.extend(flatten_dict(value, new_key, separator=separator).items())
        else:
            items.append((new_key, value))

    return dict(items)


def read(path: Path, file_names: list[str]) -> pandas.DataFrame:
    """
    Read files and dump them into a single dataframe.

    Parameters
    ----------
    path : pathlib.Path
        A path to walk and discover files.
    file_names : list[str]
        A list of filenames to consider while walking.

    Returns
    -------
    data : pandas.DataFrame
        Final dataframe containing all discovered data.
    """

    full_data = []

    for node in path.glob("**/*"): # TODO: in Python 3.12 replace with .walk()
        if not node.is_dir():
            continue

        data = {}
        for subnode in node.iterdir():
            if not subnode.is_file():
                continue

            if subnode.name in file_names:
                with open(subnode) as file:
                    data |= yaml.load(file, yaml.Loader)

        if data:
            full_data.append(flatten_dict(data))

    return pandas.DataFrame(full_data)

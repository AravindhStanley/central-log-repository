import secrets
import string
from pathlib import Path

import yaml


def generate_password(length: int = 36) -> str:
    """
    Generates a random password.

    The password is a random combination of letters and digits with a default length of 36.

    Parameters
    ----------
    length : int
        The length of the password. Defaults to 36.

    Returns
    -------
    str
        The generated password.
    """
    letters = string.ascii_letters
    digits = string.digits
    possible_chars = letters + digits

    pre_password = [secrets.choice(possible_chars) for _ in range(length)]

    password = "".join(pre_password)

    return password


def update_config_file(
    user: str, password: str, file_path: Path = "/opt/log-repo/passwords.yml"
) -> None:

    ## Create the password file if it does not exist
    """
    Updates a password value for a user key in passwords.yml file.

    Parameters
    ----------
    user : str
        The key to write to the YAML file.
    password : str
        The value to write to the YAML file.
    file_path : Path, optional
        The path to the YAML file to update. Defaults to "/opt/log-repo/passwords.yml".

    Returns
    -------
    None
    """
    Path(file_path).touch(exist_ok=True)

    with open(file_path, "r") as config_file:
        config = yaml.load(config_file, Loader=yaml.FullLoader)

    if config is None:
        config = {}

    config[user] = password

    with open(file_path, "w") as config_file:
        yaml.dump(config, config_file)


if __name__ == "__main__":
    users: dict[str, str] = {
        "elasticsearch8_keystore_password": "",
        "kibana8_system_password": "",
        "kibana8_security_encrpytionKey": "",
        "kibana8_encryptedSavedObjects_encryptionKey": "",
    }

    for user in users:
        users[user] = generate_password()
        update_config_file(user=user, password=users[user])

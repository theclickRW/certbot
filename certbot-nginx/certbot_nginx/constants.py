"""nginx plugin constants."""
import pkg_resources


CLI_DEFAULTS = dict(
    server_root="/etc/nginx",
    ctl="nginx",
)
"""CLI defaults."""


MOD_SSL_CONF_DEST = "options-ssl-nginx.conf"
"""Name of the mod_ssl config file as saved in `IConfig.config_dir`."""

MOD_SSL_CONF_SRC = pkg_resources.resource_filename(
    "certbot_nginx", "options-ssl-nginx.conf")
"""Path to the nginx mod_ssl config file found in the Certbot
distribution."""

UPDATED_MOD_SSL_CONF_DIGEST = ".updated-options-ssl-nginx-conf-digest.txt"
"""Name of the hash of the updated or informed mod_ssl_conf as saved in `IConfig.config_dir`."""


ALL_SSL_OPTIONS_HASHES = [
    '0f81093a1465e3d4eaa8b0c14e77b2a2e93568b0fc1351c2b87893a95f0de87c',
    '9a7b32c49001fed4cff8ad24353329472a50e86ade1ef9b2b9e43566a619612e',
    'a6d9f1c7d6b36749b52ba061fff1421f9a0a3d2cfdafbd63c05d06f65b990937',
    '7f95624dd95cf5afc708b9f967ee83a24b8025dc7c8d9df2b556bbc64256b3ff',
    '394732f2bbe3e5e637c3fb5c6e980a1f1b90b01e2e8d6b7cff41dde16e2a756d',
    '4b16fec2bcbcd8a2f3296d886f17f9953ffdcc0af54582452ca1e52f5f776f16',
]
"""SHA256 hashes of the contents of all versions of MOD_SSL_CONF_SRC"""

SSL_DHPARAMS_DEST = "certbot-ssl-dhparams.pem"
"""Name of the ssl_dhparams file as saved in `IConfig.config_dir`."""

SSL_DHPARAMS_SRC = pkg_resources.resource_filename(
    "certbot_nginx", "certbot-ssl-dhparams.pem")
"""Path to the nginx ssl_dhparams file found in the Certbot distribution."""

UPDATED_SSL_DHPARAMS_DIGEST = ".updated-ssl-dhparams-pem-digest.txt"
"""Name of the hash of the updated or informed ssl_dhparams as saved in `IConfig.config_dir`."""

ALL_SSL_DHPARAMS_HASHES = [
    '9ba6429597aeed2d8617a7705b56e96d044f64b07971659382e426675105654b',
]
"""SHA256 hashes of the contents of all versions of SSL_DHPARAMS_SRC"""

def os_constant(key):
    # XXX TODO: In the future, this could return different constants
    #           based on what OS we are running under.  To see an
    #           approach to how to handle different OSes, see the
    #           apache version of this file.  Currently, we do not
    #           actually have any OS-specific constants on Nginx.
    """
    Get a constant value for operating system

    :param key: name of cli constant
    :return: value of constant for active os
    """
    return CLI_DEFAULTS[key]

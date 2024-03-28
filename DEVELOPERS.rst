.. _DEVELOPERS:

.. note::
    ParaPy >= 1.11 requires Python >= 3.9. Make sure it is installed on your system.

.. note::
    This documentation assumes Windows with a ``PowerShell`` or ``Cmd`` terminal. Adjust the commands
    to match your system and preferred terminal.

Management
----------
The ``parapy-run`` Python package is available to assist during development and easy (cloud) deployment of the
application. It is from now on simply referred to as the "management tool". It exposes a command line interface,
``parapy run``.

Prerequisites Windows
=====================
For a subset of commands a Linux distribution installed with WSL 2 (version >= 0.67.6) is required for Windows users.
The Ubuntu 20.04 and 22.04 LTS releases have both been tested and are actively supported. The official installation
documentation can be found `here <https://docs.microsoft.com/en-us/windows/wsl/install>`_.

If WSL isn't installed at all, you only need to run one command. ::

    wsl --install --distribution ubuntu

If you already have WSL, but Ubuntu has not been installed yet, you can easily install it. Make sure to switch to WSL
2 before installing Ubuntu. Also consider setting Ubuntu as your default distribution. ::

    wsl --set-default-version 2
    wsl --install --distribution ubuntu
    wsl --setdefault ubuntu

If you already have WSL with Ubuntu installed, but it still runs on WSL 1, you can easily upgrade it. Also consider
setting Ubuntu as your default distribution. ::

    wsl --set-version ubuntu 2
    wsl --setdefault ubuntu

When listing the available distributions and associated WSL versions, you should see something like this. ::

    wsl --list --verbose
      NAME            STATE           VERSION
    * Ubuntu          Running         2

Lastly, enable `systemd <https://learn.microsoft.com/en-us/windows/wsl/wsl-config#systemd-support>`_ in the Linux distro
as well. This can be configured in a ``/etc/wsl.conf`` file in the distro. As a privileged user, create or edit the
``/etc/wsl.conf`` file in your Linux distro. Add the following contents; adjust as necessary. ::

    [boot]
    systemd=true

After enabling systemd, restart WSL, so that the change can take effect. ::

    wsl --shutdown
    wsl

If you're running an older version of WSL (<0.67.6) and cannot upgrade for some reason, consider installing and
using an alternative for systemd like `distrod <https://github.com/nullpo-head/wsl-distrod>`_.

Installation
============
The management tools are part of the "dev(eloper) requirements". ::

    pip install -r requirements-dev.txt --index-url https://pypi.parapy.nl/simple/

Alternatively, install the package directly. ::

    pip install parapy-run --index-url https://pypi.parapy.nl/simple/

This will install the ``parapy-run`` Python package and expose the ``parapy run`` command group. Invoke
the ``--help`` to see it in action. ::

    parapy run --help

.. note::
    Environment variables play a big role in the commands that come with the management tool. The
    ``--help`` of each command will show you what ``env var`` is associated with the various parameters.
    The "Configuration" section will expand on this.

Configuration
=============
All the commands have the global options ``--env`` (load an "env file") and ``--app-dir`` (configure the application
directory). The ``--env`` option can be passed multiple times to load multiple "env files". Note that the order matters;
the leading ``--env`` takes precedence over the trailing ``--env``. Certain commands require knowledge of where the
application directory is located and (nearly) all the commands have parameters that accept environment variables as input.
The commands always try to load an "env file" prior to executing a command. This file, by default, is assumed to be named
``.env`` and is considered relative to the application directory. The default application directory is the current working
directory.

Providing an alternative ``--app-dir`` to a command allows the user to run the commands from anywhere. Just provide the
relative or absolute path to the application directory and everything should work the same. The ``.env`` file will be
discovered in the same way. The ``--env`` and ``--app-dir`` options of the commands will automatically try to load the
``PARAPY_ENV`` and ``PARAPY_APP_DIR`` respectively to use as their values when the parameter is not explicitly passed
via the command line. Updating what environment is used can be done by providing a relative or absolute pathlike value.
The following arguments are all valid values for ``--env``.

These arguments reason with respect to ``--app-dir``,

- ``--env .example.env``
- ``--env example``
- ``--env ../some/relative/path/.example.env``
- ``--env ../some/relative/path/example``

and these (absolute path-like) arguments do not.

- ``--env /some/absolute/path/.example.env``
- ``--env /some/absolute/path/example``

We can also set the ``PARAPY_ENV`` to achieve the same thing. The same values would be valid. Multiple env files
can be provided, separated by semicolons (``;``). E.g. ``PARAPY_ENV=.first.env;.second.env``.

Many command groups provide the option to ``--generate-env``. Invoking the command group with that flag will instruct it
to recursively obtain all the used environment variables of the sub-commands and generate env files from those. The
public and private variables are written to separate files, with the ``.env`` and ``.credentials.env`` prefix
respectively. ::

    parapy run [...] --generate-env

An overview of the environment variables relevant to the management tool, along with an explanation of
what they represent and how the associated values can be retrieved, can be found in the section
`Parameters: environment variables <https://parapy.nl/docs/cloud/latest/miscellaneous/management_with_cli.html#
parameters-environment-variables>`_ of the `Managing ParaPy Cloud from the command line <https://parapy.nl/docs/cloud/
latest/miscellaneous/management_with_cli.html>`_ chapter of the ParaPy Cloud documentation.

Testing
-------
First make sure the test requirements have been installed ::

    pip install -r requirements-test.txt

To run the tests, open a terminal in the project directory and type ::

    pytest

Or to run individual tests ::

    pytest tests\unit\test_dummy.py::test_foo

Deployment
----------
Once the management tool and application environment have been properly configured, deploying an
application to the ParaPy Cloud is easily done. Detailed information on the ParaPy Cloud can be found
`here <https://parapy.nl/docs/cloud/latest/>`_.

A Docker image of the application is required in order to deploy it to the ParaPy Cloud. Install the required system
dependencies for the ``docker`` commands (if required), build a Docker image of your application and push it to the
remote Docker registry. ::

    parapy run docker install-dependencies
    parapy run docker build
    parapy run docker push

.. note::
    The ``install-dependencies`` command only needs to be executed once.

To actually deploy the application you need to install the required system dependencies for the ``cloud azure``
or ``cloud aws`` (depending on your cloud provider) commands (if required) first. ::

    parapy run cloud azure install-dependencies
    parapy run cloud aws install-dependencies

To deploy your application to the ParaPy Cloud, use the relevant ``deploy`` command. ::

    parapy run cloud azure app deploy
    parapy run cloud aws app deploy

.. note::
    The ``install-dependencies`` command only needs to be executed once.

# Example on how to build a plugin-based Python package

This repo contains two packages and an environment that makes
use of them. The `spiffy-core` package is the base of the `spiffy`
package. (It's what they call a "namespace package".)

The `spiffy-plugin` package is, as the name suggests, a plugin for
`spiffy-core`.

The user can set up an environment and list `spiffy-plugin` as a dependency
and with it install the required core-functionality as well, without needing
to worry about it.



## Setup

From the root of this repo, execute the setup_all script:
```bash
. ./setup_all.sh
```

This will create all the virtual environments and build the wheels. You can then test the `spiffy` package as a user from the `spiffy-user` folder.

## Namespace package

As mentioned before, in this example we make use of so-called namespace packages to
achieve the plugin functionality.

From [py-pkgs.org](https://py-pkgs.org/04-package-structure.html#package-structure):
> Namespace packages are a way of splitting a single Python package across multiple directories.
> Unlike regular packages, where all contents live in the same directory hierarchy, namespace packages
> can be formed from directories in different locations on a file system and do not contain an `__init__.py` file.

In practice, this means that whenever we have a package we want to be
extensible with a plugin from a different repo, we need to drop the `__init__.py` file from that package.

In this example we want the core-packeg itself (`spiffy`) to be extensible and its `astrophys` package.
Leaving out the init files allows us to extend `spiffy` with the `vehicles` package and the `astrophys/blackhole.py` module.


Now, as a user, we do not need to import the `blackhole` module from `spiffy_plugin`.
For example, we can directly use `from spiffy.astrophys import blackhole`.
So when we install `spiffy-plugin`, we will be able to import and use the `spiffy` package as though it is a single
consistent package containing all the core utilities and plugins.

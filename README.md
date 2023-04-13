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

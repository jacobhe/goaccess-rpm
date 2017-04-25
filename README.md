goaccess-rpm
============

**GoAccess** [\(http://goaccess.io/)](http://goaccess.io/) is a great real-time web log analyzer with an interface that makes it easy to visualize web traffic from within your terminal.

## Building

*Note: This spec file is complete and works, but the build script and documentation in this repository is still being worked on.*

1. `git clone https://github.com/clcollins/goaccess-rpm.git`
2. `yum groupinstall -y "Development Tools" && yum install rpm-build rpmdevtools automake glib2-devel ncurses-devel geoip-devel tokyocabinet-devel`
3. `./build.sh goaccess`
4. `yum install ~/rpmbuild/RPMS/*/*.rpm`
5. PROFIT!

## Releases

Release versions will match versions of the upstream GoAccess project, though best effort only for release dates - releases will be created periodically based on whatever current version exists for upstream.  Some versions might be missed.

## Acknowledgements

Thanks to:

* Geraldo O. [\(https://github.com/allinurl\)](https://github.com/allinurl) for developing GoAccess.

* Ian Meyer [\(https://github.com/imeyer\)](https://github.com/imeyer) for giving me the idea to do this and the code to base some of this off of (check out his awesome Runit rpm spec file and build script for RHEL-based systems).

## Copyright Information

The GoAccess source code is released under the GNU General Public License, version 2.

This repo, and the .spec file and build script are:

Copyright (C) 2014 Chris Collins

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.


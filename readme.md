# Pava: P(ython) (J)ava

Makes any executable jar instantly callable from python.

Takes care of:

* Downloading jar and jre
* Placing this bundle in a folder in the user home
* Routing calls through python to the bundle. 
    * Calls can be made from within python (API) or from the system commandline / terminal

## Run Pava

todo: Get the pava module

Execute the sample "echo" bundle from the commandline. On Linux with java 11:

    pava echo_lin_11 "Hello from pava"

## Requirements to create your own bundles

The application jar and the jre must be downloadable through a http(s) GET request.

The bundle is placed in [USER HOME]/pava/[BUNDLE NAME]

[USER HOME]/pava/pava.yml contains the config information for all bundles.

# Software design

Steps

* Load bundle if not present
    * Load jar
    * Load jre
    * Verify by calling the jar with a "no dependencies" option like --version or --help or --info
* Route the call to java in bundle

Libs

Logging, System output, System error

Exceptions



# Resources

* https://www.py4e.com/
* https://automatetheboringstuff.com/
* https://www.thedigitalcatbooks.com/pycabook-chapter-01/
* https://python-3-patterns-idioms-test.readthedocs.io/en/latest/index.html





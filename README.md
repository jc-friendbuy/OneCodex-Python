# onecodex-api-python
Bindings for the OneCodex REST API in Python.

## Important notes:
 - This is a work in progress.  The current version is not suitable for any kind of production 
   application. It will be clearly stated when/if this situation changes.
 
 - The currently targeted One Codex API version is 0, which is the last published version.

## Required packages:
 - This project requires: `nose>=1.3.6`, `requests>=2.7.0`, `purl>=1.1` and `pytz==2015.4`.  
   A setup.py file will be added later which will automate installation.  Presently, though, they 
   need to be installed manually.

## Usage
`python main.py` will run all tests for all API versions (currently only v0).  This *should* not 
require any sort of modification of the path by you.  However, this is still a very early library
 and may have issues.
 
## Contact
If you run into any issues, please contact me at: jc[at]jccoto[dot]com.

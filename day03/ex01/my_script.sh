PYTHON_PATH = "/usr/local/bin/python3"
LOCAL_LIB = "local_lib"

$PYTHON_PATH -m venv $LOCAL_LIB
source $LOCAL_LIB/bin/activate
python3 -m pip --version
python3 -m pip install --upgrade pip
python3 -m pip install --log local_lib --force-reinstall git+"https://github.com/jaraco/path"
python3 my_program.py

#!/bin/bash
WORK_DIR=$(cd `dirname $0`; pwd)
cd $WORK_DIR

# check if have crudini
if ! command -v crudini &> /dev/null
then
    echo "crudini could not be found"
    echo "please install crudini first"
    exit
fi

package_base_name=$(crudini --get setup.cfg metadata name)
pip uninstall $package_base_name -y

rm -rf build
rm -rf dist
python3 setup.py sdist

pip install dist/$package_base_name-*.tar.gz

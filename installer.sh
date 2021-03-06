#!bin/sh

echo "Installing . . ."

pip3 install colorama gTTS

if [[ $? == 0 ]]; then
	echo "Installing successfuly!"
	echo "Please run main.py"
else
	echo "Installing not successfuly! please fix that and then run again"
fi

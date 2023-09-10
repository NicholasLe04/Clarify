if [ -z $1 ]
then
    echo "usage: run clarify [the path to the python file to be clarified]"
    exit 1
fi

if [ $1 == "completion" ]
then
    echo "# for Clarify"
    echo "alias clarify=\"$(pwd)/clarify.sh\""
    echo ""
    exit 0
fi

file_directory="$(pwd)/$1"

# Check that the file is a python file
if [[ $1 != *.py ]]
then
    echo "Not a python file"
    exit 1
fi

# Check if file exists
if [ ! -e $file_directory ]
then
    echo "That jawn don't exist"
    exit 1
fi

starting_dir="$(dirname $0)"
python3 $starting_dir/clarifier/cli.py -f $file_directory

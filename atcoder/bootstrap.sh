folder_path=$1

mkdir -p $folder_path
SHELL_PATH=$(pwd -P)
cd $folder_path
echo $SHELL_PATH
ln -s $SHELL_PATH/ac-library/atcoder atcoder
ln -s $SHELL_PATH/run_cpp.sh run_cpp.sh
cp $SHELL_PATH/*.cpp .
cp $SHELL_PATH/*.py .
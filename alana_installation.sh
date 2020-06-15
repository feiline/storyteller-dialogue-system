echo "Creating virtual environment..."
echo
conda create -n Alana python=3.6 -y
eval "$(conda shell.bash hook)"
conda activate Alana

# echo "Installing requirements for sample bot..."
# echo
#cd sample_bot && pip install -r requirements.txt

echo "Installing supporting packages..."
echo
cd utils && pip install -e .
@echo off
echo Installing ipykernel...
pip install ipykernel

echo.
echo Registering the current environment to Jupyter...
python -m ipykernel install --user --name=python_dp2031 --display-name "Python (DP2031)"

echo.
echo === Done! ===
echo You can now open Jupyter Notebook and select the "Python (DP2031)" kernel.
pause
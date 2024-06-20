import subprocess
import os

def install_pandas_in_conda_env(env_name):
    try:
        # Activate the environment and install pandas using pip
        subprocess.check_call(['conda', 'activate', env_name, 'pip', 'install', 'libstdcxx-ng'])
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while installing pandas in {env_name}: {e}")

# List all conda environments
envs = subprocess.check_output(['conda', 'env', 'list']).decode().split('\n')

for env in envs:
    if 'mlflow' in env:
        env_name = env.split()[0]
        install_pandas_in_conda_env(env_name)

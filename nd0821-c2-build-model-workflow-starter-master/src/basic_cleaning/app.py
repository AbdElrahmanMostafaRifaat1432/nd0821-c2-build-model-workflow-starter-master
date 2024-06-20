import subprocess
import os

def install_pandas_in_conda_env(env_name):
    try:
        subprocess.check_call(['conda', 'install', '-n', env_name, 'pandas', '-y'])
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while installing pandas in {env_name}: {e}")

# List all conda environments
envs = subprocess.check_output(['conda', 'env', 'list']).decode().split('\n')

for env in envs:
    if 'mlflow' in env:
        env_name = env.split()[0]
        install_pandas_in_conda_env(env_name)

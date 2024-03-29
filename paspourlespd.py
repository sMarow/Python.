version: 2

jobs:
  build_35:
    machine: true
    environment:
      PYTHON: "3.5"
      ENV_NAME: "py35-xonsh-test"
    steps:
      - checkout
      - restore_cache:
          keys:
            - miniconda-v1-{{ checksum "ci/environment-3.5.yml" }}
      - run:
          name: install miniconda
          command: |
              if [ ! -d "/home/circleci/miniconda" ]; then
                wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
                bash miniconda.sh -b -p $HOME/miniconda
                export PATH="$HOME/miniconda/bin:$PATH"
                conda config --set always_yes yes --set changeps1 no --set channel_priority strict
              fi
              sudo chown -R $USER.$USER $HOME
      - run:
          name: configure conda
          command: |
              export PATH="$HOME/miniconda/bin:$PATH"
              export ENV_NAME="py35-xonsh-test"
              if [ ! -d "/home/circleci/miniconda/envs/py35-xonsh-test" ]; then
                conda update -q conda
                conda env create -f ci/environment-${PYTHON}.yml --name=${ENV_NAME}
                source activate ${ENV_NAME}
              fi
              conda env list
              conda list ${ENV_NAME}
      - save_cache:
          key: miniconda-v1-{{ checksum "ci/environment-3.5.yml" }}
          paths:
            - "/home/circleci/miniconda"
      - run:
          command: |
            export PATH="$HOME/miniconda/bin:$PATH"
            source activate ${ENV_NAME}
            pip install . --no-deps
      - run:
          command: |
            export PATH="$HOME/miniconda/bin:$PATH"
            source activate ${ENV_NAME}
            xonsh run-tests.xsh --timeout=10
  build_36:
    machine: true
    environment:
      PYTHON: "3.6"
      ENV_NAME: "py36-xonsh-test"
    steps:
      - checkout
      - restore_cache:
          keys:
            - miniconda-v1-{{ checksum "ci/environment-3.6.yml" }}
      - run:
          name: install miniconda
          command: |
              if [ ! -d "/home/circleci/miniconda" ]; then
                wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
                bash miniconda.sh -b -p $HOME/miniconda
                export PATH="$HOME/miniconda/bin:$PATH"
                conda config --set always_yes yes --set changeps1 no --set channel_priority strict
              fi
              sudo chown -R $USER.$USER $HOME
      - run:
          name: configure conda
          command: |
              export PATH="$HOME/miniconda/bin:$PATH"
              export ENV_NAME="py36-xonsh-test"
              if [ ! -d "/home/circleci/miniconda/envs/py36-xonsh-test" ]; then
                conda update -q conda
                conda env create -f ci/environment-${PYTHON}.yml --name=${ENV_NAME}
                source activate ${ENV_NAME}
              fi
              conda env list
              conda list ${ENV_NAME}
      - save_cache:
          key: miniconda-v1-{{ checksum "ci/environment-3.6.yml" }}
          paths:
            - "/home/circleci/miniconda"
      - run:
          command: |
            export PATH="$HOME/miniconda/bin:$PATH"
            source activate ${ENV_NAME}
            pip install . --no-deps
      - run:
          command: |
            export PATH="$HOME/miniconda/bin:$PATH"
            source activate ${ENV_NAME}
            xonsh run-tests.xsh --timeout=10 --flake8 --cov=./xonsh
  build_37:
    machine: true
    environment:
      PYTHON: "3.7"
      ENV_NAME: "py37-xonsh-test"
    steps:
      - checkout
      - restore_cache:
          keys:
            - miniconda-v1-{{ checksum "ci/environment-3.7.yml" }}
      - run:
          name: install miniconda
          command: |
              if [ ! -d "/home/circleci/miniconda" ]; then
                wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
                bash miniconda.sh -b -p $HOME/miniconda
                export PATH="$HOME/miniconda/bin:$PATH"
                conda config --set always_yes yes --set changeps1 no --set channel_priority strict
              fi
              sudo chown -R $USER.$USER $HOME
      - run:
          name: configure conda
          command: |
              export PATH="$HOME/miniconda/bin:$PATH"
              export ENV_NAME="py37-xonsh-test"
              if [ ! -d "/home/circleci/miniconda/envs/py37-xonsh-test" ]; then
                conda update -q conda
                conda env create -f ci/environment-${PYTHON}.yml --name=${ENV_NAME}
                source activate ${ENV_NAME}
              fi
              conda env list
              conda list ${ENV_NAME}
      - save_cache:
          key: miniconda-v1-{{ checksum "ci/environment-3.7.yml" }}
          paths:
            - "/home/circleci/miniconda"
      - run:
          command: |
            export PATH="$HOME/miniconda/bin:$PATH"
            source activate ${ENV_NAME}
            pip install . --no-deps
      - run:
          command: |
            export PATH="$HOME/miniconda/bin:$PATH"
            source activate ${ENV_NAME}
            xonsh run-tests.xsh --timeout=10 --flake8 --cov=./xonsh
  build_38:
    machine: true
    environment:
      PYTHON: "3.8"
      ENV_NAME: "py38-xonsh-test"
    steps:
      - checkout
      - restore_cache:
          keys:
            - miniconda-v1-{{ checksum "ci/environment-3.8.yml" }}
      - run:
          name: install miniconda
          command: |
              if [ ! -d "/home/circleci/miniconda" ]; then
                wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
                bash miniconda.sh -b -p $HOME/miniconda
                export PATH="$HOME/miniconda/bin:$PATH"
                conda config --set always_yes yes --set changeps1 no --set channel_priority strict
              fi
              sudo chown -R $USER.$USER $HOME
      - run:
          name: configure conda
          command: |
              export PATH="$HOME/miniconda/bin:$PATH"
              export ENV_NAME="py38-xonsh-test"
              if [ ! -d "/home/circleci/miniconda/envs/py38-xonsh-test" ]; then
                conda update -q conda
                conda env create -f ci/environment-${PYTHON}.yml --name=${ENV_NAME}
                source activate ${ENV_NAME}
              fi
              conda env list
              conda list ${ENV_NAME}
      - save_cache:
          key: miniconda-v1-{{ checksum "ci/environment-3.8.yml" }}
          paths:
            - "/home/circleci/miniconda"
      - run:
          command: |
            export PATH="$HOME/miniconda/bin:$PATH"
            source activate ${ENV_NAME}
            pip install . --no-deps
      - run:
          command: |
            export PATH="$HOME/miniconda/bin:$PATH"
            source activate ${ENV_NAME}
            xonsh run-tests.xsh --timeout=10 --flake8 --cov=./xonsh
  build_black:
    machine: true
    steps:
      - checkout
      - restore_cache:
          keys:
            - miniconda-v1-black
      - run:
          name: install miniconda
          command: |
              if [ ! -d "/home/circleci/miniconda" ]; then
                wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
                bash miniconda.sh -b -p $HOME/miniconda
                export PATH="$HOME/miniconda/bin:$PATH"
                conda config --set always_yes yes --set changeps1 no --set channel_priority strict
              fi
              sudo chown -R $USER.$USER $HOME
      - run:
          name: configure conda
          command: |
              export PATH="$HOME/miniconda/bin:$PATH"
              pip install black==18.9b0
      - save_cache:
          key: miniconda-v1-black
          paths:
            - "/home/circleci/miniconda"
      - run:
          command: |
            export PATH="$HOME/miniconda/bin:$PATH"
            black --check --exclude=xonsh/ply/ xonsh/ xontrib/
workflows:
  version: 2
  run_all_pythons:
    jobs:
      - build_35
      - build_36
      - build_37
      - build_black
      # conda-foge does not yet have all Python 3.8 packages available
      # uncomment when it does
      #- build_38
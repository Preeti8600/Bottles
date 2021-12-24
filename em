version: 1

# Please visit https://docs.embold.io/v2-quick-start-guide/#default-configurations 
#  to know more about configurations available

sources:
  #Files or Directories to be Excluded are mentioned in exclusions
  exclusions:
    - 'test'
    - 'generated'
    - 'mock'
    - 'thirdparty'
    - 'third-party'
    - '3rd-party'
    - '3rdparty'
    - 'external'
    - 'build'
    - 'node_modules'
    - 'assets'
    - 'gulp'
    - 'grunt'
    - 'library'
    - '.git'
    
# Specify the languages you would like to Scan. Default is all Detected
#languages: 'JAVA,CPP'


# Define modules one would like to run or disable. This is enough for Basic Users
# Get List of Modules (Which are Default Enabled/Disabled) at the documentation link above
#modules:
#  - name: pmd
#    enabled: true
#  - name: gamma_cxx
#    enabled: false
#  - name: jshint
#    enabled: true
modules:
  - name: pylint
    enabled: true
    config:
      - name: config
        value: data/icons/file1/configs/pyconf//pylintrc

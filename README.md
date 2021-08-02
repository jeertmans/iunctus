# iunctus

Connect your pictures using facial idenfication and quickly build beautiful slideshows!

## Features (future)

- [] use cli-based interface
- [] use web server interface
- [] use camera to identify person and
- [] create profiles for all people (ageing, friends, ...)
- [] easily move files without
- [] accelerate the process with GPU's or TPU's
- [] run this on an external server
- [] create a slideshow of groups of people / people appearing as often / ...

## TODO-list

- [] CLI
  - [] create a new project
  - [] have general config file (for video, cuda, # of threads, etc.)
  - [] have local config file (for folder, includes, excludes, etc.)
  - [] delete project
  - [] auto-locate current project
  - [] add pictures to project
  - [] remove pictures from project
  - [] list pictures in project
  - [] list people in project
  - [] add person in project
    - [] based on (new) picture
    - [] based on unknown faces in pictures
    - [] based on camera input
  - [] remove person from project
  - [] move a set of input pictures and udate their location
  - [] enter interactive mode
    - [] swipe trough pictures
      - [] random order
      - [] ordered (time, name)
      - [] same but through a slice (e.g.: a folder)
    - [] add people that are detected in pictures
    - [] remove false positives
    - [] add people that are not detected in pictures
  - [] add possibility to encrypt all the project data
  - [] list all pictures containing one or multiple people (union)
  - [] edit config
- [] WEB SERVER
  - [] ...
- [] FACIAL INDENFICATION
- [] NETWORK
  - [] connect people via the pictures they share
  - [] generate a list of photos that all contain a given person
  - [] generate a list of photos that equally contain a list of people
  - [] compute funny metrics about people relationships
    - [] closest person
    - [] closest X people
    - [] average pictures per person
    - [] pictures density (?)
    - [] ...
  - [] store network data into portable and light format
- [] ACCELERATION
  - [] use multiple cores
    - [] add cli option
    - [] default to multi-threaded
  - [] identify if CUDA is enabled
  - [] work on GPUs
  - [] work on RPis
  - [] work on CoralAI Dev Board Mini
- [] PUBLISH
  - [] create PYPI package
  - [] list requirements external to Python
  - [] create Linux binaries
  - [] create MacOS binaries
  - [] create Windows binaries
  - [] publish binaries on apt / ...

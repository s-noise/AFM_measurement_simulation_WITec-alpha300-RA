# AFM_measurement_simulation_WITec-alpha300-RAS
a python script for training and education purpose simulating an AFM measurement (session) of graphene on a WITec alpha300 RAS device.

This small program can be used for training or education purpose, e.g. in the context of an online practical class.
Therefore, no initial guidance is given in the program itself and no "back" button is added for the individual steps during the simulated session.
The individual steps of the simulation, ~"slide by slide" are listed in the *AFM_sim_instructions.txt* file, visible after unzip of the *images.zip* directory.

Compatible with Windows, Linux and MAC operating systems

The program contains screenshots of licensed software. The screenshots and the instruction file for individual measuerment steps *AFM_sim_instructions.txt* are password protected. Please send me a password request by e-mail to obtain the password which is needed to run the program: [stefan.noisternig@univie.ac.at](mailto:stefan.noisternig@univie.ac.at).


## Installation:
an example is given for Linux Systems

* download files: *AFM_sim_v1.py*, *images.zip* and *images.z01* in a directory

* combine zip archives *images.zip* & *images.z01* into new zip archive:
  - go to the directory with the files and open terminal:
    ```bash
     zip -F images.zip --out images_new.zip
     ```
             
* request password for zip archive:
  [stefan.noisternig@univie.ac.at](mailto:stefan.noisternig@univie.ac.at)
            
* extract the zip archive:
  ```bash
  unzip images_new.zip 
  ```
## run:
* the *images* folder and *AFM_sim_v1.py* must be in the same directory
* go to the directory and execute *AFM_sim_v1.py* in python 3
  - e.g. in Linux:
    ```bash
    python AFM_sim_v1.py
    ```
             

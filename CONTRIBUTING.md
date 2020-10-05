# Contributing

When contributing to this repository, please first discuss the change you wish to make via issue,
with the owners of this repository, before making a change. Each pull request must first be an issue.

## Pull Request Process
1. Fork the master repository.
2. Create a branch in your fork that matches the name of the issue your are working on.
3. Add the new feature or fix.
4. Run the unit tests and ensure that none fail.
5. Submit a pull request from your forked branch back to the master branch of the BlenderTools repository.
6. The pull request will be reviewed, then merged into the master branch and a new versioned build will be made.
7. Update the Wiki.

## Getting Setup
Fork the BlenderTools repository.

![1](https://blender-tools-documentation.s3.amazonaws.com/contributing/images/1.png?)

Create a branch in your fork with the name of the task/issue you are working on.

![2](https://blender-tools-documentation.s3.amazonaws.com/contributing/images/2.png?)

Clone your fork and checkout that branch:

`git clone https://github.com/<your-user-name>/BlenderTools.git`

`cd BlenderTools`

`git checkout <some-task-branch>`

## Testing Instructions
All files containing a TestCase class in `./test/unit_tests` will be run when the unit testing is run. (Note that any new features require an accompanying unit test for it to be approved.)

For the unit testing to work correctly, you will need to add both Blender and Unreal Engine to your system `PATH` variable. 

#### Windows:
Here are some example paths you might add:

`C:\Program Files\Blender Foundation\Blender <version>`

`C:\Program Files\Epic Games\UE_<version>\Engine\Binaries\Win64` 

You can add these by searching `Edit the system enviroment variables` in the quick search menu, then selecting it, then  `Environment Variables > Path > Edit..`

![3](https://blender-tools-documentation.s3.amazonaws.com/contributing/images/3.png?)

Add the full paths to the Blender and Unreal Engine executable directories.

![4](https://blender-tools-documentation.s3.amazonaws.com/contributing/images/4.png?)

Now click 'Ok' to all the dialogs. Open a new terminal at the root of the BlenderTools project, and run these commands to run the unit tests (note that the working directory has to be `./test/scripts`):

`cd ./test/scripts`

`python run_unit_tests.py`

If all went well you should see output similar to this:

    
    ----------------------------------------------------------------------
    Ran 11 tests in 33.714s

    OK
## Important Notes

### Our Standards
Our primary standard for code is [PEP 8](https://www.python.org/dev/peps/pep-0008/), overridden by any specific naming conventions recommended by the [blender python API](https://docs.blender.org/api/current/index.html):

* All functions and methods must have a descriptive docstring with all their parameter types and descriptions defined.
* Functions and methods should be `snake_case`.
* Classes should be `CamelCase`.
* All operators and any UI properties must have tool tips.

### Addon Code Structure

This is how the addon code is structured. You will see this primary file and folder structure in each of the addons.


    .
    ├── ...
    ├── addon                   # The root folder for the addon .zip
    │   ├── functions           # This folder contains all the functions that make up the addon core logic.
    │   ├── ui                  # This folder contains all UI classes for the addon.
    │   ├── __init__.py         # This contains the addon bl_info and register and unregister calls for all property groups, operators, and app handlers.
    │   ├── properties.py       # This file contains all the property group class definitions for the addon. All Addon properties should live in here.
    │   └── operators.py        # This file contains all operator class definitions. This serves as the entry point to all logic that lives in the functions module.
    └── ...

### Pull Request Check List
> 1: Did I bump the addon version in the `bl_info` dict of the `__init__.py` file? (i.e. `1.4.1` is `<core>.<new_feature>.<new_bug_fix>`)
>  
> 2: After making my change does it pass all of the unit tests?
>  
> 3: If I added a new feature, did a write a new unit test for it?
>
> 4: Did I update the documentation or leave a detailed description in the issue the change is associated with? Did I include good images or gifs?


### Have Questions?

Open an issue with a `question` label and we will get it answered.
# To create local repository

mkdir newproject
cd newproject

# Next we need to initialize the repository

git init

# Next we need to add a file to the project

touch readme.txt

# Now you will have an empty file in your repository

git status

# Even though git is aware of the file, it has not been added to the project

git add readme.txt ( add individual files )
git add -A ( add all files where changes have been made )
git status

# Your First commit, commit is a record of the file you have changed within the project
# Before we do this, we have to inform Git who we are
# If you are working with other developers they need to know who is making the changes

git config --global user.email senthilcaesar@yahoo.co.in
git config --global user.name senthilcaesar
git config --list
git help config
git log

# New we can create the commit

git commit -m "External dependecnies removed"

# Create a branch and push it to GitHub

git checkout -b gamemodules
git branch

# Next we need to create a repository on GitHub, Click the new repository button from
# your main page and click create repository
# After creating the repository you will be presented with a URL to use for pushing our new created local repository

git remote add origin https://github.com/SenthilCaesar/testapp
git push -u origin game

# Pulling the project
# Say your collaborators make changes to the code on the GitHub project and have merged those changes

git pull origin game

# clone branch
git clone -b remove-ext-dep https://github.com/pnlbwh/CNN-Diffusion-MRIBrain-Segmentation



# Example1
	# Pull the latest changes from branch
	git pull origin remove-ext-dep

	# Create new branch
	git checkout -b clean-imports

	# make the changes and commit it
	git push -u origin clean-imports
	
# When the user wants to intall your module from pip python or conda packages
# you will have to release your developed code in the github release tab

# Example 2
	# Initialize a repository from local existing code
		git init

	# If you want to stop tracking your repository, then remove the .git folder
		rm -rf .git

	# If you want to ignore few files from tracking , you have to create a .gitignore file
	# gitingnore file is a simple text file where we can add files that we want git to ignore
		*.pyc ( ignores all files with .pyc extension )

# Example 3
	# Track an existing github repository, the downaloded folder will already have a .git folder
		git clone https://github.com/SenthilCaesar/CNN-Brain-MRI-Segmentation.git

	# View information about the existing github repository
		git branch -a ( list all branches )
		git remote -v 

	 # Show me the changes that I have made to the code
	 	git diff 
	 	git status
	 	git add -A
	 	git status
	 	# now they are ready to be commited

	 # commit the changes locally
	 	git commit -m "multiply function added"

	 # Now we made changes locally , we want to push the changes to the remote github repository
	 # There are two things you want to do, git pull and git push 
	 # We are working on a project that could have mutiple developers
	 # And people have been pushing code to the remote repository, while you have been working on the features locally
	 	git pull origin master
	 	git push origin master 

	 # If you want to switch to different branch
	 	git checkout branchname
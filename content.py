# Contributions-Importer-For-Github/run_script.py
import git
from git_contributions_importer import *

# Your private repo or Bitbucket repo
repo = git.Repo("C:\\Users\\Pedro\\Documents\\codigos\\skedway\\skedway")

# Your mock repo

mock_repo = git.Repo("C:\\Users\\Pedro\\Documents\\codigos\\python\\Contributions-Importer-For-Github")
importer = Importer([repo], mock_repo)

# I use both my personal email and work email here,
# Since the private repo uses work email, and Github uses my personal email

importer.set_author(['contato.pgxv@gmail.com', 'pedro.veiga@skedway.com'])
importer.import_repository()

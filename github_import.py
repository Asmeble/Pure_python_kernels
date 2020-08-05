wget=__import__("requests").get
def Github_import(username, repo, branch, path_to_module):
  global wget
  return eval(repr(wget("https://raw.githubusercontent.com/"+username+"/"+repo+"/"+branch+"/"+path_to_module).text))

class Git_import(): 
  def __init__(self, username, repo, branch, path_to_module):
    self.username, self.repo, self.branch, self.path_to_module=username, repo, branch, path_to_module
    self.__all__=[]
  def __enter__(self):
    exec(Github_import(username=self.username,repo=self.repo,branch=self.branch, path_to_module=self.path_to_module))
    for a in dir():
      if a.count('self') != 1 and a.count('Github_import') != 1 :
        exec("self.{0}={0}".format(a))
    del self.branch, self.repo, self.path_to_module, self.username
    return self
  def __exit__(self, exc_type, exc_value, exc_traceback):
    del self
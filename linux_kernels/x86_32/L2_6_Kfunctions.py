def sys_write(fd, buf, count):
  """sys_write(fd, buf, count):
fd  --> a file descriptor to use. Currently [0, 1, 2] {standard in, out, and error} are the available options
buf --> the character you're writing to standard out, in all likelyhood...
count --> a numerical pointer that is unused as one character is fed through at a time..."""
  print(chr(buf),file={0:__import__("sys").stdin,1:__import__("sys").stdout,2:__import__("sys").stderr}.get(fd, fd), end='', flush=False)
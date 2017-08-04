from shutil import copyfile


#in copy(src, dst) the dst can be a directory
copyfile("C:/Users/Admin/Desktop/abc/joker.txt", "C:/Users/Admin/Desktop/xyz/bigjoker.txt")




"""Copy the contents of the file named src to a file named dst.
 The destination location must be writable; otherwise,
  an IOError exception will be raised.
   If dst already exists, it will be replaced.
   Special files such as character or block devices
   and pipes cannot be copied with this function.
 src and dst are path names given as strings. """

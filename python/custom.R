# A nice function to load packages.
# It checks if the required libraries are installed. If not installs them quietly and load to workspace.
# At the end it prints all loaded packages(libraries).
# for https:
# for https:
if (Sys.info()['sysname'] == "Windows") {
  # on windows:
  options(download.file.method = "wininet")
} else {
  # osx, linux
  options(download.file.method = "libcurl")
}
load.libraries <- function(libs) {
  for (package in libs) {
    if (!require(package, character.only = TRUE, quietly = TRUE)) {
      install.packages(package,
                       repos = "https://cran.ma.imperial.ac.uk/",
                       dependencies = TRUE)
      library(package, character.only = TRUE)
    }
  }
  print('Loaded packages: ')
  print(.packages())
}

#load.libraries <- function(libs) {
#  for (package in libs) {
#    if (!require(package, character.only = TRUE, quietly = TRUE)) {
#      install.packages(package,
#                       repos = "http://stat.ethz.ch/CRAN/",
#                       dependencies = TRUE)
#      library(package, character.only = TRUE)
#    }
#  }
#  print('Loaded packages: ')
#  print(.packages())
#}

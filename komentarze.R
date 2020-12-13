#' Load "Komentarze" corpus
#' @param path Path to main folder with "Komentarze" corpus
#'
#' @examples
#' load_komentarze(".")
load_komentarze <- function(path = "."){

  subfolders <- c(
    "Groźby karalne",
    "Obraźliwe",
    "Złośliwe",
    "Ostra krytyka",
    "Krytyka",
    "Pozostałe"
  )

  subfolders <- file.path(
    path, subfolders
  )

  dfs <- Map(.load_all_jsons, subfolders)
  dfs <- dplyr::bind_rows(dfs)
  dplyr::select(dfs, klasa, everything())
}

.load_all_jsons <- function(path){
  json_paths <- list.files(path, full.names = TRUE)
  parsed_files <- Map(jsonlite::fromJSON, json_paths)
  df <- dplyr::bind_rows(parsed_files)
  df$klasa <- basename(path)
  df
}

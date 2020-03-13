# Ruby Webcomics

> Source: http://imaginegen.github.io/main/2016/02/22/webcomics-reference.html

> Aliases: webcomics-docs, webcomics-spec, webcomics-documentation

$ Comics Directory
    `return_an_array_of_comics_entries(directory)
>                                  {{Returns an array of entries from a directory without previous and current directories}} 
    `return_comics_entries_without_file_extentions(array)
>                                  {{Returns an array of entries without file extentions}} 
    `is_this_series_path_a_directory?(series_path)
>                                  {{Returns true if the series path is a directory. Return false otherwise}} 
    `is_this_series_path_a_chapter?(series_path)
>                                  {{Returns true if the series path is a directory. Return false otherwise}} 
    `return_an_array_of_chapters(series_path)
>                                  {{Returns an array of all the directories within this series path}} 
    `is_this_series_path_a_page?(series_path)
>                                  {{Returns true if the series path is a file. Return false otherwise}} 
    `return_an_array_of_comics_pages(series_path)
>                                  {{Returns an array of all the files within this series path}} 
    `return_an_array_of_alpha_chapters(series_path)
>                                  {{Returns an array of all the directories within this series path that only consist of letters}} 
    `return_an_array_of_numeric_chapters(series_path)
>                                  {{Returns an array of all the directories within this series path that only consist of numbers}} 

$ Comics DB
    `is_there_a_db_field_value_that_matches_an_asset?
>                                  {{Returns true if a folder matching the folder name to the database field value. Returns false otherwise}} 
    `is_there_a_db_field_value_that_matches_a_series?
>                                  {{Returns true if a folder matching the folder name to the database field value. Returns false otherwise}} 

$ Comics Canvas
    `length_of_the_comic(series_path)
>                                  {{Returns the amount of pages in the series}} 
    `page_equalizer(page, series_path)
>                                  {{Returns the number of pages in the series path if the page number is less than zero. Returns zero if the number of pages is greater than or equal to the number of pages in the series path}} 

$ Comics Directory Helper
    `return_page(series_path, page = 0)
>                                  {{Returns a specified page. It takes two arguments; series_path should be the path to the series folder, and the page should be the index to the page you want to be returned from the array. By default, it returns the first page}} 
    `does_this_series_have_chapters?(series_path)
>                                  {{Returns true if the comic book series has chapters. Returns false otherwise}} 

$ Comics Engine
    `return_an_array_of_entries_without_image_files(array)
>                                  {{Returns an array of entries without image files and hash files.}} 
    `return_series_assets_directories(series_path)
>                                  {{Returns an array of entries with only assets. Assets are directories that are relevant to a “Comics Engine”. Those relevant directories are folders, and .cbz/.zip files}} 
    `return_an_array_of_pages(series_path = “”, path_to_cbz = “”)
>                                  {{Returns an array of entries from either a folder or a .cbz/.zip}} 


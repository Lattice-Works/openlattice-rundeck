# Rundeck
#
# No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
#
# The version of the OpenAPI document: 1.0.0
# 
# Generated by: https://openapi-generator.tech

#' @docType class
#' @title JobInputFileListResponse
#' @description JobInputFileListResponse Class
#' @format An \code{R6Class} generator object
#' @field paging  \link{Paging} 
#'
#' @field files  list( \link{JobInputFileInfo} ) 
#'
#'
#' @importFrom R6 R6Class
#' @importFrom jsonlite fromJSON toJSON
#' @export
JobInputFileListResponse <- R6::R6Class(
  'JobInputFileListResponse',
  public = list(
    `paging` = NULL,
    `files` = NULL,
    initialize = function(`paging`, `files`, ...){
      local.optional.var <- list(...)
      if (!missing(`paging`)) {
        stopifnot(R6::is.R6(`paging`))
        self$`paging` <- `paging`
      }
      if (!missing(`files`)) {
        stopifnot(is.vector(`files`), length(`files`) != 0)
        sapply(`files`, function(x) stopifnot(R6::is.R6(x)))
        self$`files` <- `files`
      }
    },
    toJSON = function() {
      JobInputFileListResponseObject <- list()
      if (!is.null(self$`paging`)) {
        JobInputFileListResponseObject[['paging']] <-
          self$`paging`$toJSON()
      }
      if (!is.null(self$`files`)) {
        JobInputFileListResponseObject[['files']] <-
          lapply(self$`files`, function(x) x$toJSON())
      }

      JobInputFileListResponseObject
    },
    fromJSON = function(JobInputFileListResponseJson) {
      JobInputFileListResponseObject <- jsonlite::fromJSON(JobInputFileListResponseJson)
      if (!is.null(JobInputFileListResponseObject$`paging`)) {
        pagingObject <- Paging$new()
        pagingObject$fromJSON(jsonlite::toJSON(JobInputFileListResponseObject$paging, auto_unbox = TRUE, digits = NA))
        self$`paging` <- pagingObject
      }
      if (!is.null(JobInputFileListResponseObject$`files`)) {
        self$`files` <- ApiClient$new()$deserializeObj(JobInputFileListResponseObject$`files`, "array[JobInputFileInfo]", loadNamespace("olrundeck"))
      }
    },
    toJSONString = function() {
      jsoncontent <- c(
        if (!is.null(self$`paging`)) {
        sprintf(
        '"paging":
        %s
        ',
        jsonlite::toJSON(self$`paging`$toJSON(), auto_unbox=TRUE, digits = NA)
        )},
        if (!is.null(self$`files`)) {
        sprintf(
        '"files":
        [%s]
',
        paste(sapply(self$`files`, function(x) jsonlite::toJSON(x$toJSON(), auto_unbox=TRUE, digits = NA)), collapse=",")
        )}
      )
      jsoncontent <- paste(jsoncontent, collapse = ",")
      paste('{', jsoncontent, '}', sep = "")
    },
    fromJSONString = function(JobInputFileListResponseJson) {
      JobInputFileListResponseObject <- jsonlite::fromJSON(JobInputFileListResponseJson)
      self$`paging` <- Paging$new()$fromJSON(jsonlite::toJSON(JobInputFileListResponseObject$paging, auto_unbox = TRUE, digits = NA))
      self$`files` <- ApiClient$new()$deserializeObj(JobInputFileListResponseObject$`files`, "array[JobInputFileInfo]", loadNamespace("olrundeck"))
      self
    }
  )
)

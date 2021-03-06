# Rundeck
#
# No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
#
# The version of the OpenAPI document: 1.0.0
# 
# Generated by: https://openapi-generator.tech

#' @docType class
#' @title BulkJobSucceededInfo
#' @description BulkJobSucceededInfo Class
#' @format An \code{R6Class} generator object
#' @field id  character 
#'
#' @field message  character 
#'
#'
#' @importFrom R6 R6Class
#' @importFrom jsonlite fromJSON toJSON
#' @export
BulkJobSucceededInfo <- R6::R6Class(
  'BulkJobSucceededInfo',
  public = list(
    `id` = NULL,
    `message` = NULL,
    initialize = function(`id`, `message`, ...){
      local.optional.var <- list(...)
      if (!missing(`id`)) {
        stopifnot(is.character(`id`), length(`id`) == 1)
        self$`id` <- `id`
      }
      if (!missing(`message`)) {
        stopifnot(is.character(`message`), length(`message`) == 1)
        self$`message` <- `message`
      }
    },
    toJSON = function() {
      BulkJobSucceededInfoObject <- list()
      if (!is.null(self$`id`)) {
        BulkJobSucceededInfoObject[['id']] <-
          self$`id`
      }
      if (!is.null(self$`message`)) {
        BulkJobSucceededInfoObject[['message']] <-
          self$`message`
      }

      BulkJobSucceededInfoObject
    },
    fromJSON = function(BulkJobSucceededInfoJson) {
      BulkJobSucceededInfoObject <- jsonlite::fromJSON(BulkJobSucceededInfoJson)
      if (!is.null(BulkJobSucceededInfoObject$`id`)) {
        self$`id` <- BulkJobSucceededInfoObject$`id`
      }
      if (!is.null(BulkJobSucceededInfoObject$`message`)) {
        self$`message` <- BulkJobSucceededInfoObject$`message`
      }
    },
    toJSONString = function() {
      jsoncontent <- c(
        if (!is.null(self$`id`)) {
        sprintf(
        '"id":
          "%s"
                ',
        self$`id`
        )},
        if (!is.null(self$`message`)) {
        sprintf(
        '"message":
          "%s"
                ',
        self$`message`
        )}
      )
      jsoncontent <- paste(jsoncontent, collapse = ",")
      paste('{', jsoncontent, '}', sep = "")
    },
    fromJSONString = function(BulkJobSucceededInfoJson) {
      BulkJobSucceededInfoObject <- jsonlite::fromJSON(BulkJobSucceededInfoJson)
      self$`id` <- BulkJobSucceededInfoObject$`id`
      self$`message` <- BulkJobSucceededInfoObject$`message`
      self
    }
  )
)

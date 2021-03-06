# Rundeck
#
# No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
#
# The version of the OpenAPI document: 1.0.0
# 
# Generated by: https://openapi-generator.tech

#' @docType class
#' @title InlineObject7
#' @description InlineObject7 Class
#' @format An \code{R6Class} generator object
#' @field value  character [optional]
#'
#'
#' @importFrom R6 R6Class
#' @importFrom jsonlite fromJSON toJSON
#' @export
InlineObject7 <- R6::R6Class(
  'InlineObject7',
  public = list(
    `value` = NULL,
    initialize = function(`value`=NULL, ...){
      local.optional.var <- list(...)
      if (!is.null(`value`)) {
        stopifnot(is.character(`value`), length(`value`) == 1)
        self$`value` <- `value`
      }
    },
    toJSON = function() {
      InlineObject7Object <- list()
      if (!is.null(self$`value`)) {
        InlineObject7Object[['value']] <-
          self$`value`
      }

      InlineObject7Object
    },
    fromJSON = function(InlineObject7Json) {
      InlineObject7Object <- jsonlite::fromJSON(InlineObject7Json)
      if (!is.null(InlineObject7Object$`value`)) {
        self$`value` <- InlineObject7Object$`value`
      }
    },
    toJSONString = function() {
      jsoncontent <- c(
        if (!is.null(self$`value`)) {
        sprintf(
        '"value":
          "%s"
                ',
        self$`value`
        )}
      )
      jsoncontent <- paste(jsoncontent, collapse = ",")
      paste('{', jsoncontent, '}', sep = "")
    },
    fromJSONString = function(InlineObject7Json) {
      InlineObject7Object <- jsonlite::fromJSON(InlineObject7Json)
      self$`value` <- InlineObject7Object$`value`
      self
    }
  )
)

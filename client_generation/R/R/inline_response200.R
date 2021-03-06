# Rundeck
#
# No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
#
# The version of the OpenAPI document: 1.0.0
# 
# Generated by: https://openapi-generator.tech

#' @docType class
#' @title InlineResponse200
#' @description InlineResponse200 Class
#' @format An \code{R6Class} generator object
#' @field name  character [optional]
#'
#' @field description  character [optional]
#'
#' @field url  character [optional]
#'
#' @field label  character [optional]
#'
#'
#' @importFrom R6 R6Class
#' @importFrom jsonlite fromJSON toJSON
#' @export
InlineResponse200 <- R6::R6Class(
  'InlineResponse200',
  public = list(
    `name` = NULL,
    `description` = NULL,
    `url` = NULL,
    `label` = NULL,
    initialize = function(`name`=NULL, `description`=NULL, `url`=NULL, `label`=NULL, ...){
      local.optional.var <- list(...)
      if (!is.null(`name`)) {
        stopifnot(is.character(`name`), length(`name`) == 1)
        self$`name` <- `name`
      }
      if (!is.null(`description`)) {
        stopifnot(is.character(`description`), length(`description`) == 1)
        self$`description` <- `description`
      }
      if (!is.null(`url`)) {
        stopifnot(is.character(`url`), length(`url`) == 1)
        self$`url` <- `url`
      }
      if (!is.null(`label`)) {
        stopifnot(is.character(`label`), length(`label`) == 1)
        self$`label` <- `label`
      }
    },
    toJSON = function() {
      InlineResponse200Object <- list()
      if (!is.null(self$`name`)) {
        InlineResponse200Object[['name']] <-
          self$`name`
      }
      if (!is.null(self$`description`)) {
        InlineResponse200Object[['description']] <-
          self$`description`
      }
      if (!is.null(self$`url`)) {
        InlineResponse200Object[['url']] <-
          self$`url`
      }
      if (!is.null(self$`label`)) {
        InlineResponse200Object[['label']] <-
          self$`label`
      }

      InlineResponse200Object
    },
    fromJSON = function(InlineResponse200Json) {
      InlineResponse200Object <- jsonlite::fromJSON(InlineResponse200Json)
      if (!is.null(InlineResponse200Object$`name`)) {
        self$`name` <- InlineResponse200Object$`name`
      }
      if (!is.null(InlineResponse200Object$`description`)) {
        self$`description` <- InlineResponse200Object$`description`
      }
      if (!is.null(InlineResponse200Object$`url`)) {
        self$`url` <- InlineResponse200Object$`url`
      }
      if (!is.null(InlineResponse200Object$`label`)) {
        self$`label` <- InlineResponse200Object$`label`
      }
    },
    toJSONString = function() {
      jsoncontent <- c(
        if (!is.null(self$`name`)) {
        sprintf(
        '"name":
          "%s"
                ',
        self$`name`
        )},
        if (!is.null(self$`description`)) {
        sprintf(
        '"description":
          "%s"
                ',
        self$`description`
        )},
        if (!is.null(self$`url`)) {
        sprintf(
        '"url":
          "%s"
                ',
        self$`url`
        )},
        if (!is.null(self$`label`)) {
        sprintf(
        '"label":
          "%s"
                ',
        self$`label`
        )}
      )
      jsoncontent <- paste(jsoncontent, collapse = ",")
      paste('{', jsoncontent, '}', sep = "")
    },
    fromJSONString = function(InlineResponse200Json) {
      InlineResponse200Object <- jsonlite::fromJSON(InlineResponse200Json)
      self$`name` <- InlineResponse200Object$`name`
      self$`description` <- InlineResponse200Object$`description`
      self$`url` <- InlineResponse200Object$`url`
      self$`label` <- InlineResponse200Object$`label`
      self
    }
  )
)

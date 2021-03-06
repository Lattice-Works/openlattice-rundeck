# Rundeck
#
# No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
#
# The version of the OpenAPI document: 1.0.0
# 
# Generated by: https://openapi-generator.tech

#' @docType class
#' @title ModifyUserRequest
#' @description ModifyUserRequest Class
#' @format An \code{R6Class} generator object
#' @field firstName  character [optional]
#'
#' @field lastName  character [optional]
#'
#' @field email  character [optional]
#'
#'
#' @importFrom R6 R6Class
#' @importFrom jsonlite fromJSON toJSON
#' @export
ModifyUserRequest <- R6::R6Class(
  'ModifyUserRequest',
  public = list(
    `firstName` = NULL,
    `lastName` = NULL,
    `email` = NULL,
    initialize = function(`firstName`=NULL, `lastName`=NULL, `email`=NULL, ...){
      local.optional.var <- list(...)
      if (!is.null(`firstName`)) {
        stopifnot(is.character(`firstName`), length(`firstName`) == 1)
        self$`firstName` <- `firstName`
      }
      if (!is.null(`lastName`)) {
        stopifnot(is.character(`lastName`), length(`lastName`) == 1)
        self$`lastName` <- `lastName`
      }
      if (!is.null(`email`)) {
        stopifnot(is.character(`email`), length(`email`) == 1)
        self$`email` <- `email`
      }
    },
    toJSON = function() {
      ModifyUserRequestObject <- list()
      if (!is.null(self$`firstName`)) {
        ModifyUserRequestObject[['firstName']] <-
          self$`firstName`
      }
      if (!is.null(self$`lastName`)) {
        ModifyUserRequestObject[['lastName']] <-
          self$`lastName`
      }
      if (!is.null(self$`email`)) {
        ModifyUserRequestObject[['email']] <-
          self$`email`
      }

      ModifyUserRequestObject
    },
    fromJSON = function(ModifyUserRequestJson) {
      ModifyUserRequestObject <- jsonlite::fromJSON(ModifyUserRequestJson)
      if (!is.null(ModifyUserRequestObject$`firstName`)) {
        self$`firstName` <- ModifyUserRequestObject$`firstName`
      }
      if (!is.null(ModifyUserRequestObject$`lastName`)) {
        self$`lastName` <- ModifyUserRequestObject$`lastName`
      }
      if (!is.null(ModifyUserRequestObject$`email`)) {
        self$`email` <- ModifyUserRequestObject$`email`
      }
    },
    toJSONString = function() {
      jsoncontent <- c(
        if (!is.null(self$`firstName`)) {
        sprintf(
        '"firstName":
          "%s"
                ',
        self$`firstName`
        )},
        if (!is.null(self$`lastName`)) {
        sprintf(
        '"lastName":
          "%s"
                ',
        self$`lastName`
        )},
        if (!is.null(self$`email`)) {
        sprintf(
        '"email":
          "%s"
                ',
        self$`email`
        )}
      )
      jsoncontent <- paste(jsoncontent, collapse = ",")
      paste('{', jsoncontent, '}', sep = "")
    },
    fromJSONString = function(ModifyUserRequestJson) {
      ModifyUserRequestObject <- jsonlite::fromJSON(ModifyUserRequestJson)
      self$`firstName` <- ModifyUserRequestObject$`firstName`
      self$`lastName` <- ModifyUserRequestObject$`lastName`
      self$`email` <- ModifyUserRequestObject$`email`
      self
    }
  )
)

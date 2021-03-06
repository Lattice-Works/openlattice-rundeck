# Rundeck
#
# No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
#
# The version of the OpenAPI document: 1.0.0
# 
# Generated by: https://openapi-generator.tech

#' @docType class
#' @title Project
#' @description Project Class
#' @format An \code{R6Class} generator object
#' @field description  character [optional]
#'
#' @field name  character [optional]
#'
#' @field url  character [optional]
#'
#' @field config  object [optional]
#'
#'
#' @importFrom R6 R6Class
#' @importFrom jsonlite fromJSON toJSON
#' @export
Project <- R6::R6Class(
  'Project',
  public = list(
    `description` = NULL,
    `name` = NULL,
    `url` = NULL,
    `config` = NULL,
    initialize = function(`description`=NULL, `name`=NULL, `url`=NULL, `config`=NULL, ...){
      local.optional.var <- list(...)
      if (!is.null(`description`)) {
        stopifnot(is.character(`description`), length(`description`) == 1)
        self$`description` <- `description`
      }
      if (!is.null(`name`)) {
        stopifnot(is.character(`name`), length(`name`) == 1)
        self$`name` <- `name`
      }
      if (!is.null(`url`)) {
        stopifnot(is.character(`url`), length(`url`) == 1)
        self$`url` <- `url`
      }
      if (!is.null(`config`)) {
        self$`config` <- `config`
      }
    },
    toJSON = function() {
      ProjectObject <- list()
      if (!is.null(self$`description`)) {
        ProjectObject[['description']] <-
          self$`description`
      }
      if (!is.null(self$`name`)) {
        ProjectObject[['name']] <-
          self$`name`
      }
      if (!is.null(self$`url`)) {
        ProjectObject[['url']] <-
          self$`url`
      }
      if (!is.null(self$`config`)) {
        ProjectObject[['config']] <-
          self$`config`
      }

      ProjectObject
    },
    fromJSON = function(ProjectJson) {
      ProjectObject <- jsonlite::fromJSON(ProjectJson)
      if (!is.null(ProjectObject$`description`)) {
        self$`description` <- ProjectObject$`description`
      }
      if (!is.null(ProjectObject$`name`)) {
        self$`name` <- ProjectObject$`name`
      }
      if (!is.null(ProjectObject$`url`)) {
        self$`url` <- ProjectObject$`url`
      }
      if (!is.null(ProjectObject$`config`)) {
        self$`config` <- ProjectObject$`config`
      }
    },
    toJSONString = function() {
      jsoncontent <- c(
        if (!is.null(self$`description`)) {
        sprintf(
        '"description":
          "%s"
                ',
        self$`description`
        )},
        if (!is.null(self$`name`)) {
        sprintf(
        '"name":
          "%s"
                ',
        self$`name`
        )},
        if (!is.null(self$`url`)) {
        sprintf(
        '"url":
          "%s"
                ',
        self$`url`
        )},
        if (!is.null(self$`config`)) {
        sprintf(
        '"config":
          "%s"
                ',
        self$`config`
        )}
      )
      jsoncontent <- paste(jsoncontent, collapse = ",")
      paste('{', jsoncontent, '}', sep = "")
    },
    fromJSONString = function(ProjectJson) {
      ProjectObject <- jsonlite::fromJSON(ProjectJson)
      self$`description` <- ProjectObject$`description`
      self$`name` <- ProjectObject$`name`
      self$`url` <- ProjectObject$`url`
      self$`config` <- ProjectObject$`config`
      self
    }
  )
)

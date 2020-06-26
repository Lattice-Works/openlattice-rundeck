# Rundeck
#
# No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
#
# The version of the OpenAPI document: 1.0.0
# 
# Generated by: https://openapi-generator.tech

#' @docType class
#' @title Acl operations
#' @description openlattice-rundeck.Acl
#' @format An \code{R6Class} generator object
#' @field apiClient Handles the client-server communication.
#'
#' @section Methods:
#' \describe{
#' \strong{ system_acl_policy_delete } \emph{ Delete policy }
#' 
#'
#' \itemize{
#' \item \emph{ @param } policy_name character
#'
#'
#' \item status code : 200 | Success !
#'
#'
#' \item response headers :
#'
#' \tabular{ll}{
#' }
#' }
#'
#' }
#'
#'
#' @examples
#' \dontrun{
#' ####################  system_acl_policy_delete  ####################
#'
#' library(openlattice-rundeck)
#' var.policy_name <- 'policy_name_example' # character | Policy file name
#'
#' #Delete policy
#' api.instance <- AclApi$new()
#'
#' result <- api.instance$system_acl_policy_delete(var.policy_name)
#'
#'
#' }
#' @importFrom R6 R6Class
#' @importFrom base64enc base64encode
#' @export
AclApi <- R6::R6Class(
  'AclApi',
  public = list(
    apiClient = NULL,
    initialize = function(apiClient){
      if (!missing(apiClient)) {
        self$apiClient <- apiClient
      }
      else {
        self$apiClient <- ApiClient$new()
      }
    },
    system_acl_policy_delete = function(policy_name, ...){
      apiResponse <- self$system_acl_policy_deleteWithHttpInfo(policy_name, ...)
      resp <- apiResponse$response
      if (httr::status_code(resp) >= 200 && httr::status_code(resp) <= 299) {
        apiResponse$content
      } else if (httr::status_code(resp) >= 300 && httr::status_code(resp) <= 399) {
        apiResponse
      } else if (httr::status_code(resp) >= 400 && httr::status_code(resp) <= 499) {
        apiResponse
      } else if (httr::status_code(resp) >= 500 && httr::status_code(resp) <= 599) {
        apiResponse
      }
    },

    system_acl_policy_deleteWithHttpInfo = function(policy_name, ...){
      args <- list(...)
      queryParams <- list()
      headerParams <- c()

      if (missing(`policy_name`)) {
        stop("Missing required parameter `policy_name`.")
      }

      urlPath <- "/api/26/system/acl/{policyName}"
      if (!missing(`policy_name`)) {
        urlPath <- gsub(paste0("\\{", "policyName", "\\}"), URLencode(as.character(`policy_name`), reserved = TRUE), urlPath)
      }


      resp <- self$apiClient$CallApi(url = paste0(self$apiClient$basePath, urlPath),
                                 method = "DELETE",
                                 queryParams = queryParams,
                                 headerParams = headerParams,
                                 body = body,
                                 ...)

      if (httr::status_code(resp) >= 200 && httr::status_code(resp) <= 299) {
        ApiResponse$new(NULL, resp)
      } else if (httr::status_code(resp) >= 300 && httr::status_code(resp) <= 399) {
        ApiResponse$new(paste("Server returned " , httr::status_code(resp) , " response status code."), resp)
      } else if (httr::status_code(resp) >= 400 && httr::status_code(resp) <= 499) {
        ApiResponse$new("API client error", resp)
      } else if (httr::status_code(resp) >= 500 && httr::status_code(resp) <= 599) {
        ApiResponse$new("API server error", resp)
      }
    }
  )
)
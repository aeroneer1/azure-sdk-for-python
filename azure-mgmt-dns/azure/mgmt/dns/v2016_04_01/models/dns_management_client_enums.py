# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class OperationStatus(str, Enum):

    in_progress = "InProgress"
    succeeded = "Succeeded"
    failed = "Failed"


class HttpStatusCode(str, Enum):

    continue_enum = "Continue"
    switching_protocols = "SwitchingProtocols"
    ok = "OK"
    created = "Created"
    accepted = "Accepted"
    non_authoritative_information = "NonAuthoritativeInformation"
    no_content = "NoContent"
    reset_content = "ResetContent"
    partial_content = "PartialContent"
    multiple_choices = "MultipleChoices"
    ambiguous = "Ambiguous"
    moved_permanently = "MovedPermanently"
    moved = "Moved"
    found = "Found"
    redirect = "Redirect"
    see_other = "SeeOther"
    redirect_method = "RedirectMethod"
    not_modified = "NotModified"
    use_proxy = "UseProxy"
    unused = "Unused"
    temporary_redirect = "TemporaryRedirect"
    redirect_keep_verb = "RedirectKeepVerb"
    bad_request = "BadRequest"
    unauthorized = "Unauthorized"
    payment_required = "PaymentRequired"
    forbidden = "Forbidden"
    not_found = "NotFound"
    method_not_allowed = "MethodNotAllowed"
    not_acceptable = "NotAcceptable"
    proxy_authentication_required = "ProxyAuthenticationRequired"
    request_timeout = "RequestTimeout"
    conflict = "Conflict"
    gone = "Gone"
    length_required = "LengthRequired"
    precondition_failed = "PreconditionFailed"
    request_entity_too_large = "RequestEntityTooLarge"
    request_uri_too_long = "RequestUriTooLong"
    unsupported_media_type = "UnsupportedMediaType"
    requested_range_not_satisfiable = "RequestedRangeNotSatisfiable"
    expectation_failed = "ExpectationFailed"
    upgrade_required = "UpgradeRequired"
    internal_server_error = "InternalServerError"
    not_implemented = "NotImplemented"
    bad_gateway = "BadGateway"
    service_unavailable = "ServiceUnavailable"
    gateway_timeout = "GatewayTimeout"
    http_version_not_supported = "HttpVersionNotSupported"


class RecordType(str, Enum):

    a = "A"
    aaaa = "AAAA"
    cname = "CNAME"
    mx = "MX"
    ns = "NS"
    ptr = "PTR"
    soa = "SOA"
    srv = "SRV"
    txt = "TXT"

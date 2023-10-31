// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Cognito
{
    public static class GetUserPoolClient
    {
        /// <summary>
        /// Resource Type definition for AWS::Cognito::UserPoolClient
        /// </summary>
        public static Task<GetUserPoolClientResult> InvokeAsync(GetUserPoolClientArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetUserPoolClientResult>("aws-native:cognito:getUserPoolClient", args ?? new GetUserPoolClientArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::Cognito::UserPoolClient
        /// </summary>
        public static Output<GetUserPoolClientResult> Invoke(GetUserPoolClientInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetUserPoolClientResult>("aws-native:cognito:getUserPoolClient", args ?? new GetUserPoolClientInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetUserPoolClientArgs : global::Pulumi.InvokeArgs
    {
        [Input("clientId", required: true)]
        public string ClientId { get; set; } = null!;

        [Input("userPoolId", required: true)]
        public string UserPoolId { get; set; } = null!;

        public GetUserPoolClientArgs()
        {
        }
        public static new GetUserPoolClientArgs Empty => new GetUserPoolClientArgs();
    }

    public sealed class GetUserPoolClientInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("clientId", required: true)]
        public Input<string> ClientId { get; set; } = null!;

        [Input("userPoolId", required: true)]
        public Input<string> UserPoolId { get; set; } = null!;

        public GetUserPoolClientInvokeArgs()
        {
        }
        public static new GetUserPoolClientInvokeArgs Empty => new GetUserPoolClientInvokeArgs();
    }


    [OutputType]
    public sealed class GetUserPoolClientResult
    {
        public readonly int? AccessTokenValidity;
        public readonly ImmutableArray<string> AllowedOAuthFlows;
        public readonly bool? AllowedOAuthFlowsUserPoolClient;
        public readonly ImmutableArray<string> AllowedOAuthScopes;
        public readonly Outputs.UserPoolClientAnalyticsConfiguration? AnalyticsConfiguration;
        public readonly int? AuthSessionValidity;
        public readonly ImmutableArray<string> CallbackUrls;
        public readonly string? ClientId;
        public readonly string? ClientName;
        public readonly string? ClientSecret;
        public readonly string? DefaultRedirectUri;
        public readonly bool? EnablePropagateAdditionalUserContextData;
        public readonly bool? EnableTokenRevocation;
        public readonly ImmutableArray<string> ExplicitAuthFlows;
        public readonly int? IdTokenValidity;
        public readonly ImmutableArray<string> LogoutUrls;
        public readonly string? Name;
        public readonly string? PreventUserExistenceErrors;
        public readonly ImmutableArray<string> ReadAttributes;
        public readonly int? RefreshTokenValidity;
        public readonly ImmutableArray<string> SupportedIdentityProviders;
        public readonly Outputs.UserPoolClientTokenValidityUnits? TokenValidityUnits;
        public readonly ImmutableArray<string> WriteAttributes;

        [OutputConstructor]
        private GetUserPoolClientResult(
            int? accessTokenValidity,

            ImmutableArray<string> allowedOAuthFlows,

            bool? allowedOAuthFlowsUserPoolClient,

            ImmutableArray<string> allowedOAuthScopes,

            Outputs.UserPoolClientAnalyticsConfiguration? analyticsConfiguration,

            int? authSessionValidity,

            ImmutableArray<string> callbackUrls,

            string? clientId,

            string? clientName,

            string? clientSecret,

            string? defaultRedirectUri,

            bool? enablePropagateAdditionalUserContextData,

            bool? enableTokenRevocation,

            ImmutableArray<string> explicitAuthFlows,

            int? idTokenValidity,

            ImmutableArray<string> logoutUrls,

            string? name,

            string? preventUserExistenceErrors,

            ImmutableArray<string> readAttributes,

            int? refreshTokenValidity,

            ImmutableArray<string> supportedIdentityProviders,

            Outputs.UserPoolClientTokenValidityUnits? tokenValidityUnits,

            ImmutableArray<string> writeAttributes)
        {
            AccessTokenValidity = accessTokenValidity;
            AllowedOAuthFlows = allowedOAuthFlows;
            AllowedOAuthFlowsUserPoolClient = allowedOAuthFlowsUserPoolClient;
            AllowedOAuthScopes = allowedOAuthScopes;
            AnalyticsConfiguration = analyticsConfiguration;
            AuthSessionValidity = authSessionValidity;
            CallbackUrls = callbackUrls;
            ClientId = clientId;
            ClientName = clientName;
            ClientSecret = clientSecret;
            DefaultRedirectUri = defaultRedirectUri;
            EnablePropagateAdditionalUserContextData = enablePropagateAdditionalUserContextData;
            EnableTokenRevocation = enableTokenRevocation;
            ExplicitAuthFlows = explicitAuthFlows;
            IdTokenValidity = idTokenValidity;
            LogoutUrls = logoutUrls;
            Name = name;
            PreventUserExistenceErrors = preventUserExistenceErrors;
            ReadAttributes = readAttributes;
            RefreshTokenValidity = refreshTokenValidity;
            SupportedIdentityProviders = supportedIdentityProviders;
            TokenValidityUnits = tokenValidityUnits;
            WriteAttributes = writeAttributes;
        }
    }
}
